import datetime
import logging
import re

from codicefiscale import codicefiscale
from rapidfuzz.distance import Levenshtein
import gender_guesser.detector as gender_detector
import pandas as pd

from .fiscal_countries import FiscalCountries
from .utils import is_empty
from .places_infer import get_country_alpha_from_name

logger = logging.getLogger(__name__)

_gender_detector = gender_detector.Detector(case_sensitive=False)

DATETIME_PLACEHOLDER = datetime.date(year=1970, month=1, day=1)

cf_error_counts = pd.Series({
    'birthdate': 0,
    'birthplace': 0,
    'gender': 0,
    'cf': 0,
    'not_recoverable_cf': 0,
    'no_data': 0
})


# ---------------------------------------------------------------------------
# GENDER INFERENCE
# ---------------------------------------------------------------------------

def compute_gender_by_name(cf_gender, db_gender, name, min_confidence=0.55) -> str:
    """
    Inferisce il genere combinando CF (0.85), DB (0.30) e nome (0.65-0.90).
    Lancia ValueError se la confidenza e' sotto min_confidence.
    """
    signals = []

    if not is_empty(cf_gender):
        signals.append(('cf', cf_gender.lower(), 0.85))
    if not is_empty(db_gender):
        signals.append(('db', db_gender.lower(), 0.30))
    if not is_empty(name):
        first = str(name).strip().split()[0]
        guess = _gender_detector.get_gender(first, 'italy')
        name_map = {
            'male': ('m', 0.90),
            'mostly_male': ('m', 0.65),
            'female': ('f', 0.90),
            'mostly_female': ('f', 0.65),
        }
        if guess in name_map:
            g, w = name_map[guess]
            signals.append(('nome', g, w))

    if not signals:
        raise ValueError(f"Nessun segnale per inferire il genere (name={name!r})")

    score = {'m': 0.0, 'f': 0.0}
    for _, g, w in signals:
        if g in score:
            score[g] += w

    best = max(score, key=score.__getitem__)
    confidence = score[best] / sum(score.values())

    if confidence < min_confidence:
        raise ValueError(
            f"Confidenza genere troppo bassa ({confidence:.0%}): "
            f"cf={cf_gender!r}, db={db_gender!r}, name={name!r}"
        )

    return best


# ---------------------------------------------------------------------------
# CF RECOMPUTE
# ---------------------------------------------------------------------------

def _build_birthplace_str(birth_country, birth_province, birth_comune) -> str:
    """
    Costruisce la stringa birthplace per codicefiscale.encode.
    Italiani: "Comune (PR)"
    Esteri:   solo nome citta' (codicefiscale ha il suo DB interno)
    """
    if birth_country == 'Italia':
        return f'{birth_comune} ({birth_province})'
    return birth_comune


def full_recompute_cf(name, surname, birth_country, birth_province,
                      birth_comune, birthdate, gender) -> str:
    """
    Ricalcola il CF dai dati anagrafici.
    Lancia ValueError se i dati sono insufficienti o il calcolo fallisce.
    """
    global cf_error_counts

    missing = [k for k, v in {
        'name': name, 'surname': surname,
        'birth_country': birth_country, 'birth_province': birth_province,
        'birth_comune': birth_comune, 'birthdate': birthdate, 'gender': gender
    }.items() if is_empty(v)]

    if missing:
        cf_error_counts['no_data'] += 1
        cf_error_counts['not_recoverable_cf'] += 1
        raise ValueError(
            f"Dati insufficienti per ricalcolare CF: "
            f"name={name!r}, surname={surname!r}, "
            f"birthplace=({birth_country!r}, {birth_province!r}, {birth_comune!r}), "
            f"birthdate={birthdate!r}, gender={gender!r}. "
            f"Campi mancanti: {missing}"
        )

    birthplace = _build_birthplace_str(birth_country, birth_province, birth_comune)

    try:
        return codicefiscale.encode(
            lastname=surname,
            firstname=name,
            birthplace=birthplace,
            birthdate=birthdate,
            gender=gender,
        )
    except ValueError as e:
        cf_error_counts['not_recoverable_cf'] += 1
        r = f"lastname={surname!r}, firstname={name!r}, {birthplace!r}, {birthdate!r}, gender={gender!r} "
        raise ValueError(f"Impossibile codificare CF: {e}, {r}") from e


# ---------------------------------------------------------------------------
# BIRTHPLACE FROM CF
# ---------------------------------------------------------------------------


def infer_birthplace_cf(raw_cf: dict) -> tuple:
    """Estrae (country, province, city) dal CF decodificato."""

    if raw_cf['birthplace']['province'] == 'EE':
        cf_province = 'EE'
        cf_city = pd.NA
        cf_city_code = pd.NA
        fc = FiscalCountries()
        fiscal_code = raw_cf['birthplace']['code']

        if not fc.valid_country_code(fiscal_code):
            return pd.NA, pd.NA, pd.NA, pd.NA

        cf_country = fc.get_name(fiscal_code)
        cf_country_code = fc.get_code(fiscal_code)
    else:
        cf_province = raw_cf['birthplace']['province']
        cf_city = raw_cf['birthplace']['name']
        cf_city_code = raw_cf['birthplace']['code']
        cf_country = 'Italia'
        cf_country_code = 'Italy'

    return cf_country, cf_province, cf_city, cf_city_code, cf_country_code


# ---------------------------------------------------------------------------
# ENCODE CF CON FALLBACK PER ESTERI
# ---------------------------------------------------------------------------

def _encode_cf(name, surname, birthdate, gender,
               birth_country, birth_province, birth_comune) -> str:
    """
    Codifica il CF. Per gli esteri prova in sequenza:
    citta', sigla provincia, paese.
    Lancia ValueError se nessun tentativo funziona.
    """
    if birth_country == 'Italia':
        return codicefiscale.encode(
            lastname=surname,
            firstname=name,
            birthplace=birth_comune,
            birthdate=birthdate,
            gender=gender,
        )

    last_exc = None
    for birthplace_try in [birth_comune, birth_province, birth_country]:
        if is_empty(birthplace_try):
            continue
        try:
            return codicefiscale.encode(
                lastname=surname,
                firstname=name,
                birthplace=birthplace_try,
                birthdate=birthdate,
                gender=gender,
            )
        except ValueError as e:
            last_exc = e

    raise ValueError(
        f"Impossibile codificare CF per estero: "
        f"comune={birth_comune!r}, province={birth_province!r}, "
        f"country={birth_country!r}"
    ) from last_exc


# ---------------------------------------------------------------------------
# FUNZIONE PRINCIPALE
# ---------------------------------------------------------------------------

def check_fiscal_data(row: pd.Series) -> pd.Series:
    """
    Valida e corregge i dati anagrafici di una riga.
    Lancia ValueError se i dati non sono recuperabili.
    """
    global cf_error_counts

    name = row['first_name']
    surname = row['last_name']
    gender = row['gender']
    birth_country = row['birth_country']
    birth_province = row['birth_province']
    birth_comune = row['birth_comune']
    birthdate = row['birthdate']
    fiscal_code = row['fiscal_code']

    # ------------------------------------------------------------------
    # STEP 1: Assicurati di avere un CF valido
    # ------------------------------------------------------------------
    if is_empty(fiscal_code):
        fiscal_code = full_recompute_cf(
            name, surname, birth_country, birth_province,
            birth_comune, birthdate, gender
        )

    # Sanifica: stringa uppercase senza spazi
    fiscal_code = str(fiscal_code).strip().upper()
    if fiscal_code in ('NAN', 'NONE', ''):
        raise ValueError(f"CF non valido: {fiscal_code!r}")

    # Decodifica
    try:
        raw_data = codicefiscale.decode(fiscal_code)
    except ValueError as e:
        cf_error_counts['cf'] += 1
        if 'wrong CIN' in str(e):
            match = re.search(r"expected '(\w)'", str(e))
            correct_cin = match.group(1)
            fiscal_code = fiscal_code[:-1] + correct_cin
            # it does not raise exception
            raw_data = codicefiscale.decode(fiscal_code)
        else:
            fiscal_code = full_recompute_cf(
                name, surname, birth_country, birth_province,
                birth_comune, birthdate, gender
            )
            raw_data = codicefiscale.decode(fiscal_code)

    # ------------------------------------------------------------------
    # STEP 2: Genere
    # ------------------------------------------------------------------
    d_gender = raw_data['gender'].lower()
    d_birthdate = raw_data['birthdate']

    if is_empty(gender):
        gender = d_gender
    elif gender != d_gender:
        cf_error_counts['gender'] += 1
        gender = compute_gender_by_name(d_gender, gender, name)

    # ------------------------------------------------------------------
    # STEP 3: Data di nascita
    # ------------------------------------------------------------------
    if birthdate != d_birthdate:
        # Data reale ma diversa dal CF: errore
        cf_error_counts['birthdate'] += 1
        logger.info(
            f"Data di nascita inconsistente: db={birthdate!r}, cf={d_birthdate!r} "
            f"({name!r} {surname!r})"
        )
    # Trust CF
    birthdate = d_birthdate

    # ------------------------------------------------------------------
    # STEP 4: Birthplace dal CF (fonte di verita')
    # ------------------------------------------------------------------
    birth_country_check, birth_province, birth_comune, birth_comune_code, birth_country_code = infer_birthplace_cf(
        raw_data)

    if pd.isna(birth_country_check):
        # fail
        logger.error(f"Impossibile calcolare il birthplace dal CF: {birth_country!r}")

    # ------------------------------------------------------------------
    # STEP 5: Verifica finale
    # ------------------------------------------------------------------
    computed_cf = _encode_cf(
        name, surname, birthdate, gender,
        birth_country, birth_province, birth_comune
    )

    cf_dist = Levenshtein.normalized_distance(computed_cf, fiscal_code)
    if cf_dist > 0.2:
        try:
            computed_cf_inv = _encode_cf(
                surname, name, birthdate, gender,  # <- invertiti
                birth_country, birth_province, birth_comune
            )
            cf_dist_inv = Levenshtein.normalized_distance(computed_cf_inv, fiscal_code)
            if cf_dist_inv <= 0.2:
                logger.info(f"[INFO] Nome/cognome invertiti corretti: {name!r} {surname!r}")
                name, surname = surname, name
                computed_cf = computed_cf_inv
                cf_dist = cf_dist_inv
            else:
                raise ValueError(
                    f"CF calcolato diverge troppo dal CF in DB: "
                    f"computed={computed_cf!r}, db={fiscal_code!r}, dist={cf_dist:.2f} "
                    f"({name!r} {surname!r})"
                )
        except ValueError:
            raise ValueError(
                f"CF calcolato diverge troppo dal CF in DB: "
                f"computed={computed_cf!r}, db={fiscal_code!r}, dist={cf_dist:.2f} "
                f"({name!r} {surname!r})"
            )

    fiscal_code = computed_cf

    # ------------------------------------------------------------------
    # STEP 6: Aggiorna la riga
    # ------------------------------------------------------------------
    row = row.copy()
    row['first_name'] = name
    row['last_name'] = surname
    row['gender'] = gender.upper() if gender else pd.NA
    row['fiscal_code'] = fiscal_code
    row['birth_country'] = get_country_alpha_from_name(
        birth_country) if birth_country == "Italia" else get_country_alpha_from_name(birth_country_code)
    row['birth_province'] = birth_province
    row['birth_comune'] = birth_comune
    row['birth_comune_code'] = birth_comune_code
    row['birthdate'] = birthdate

    return row


# ---------------------------------------------------------------------------
# WRAPPER SICURO
# ---------------------------------------------------------------------------

def safe_check_fiscal_data(row: pd.Series) -> pd.Series:
    """
    Wrapper per df.apply — cattura ValueError e li mette in '_cf_error'.
    """
    try:
        result = check_fiscal_data(row)
        result['_cf_error'] = None
        return result
    except ValueError as e:
        row = row.copy()
        row['_cf_error'] = str(e)
        return row
