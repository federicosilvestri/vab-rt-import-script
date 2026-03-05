"""Here we want to extract and build fiscal data."""
import pandas as pd
from vab_rt_import.utils.places_infer import build_place_inference
from vab_rt_import.utils.fiscal_clean import safe_check_fiscal_data, cf_error_counts
from vab_rt_import.utils import utils as utils
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

REPORT_FILE = Path(__file__).parent / 'data' / 'fiscal_not_recoverable_report.csv'

FINAL_COLUMNS = [
    'id',
    'first_name',
    'last_name',
    'gender',
    'birthdate',
    'birth_country',
    'birth_province',
    'birth_comune',
    'birth_comune_code',
    'fiscal_code',
]


def process_names(df: pd.DataFrame) -> pd.DataFrame:
    df['first_name'] = df['nome_socio'].apply(utils.clean_name)
    df['last_name'] = df['cognome_socio'].apply(utils.clean_name)
    df.drop(columns=['nome_socio', 'cognome_socio'], inplace=True)
    return df


def clean_junk(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['first_name', 'last_name'])
    return df


def resolve_gender(row, p_g_id, threshold=0.82):
    if pd.notna(row['sesso_socio']) and row['sesso_socio'] in ['m', 'f']:
        return row['sesso_socio']

    _id = row['id_sesso_socio']
    p_m = p_g_id.get('m', {}).get(_id, 0)
    p_f = p_g_id.get('f', {}).get(_id, 0)
    total = p_m + p_f
    if total == 0:
        return pd.NA

    p_m /= total
    p_f /= total
    if p_m >= threshold:
        return 'M'
    elif p_f >= threshold:
        return 'F'
    else:
        return pd.NA


def clean_gender(df: pd.DataFrame) -> pd.DataFrame:
    def initial_clean(gender):
        if pd.isna(gender) or not str(gender).strip():
            return pd.NA
        gender = str(gender).strip().lower()[0]
        return gender if gender in ('m', 'f') else pd.NA

    df['sesso_socio'] = df['sesso_socio'].apply(initial_clean)

    counts = df.groupby(['id_sesso_socio', 'sesso_socio']).size().unstack(fill_value=0)
    prob = counts.div(counts.sum(axis=1), axis=0)
    p_g_id = {g: prob[g].to_dict() for g in prob.columns}
    df['gender'] = df[['sesso_socio', 'id_sesso_socio']].apply(
        lambda g: resolve_gender(g, p_g_id), axis=1)
    df.drop(columns=['sesso_socio', 'id_sesso_socio'], inplace=True)
    return df


def clean_birthdate(df: pd.DataFrame) -> pd.DataFrame:
    df['birthdate'] = df['nato_il'].apply(utils.clean_date)
    df.drop(columns=['nato_il'], inplace=True)
    return df


def clean_cf(df: pd.DataFrame) -> pd.DataFrame:
    df['cod_fisc'] = df['cod_fisc'].apply(utils.clean_cf)
    # remove fiscal code
    df['fiscal_code'] = df['cod_fisc']
    df.drop(columns=['cod_fisc'], inplace=True)
    return df


def clean_birthplace(df: pd.DataFrame) -> pd.DataFrame:
    _worker = build_place_inference(col_name='nato_a', prefix='birth')
    df = df.apply(_worker, axis=1)
    df.drop(columns=['nato_a'], inplace=True)
    return df


def fiscal_clean(df: pd.DataFrame) -> pd.DataFrame:
    result = df.apply(safe_check_fiscal_data, axis=1)
    df_clean = result[result['_cf_error'].isna()].drop(columns=['_cf_error'])
    df_errors = result[result['_cf_error'].notna()]

    logger.info(f"OK:           {len(df_clean)}")
    logger.info(f"Con errori:   {len(df_errors)}")
    logger.info(f"\nContatori:\n{cf_error_counts}")

    # export
    logger.info("Saving into %s", REPORT_FILE.absolute())
    df_errors.to_csv(REPORT_FILE.absolute())
    return df_clean


def apply_name_normalization(df: pd.DataFrame) -> pd.DataFrame:
    name_den = utils.NameDenormalizer()
    df['first_name'] = df['first_name'].apply(name_den.denormalize)
    df['last_name'] = df['last_name'].apply(name_den.denormalize)

    return df


def process(df: pd.DataFrame) -> pd.DataFrame:
    df = process_names(df)
    df = clean_junk(df)
    df = clean_gender(df)
    df = clean_birthdate(df)
    df = clean_birthplace(df)
    df = clean_cf(df)
    df = fiscal_clean(df)
    # Apply name and surname normalization (a' -> to à)
    df = apply_name_normalization(df)

    return df[FINAL_COLUMNS]

