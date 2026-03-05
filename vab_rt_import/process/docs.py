import pandas as pd
import re
from vab_rt_import.utils.utils import is_empty, normalize_txt, clean_date
from rapidfuzz.distance import Levenshtein
from vab_rt_import.utils import places_infer as places
import logging

logger = logging.getLogger(__name__)

# Junk
_JUNK = re.compile(
    r'^(x+|0+|\*+|\+\+|aaa+|\d[\d\s]{4,}|[a-z]{1,2}|assente|hun|'
    r'rtjh\w+|av\d+|ti ch|moni\s\w+|ssn\s|usl\s|stato|scuola\s|'
    r'aci\s|legione\s)$'
)

_DATE_PATTERN = re.compile(r'^\d{1,2}\s\d{1,2}\s\d{4}$')

_remove_columns = [
    'patente_tipo',
    'patente_numero',
    'pat_rilasc_il',
    'pat_rilasc_da',
    'pat_scad',
    'tipo_doc_identita_socio',
    'numero_doc_identita_socio',
    'scadenza_doc_identita_socio',
    'doc_identita_socio_rilasc_da',
]

CI_TYPE_MAP = {
    'CDI': [
        'ci', 'ca', 'cdi', 'cie', 'cid',
        'cartaidentita', 'cartadidentita', 'cartadiidentita',
        'cartadidentit', 'cartaidientita', 'catradiidentita',
        'cartadidentit', 'cidentita', 'cidentia', 'cidentit',
        'cidendita', 'cielettronica', 'cartaid', 'cartaceo',
        'carta', 'documentoidentita', 'docidnazionale',
        'tesseradidentita', 'cui',
    ],
    'CNS': [
        'tesserasanitaria', 'cns', 'tessera', 'codicefiscale',
    ],
    'PATENTE': [
        'patente', 'patenteauto', 'patentediguida', 'patenteguida',
        'patauto', 'patguida', 'pat', 'patentenautica',
        'patenteeuropea', 'patenteab', 'patenteade', 'patenteabc',
        'patentede', 'patentea',
    ],
    'PASSAPORTO': [
        'passaporto', 'passaportobritannico', 'pass',
        'psoggiorno',
    ],
    'ALTRO': [
        'tesseraministeriale', 'tesseramininterno',
        'ministerodellintern', 'cartamultiservizi',
        'permessosoggiorno', 'permessodisoggiorno', 'permdisoggiorno',
        'permessodisoggiorn', 'psoggiorno', 'cartasoggiorno',
        'portodarmi'
    ],
}

# Prefissi che indicano Motorizzazione in tutte le sue varianti
_MOT_PREFIXES = (
    'Motorizzazione', 'motoriz', 'motorizz', 'mctc', 'mtct', 'mtcc',
    'mtc', 'mttc', 'mot', 'motor', 'mutc', 'mutct', 'mctct',
    'mituco', 'mit uco', 'mituc', 'uco', 'u c o', 'mim trasporti',
    'min tasporti', 'm d trasporti', 'miniaero', 'mot ne civile',
    'mot civ', 'motor civile', 'mtl', 'mc ', 'm c ', 'm t c',
)

# Prefissi Comune in tutte le varianti
_COM_PREFIXES = (
    'Comune di ', 'Comune ', 'com ', 'anagrafe ', 'municipio ',
    'sindaco di ', 'anag ', 'anagraf ', 'comcapraia',
    'coune ', 'conume ', 'cum ', 'camune ', 'cmune ', 'c di ',
    'co ', 'con ', 'c bagno', 'c san', 'c mon', 'c castel',
    'co bagno', 'co chiesina', 'c terranuova', 'acquapendente Comune',
)

# Prefissi PREFETTURA
_PREF_PREFIXES = (
    'prefettura', 'prefetto', 'pref ',
    'ministero interno', 'ministerointerno', 'min interno',
    'mininterno', 'minterni', 'min interni', 'm interno',
    'ministero dell interno', 'm d i', 'minist affari esteri',
    'mini affari esteri', 'min affari esteri',
    'repubblica italiana', 'repubblica italian',
    'stato',
)

# Prefissi Consolato / AMBASCIATA
_CONS_PREFIXES = (
    'ambasciata', 'Consolato', 'uff consol', 'governo ',
    'espana', 'bulgaria', 'albania', 'romania',
    'legione cc',
)

# Prefissi Motorizzazione CIVILE (MIT / Ministero Trasporti)
_MIT_PREFIXES = (
    'mit uco', 'mituco', 'uco', 'u c o',
    'mim trasporti', 'min tasporti', 'm d trasporti',
    'miniaero dei trasort', 'mot ne civile', 'motor civile',
    'mot civ',
)

_COLUMNS = [
    "id",
    'dl_release_authority',
    'dl_release_date',
    'dl_expiry_date',
    'dl_types',
    'dl_number',
    'id_type',
    'id_number',
    'id_expiry_date',
    'id_release_authority',
]


def _extract_sigla_provincia(text: str) -> str | None:
    """Estrae la sigla di provincia dalle ultime 2 lettere."""
    m = re.search(r'\b([a-z]{2})\b', text)
    if m:
        sigla = m.group(1)
        province = places.get_province_by_code(sigla)
        if not province:
            # fallback: ultime 2 lettere del testo
            province = places.get_province_by_code(text[-2:])
        return province
    return None


def _extract_nome_after_prefix(text: str, prefixes: tuple) -> str | None:
    """Rimuove il prefisso più lungo che matcha e ritorna il resto."""
    # Ordina dal più lungo al più corto per evitare match parziali
    for p in sorted(prefixes, key=len, reverse=True):
        if text.startswith(p):
            rest = text[len(p):].strip()
            return rest if rest else None
    return None


def _extract_nome_prefettura(text: str) -> str | None:
    """
    Estrae il nome della città dalla stringa prefettura.
    Gestisce: "prefettura firenze", "prefettura di siena",
              "prefettura (gr)", "prefettura av", "prefettura di av"
    """
    # Rimuovi il prefisso
    rest = re.sub(r'^(prefettura di |prefettura |pref di |pref )', '', text).strip()

    if not rest:
        return None

    # Caso "(GR)" o "(Gr)" -> estrai sigla
    m = re.match(r'^\(([a-z]{2})\)$', rest)
    if m:
        sigla = m.group(1)
        return places.get_province_by_code(sigla)

    # Caso sigla secca di 2 lettere -> lookup capoluogo
    if re.match(r'^[a-z]{2}$', rest):
        return places.get_province_by_code(rest)

    # Caso nome troncato tipo "catanz" -> fuzzy su capoluoghi
    return places.get_province_by_name_or_code(rest)


def _clean_doc_id_rilasciato_da(value) -> tuple:
    """
    Ritorna (categoria, nome_ente) dove:
    - categoria: Comune | PREFETTURA | Motorizzazione | Questura |
                 Consolato | ALTRO | pd.NA
    - nome_ente: stringa con il nome dell'ente se disponibile, else pd.NA
    """
    if is_empty(value):
        return pd.NA, pd.NA

    original = normalize_txt(str(value)).strip().lower()
    # Normalizza spazi e punteggiatura, mantieni spazi per prefix matching
    original = re.sub(r'[\'\.\-\_\/]+', ' ', original)
    original = re.sub(r'\s+', ' ', original).strip()

    if len(original) < 2:
        return pd.NA, pd.NA

    # Scarta spazzatura e date nel campo sbagliato
    if _JUNK.match(original) or _DATE_PATTERN.match(original):
        return pd.NA, pd.NA

    # Rimuovi date embedded in fondo (es. "mtct fi 15 04 2009")
    original = re.sub(r'\s+\d{1,2}\s+\d{1,2}\s+\d{4}$', '', original).strip()
    original = re.sub(r'\s+\d{8}$', '', original).strip()

    # -----------------------------------------------------------------------
    # Motorizzazione (prima perché "mc" è ambiguo con "Comune")
    # -----------------------------------------------------------------------
    if any(original.startswith(p) for p in _MIT_PREFIXES):
        sigla = _extract_sigla_provincia(original)
        nome = places.get_province_by_name_or_code(sigla)
        return 'Motorizzazione', nome or pd.NA

    if any(original.startswith(p) for p in _MOT_PREFIXES):
        # Cerca sigla o città dopo il prefisso
        rest = _extract_nome_after_prefix(original, _MOT_PREFIXES) or original
        sigla = _extract_sigla_provincia(rest)
        if sigla:
            nome = places.get_province_by_name_or_code(sigla)
        else:
            # Potrebbe esserci un nome città: "mot arezzo", "motorizz pistoia"
            nome = rest.title() if rest and len(rest) > 1 else pd.NA
        return 'Motorizzazione', nome if not pd.isna(nome) else pd.NA

    # -----------------------------------------------------------------------
    # Comune / ANAGRAFE
    # -----------------------------------------------------------------------
    if any(original.startswith(p) for p in _COM_PREFIXES):
        rest = _extract_nome_after_prefix(original, _COM_PREFIXES)
        nome = rest.title() if rest else pd.NA
        return 'Comune', nome

    # Nomi di Comune "nudi" (senza prefisso) — comuni noti o lookup fuzzy
    # Se è solo un nome e non matcha altro, trattiamo come Comune
    # (es. "lamporecchio", "quarrata", "pistoia", "firenze")

    # -----------------------------------------------------------------------
    # PREFETTURA / MINISTERO
    # -----------------------------------------------------------------------
    if any(original.startswith(p) for p in _PREF_PREFIXES):
        rest = _extract_nome_after_prefix(original, _PREF_PREFIXES)
        nome = _extract_nome_prefettura(original) if rest else pd.NA
        return 'Prefettura', nome

    # -----------------------------------------------------------------------
    # Questura
    # -----------------------------------------------------------------------
    if original.startswith('Questura') or original.startswith('polizia'):
        rest = re.sub(r'^(Questura di |Questura |polizia )', '', original).strip()
        nome = rest.title() if rest else pd.NA
        return 'Questura', nome

    # -----------------------------------------------------------------------
    # Consolato / AMBASCIATA / ESTERO
    # -----------------------------------------------------------------------
    if any(original.startswith(p) for p in _CONS_PREFIXES):
        rest = _extract_nome_after_prefix(original, _CONS_PREFIXES)
        nome = rest.title() if rest else pd.NA
        return 'Consolato', nome

    # -----------------------------------------------------------------------
    # FALLBACK: nome nudo senza prefisso
    # Probabilmente è un Comune scritto senza "Comune di"
    # -----------------------------------------------------------------------
    # Controlla che non sia un numero di documento o stringa alfanumerica
    if re.search(r'\d', original):
        return pd.NA, pd.NA

    # Se arriva qui è probabilmente un Comune nudo
    print(f"[rilasciato_da] assunto Comune (nudo): {original!r}")
    return 'Comune', original.title()


def clean_doc_id_rilasciato_da(value):
    cat, nome = _clean_doc_id_rilasciato_da(value)

    if pd.isna(cat) and pd.isna(nome):
        return pd.NA
    if pd.isna(nome):
        return cat.title()

    for k in ['Prefettura', 'Comune', 'Consolato', 'Motorizzazione']:
        if k in nome:
            return nome.title()

    return f"{cat.title()} {nome.title()}"


def remove_junk(value):
    if pd.isna(value):
        return pd.NA
    value = str(value).strip()
    if _JUNK.match(value):
        return pd.NA
    return value


def clean_tipo_doc_id(value):
    if is_empty(value):
        return pd.NA

    value = normalize_txt(str(value)).strip().lower()
    value = re.sub(r'[\s\'\.\-\_\/]+', '', value)

    if len(value) < 2 or _JUNK.match(value):
        return pd.NA

    for ctype, aliases in CI_TYPE_MAP.items():
        if value in aliases:
            return ctype

    if is_empty(value):
        return pd.NA

    prefix_map = {
        'pa': 'PATENTE',
        'pat': 'PATENTE',
        'pass': 'PASSAPORTO',
        'carta': 'CDI',
        'cid': 'CDI',
        'ci': 'CDI',
        'cod': 'CNS',
        'ca': 'CDI',
    }
    for prefix, ctype in prefix_map.items():
        if value.startswith(prefix):
            best_dist = min(
                Levenshtein.normalized_distance(value, alias)
                for alias in CI_TYPE_MAP[ctype]
            )
            if best_dist < 0.4:
                return ctype

    best_type, best_dist = None, 1.0
    for ctype, aliases in CI_TYPE_MAP.items():
        for alias in aliases:
            dist = Levenshtein.normalized_distance(value, alias)
            if dist < best_dist:
                best_dist = dist
                best_type = ctype

    if best_dist < 0.25:
        return best_type

    logger.info(f"[tipo_doc] non riconosciuto: {value!r} (best={best_type!r}, dist={best_dist:.2f})")
    return pd.NA


def normalize_tipo_patente(value):
    if is_empty(value):
        return pd.NA
    value = str(value).strip().upper()
    value = re.sub(r'[\s\-\/,;.]+', '', value)

    found = set()
    i = 0
    while i < len(value):
        matched = False
        for token in ['C1E', 'D1E', 'AM', 'A1', 'A2', 'BE', 'B1', 'C1', 'CE', 'D1', 'DE', 'A', 'B', 'C', 'D', 'T']:
            if value[i:].startswith(token):
                found.add(token)
                i += len(token)
                matched = True
                break
        if not matched:
            i += 1
    if not found:
        return pd.NA
    return '-'.join(sorted(found))


def clean_patente_number(value):
    if is_empty(value):
        return pd.NA

    value = str(value).strip().upper()
    value = re.sub(r"\s?", "", value)

    if len(value) != 10:
        return pd.NA

    return value


def clean_doc_rele_by(value):
    value = remove_junk(value)
    if is_empty(value):
        return pd.NA
    return value.upper()


def process(df: pd.DataFrame):
    df['dl_release_authority'] = df['pat_rilasc_da'].apply(clean_doc_id_rilasciato_da)
    df['dl_release_date'] = df['pat_rilasc_il'].apply(clean_date)
    df['dl_expiry_date'] = df['pat_scad'].apply(clean_date)
    df['dl_types'] = df['patente_tipo'].apply(normalize_tipo_patente)
    df['dl_number'] = df['patente_numero'].apply(clean_patente_number)

    df['id_type'] = df['tipo_doc_identita_socio'].apply(clean_tipo_doc_id)
    df['id_number'] = df['numero_doc_identita_socio'].apply(clean_doc_rele_by)
    df['id_expiry_date'] = df['scadenza_doc_identita_socio'].apply(clean_date)
    df['id_release_authority'] = df['doc_identita_socio_rilasc_da'].apply(clean_doc_id_rilasciato_da)

    df.drop(columns=_remove_columns, inplace=True)
    return df[_COLUMNS]
