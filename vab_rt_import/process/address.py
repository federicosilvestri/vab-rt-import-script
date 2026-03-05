import re

import pandas as pd

from vab_rt_import.utils.utils import normalize_txt
from vab_rt_import.utils.places_infer import build_place_inference


_FINAL_COLUMNS = [
    'address_country',
    'address_province',
    'address_comune',
    'address_cap',
    'address_street',
    'address_civico',
    'address_phone_home',
    'address_phone_mobile',
    'address_phone_other',
]


def clean_field(value):
    value = normalize_txt(value)
    if len(value) < 2:
        return pd.NA
    return value

def clean_cap(value):
    value = normalize_txt(value)
    if len(value) < 5:
        return pd.NA
    if re.match(r"^[0-5]{5}$", value):
        return value
    return pd.NA

def clean_phone(value):
    value = normalize_txt(value)
    if len(value) < 3:
        return pd.NA
    cleaned = re.sub(r'[^0-9+]', '', str(value).strip())
    return cleaned if cleaned else pd.NA

def clean_email(value):
    if pd.isna(value):
        return pd.NA
    value = str(value).strip().lower()
    match = re.search(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}', value)
    return match.group(0) if match else pd.NA

def process(df: pd.DataFrame) -> pd.DataFrame:
    df['residente_a'] = df['residente_a'].apply(clean_field)
    df['provincia'] = df['provincia'].apply(clean_field)
    df['address_query'] = df[['residente_a', 'provincia']].apply(
        lambda x: "{} ({})".format(x['residente_a'], x['provincia']), axis=1)

    _worker = build_place_inference('address_query', 'address')
    df = df.apply(_worker, axis=1)

    df['address_street'] = df['via'].apply(clean_field)
    df['address_cap'] = df['cap'].apply(clean_field)
    df['address_civico'] = df['num_civico'].apply(clean_field)

    df['address_phone_home'] = df['tel_abit'].apply(clean_phone)
    df['address_phone_mobile'] = df['tel_cellulare'].apply(clean_phone)
    df['address_phone_other'] = df['tel_altro'].apply(clean_phone)

    df['address_email'] = df['email'].apply(clean_email)

    df.drop(
        columns=['via', 'residente_a', 'provincia', 'cap', 'tel_abit', 'tel_cellulare', 'tel_altro', 'address_query'],
        inplace=True
    )
    return df[_FINAL_COLUMNS]

if __name__ == '__main__':
    from vab_rt_import.source import get_data

    df = get_data()
    process(df)
