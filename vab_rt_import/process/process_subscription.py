"""Here we want to extract and build subscription data."""
import pandas as pd
from pandas._libs.missing import NAType
from vab_rt_import import utils as utils
from vab_rt_import.utils.n_tessera_filler import TesseraFiller
import logging

logger = logging.getLogger(__name__)

_FINAL_COLUMNS = [
    'id',
    'n_tessera',
    'new_n_tessera',
    'socio',
    'volontario',
    'active',
    'start_date',
    'start_date_effective',
    'end_date',
    'referring_member',
]

_FLAG_MAPS = {
    True: ["on", "1", "si"],
    False: ["off", "0", "no"]
}

_MAX_N_TESSERA_VALID = 21427
_MIN_N_TESSERA_VALID = 0


def _process_flag(value: str) -> bool | NAType:
    if utils.is_empty(value):
        # missing is False
        return False
    # we can simplify....
    value = utils.normalize_txt(value).lower().strip()
    if value in _FLAG_MAPS[True]:
        return True
    elif value in _FLAG_MAPS[False]:
        return False
    else:
        logger.error(f"Flag {value} not recognized")
        return pd.NA


def process_flags(df: pd.DataFrame) -> pd.DataFrame:
    df['socio'] = df['flag_socio'].map(_process_flag)
    df['volontario'] = df['flag_volontario'].map(_process_flag)
    return df.drop(columns=['flag_socio', 'flag_volontario'])


def _process_n_tessera(value: str) -> int | NAType:
    if utils.is_empty(value):
        return pd.NA
    try:
        x = int(value)
    except ValueError:
        logger.error(f"N_tessera {value} not recognized.")
        return pd.NA
    if x > _MAX_N_TESSERA_VALID:
        logger.error(f"N_tessera {value} too large.")
        return pd.NA
    if x < _MIN_N_TESSERA_VALID:
        logger.error(f"N_tessera {value} too small.")
        return pd.NA
    return x


def process_n_tessera(df: pd.DataFrame, col_in='num_tessera', col_out='n_tessera') -> (
        pd.DataFrame):
    df[col_out] = df[col_in].map(_process_n_tessera)
    df.dropna(subset=[col_out], inplace=True)
    return df.drop(columns=[col_in])


def _process_active(value: str) -> bool | NAType:
    if utils.is_empty(value):
        return pd.NA
    value = utils.normalize_txt(value).lower().strip()

    try:
        x = int(value)
    except ValueError:
        logger.error(f"Active {value} not recognized.")
        return pd.NA

    return x == 0  # inverted logic


def process_socio_inattivo(df: pd.DataFrame) -> pd.DataFrame:
    df['active'] = df['socio_inattivo'].map(_process_active)
    return df.drop(columns=['socio_inattivo'])


def process_start_end_date(df: pd.DataFrame) -> pd.DataFrame:
    df['end_date'] = df['data_disattivazione_socio'].map(utils.clean_date)
    df['start_date'] = df['data_iscriz'].map(utils.clean_date)
    df['start_date_effective'] = df['data_registr_libro_soci'].map(utils.clean_date)

    return df.drop(
        columns=['data_disattivazione_socio', 'data_iscriz', 'data_registr_libro_soci'])


def process_n_tessera_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    tc = TesseraFiller(df["n_tessera"].dropna())
    logger.info("Tessera filler available: %d", tc.get_available())
    df["new_n_tessera"] = False
    duplicates = df[df.duplicated("n_tessera", keep=False)]
    for num_tessera, group in duplicates.groupby("n_tessera"):
        # Priority 1: inactive member
        disabled = group[~group["active"]]
        if not disabled.empty:
            idx_to_keep = disabled.index[0]
        else:
            # Priority 2: older start_date
            idx_to_keep = group["start_date"].idxmin()

        others = group.index.difference([idx_to_keep])
        df.loc[others, "new_n_tessera"] = True
        # ogni riga chiama get_first_available separatamente, consumando un numero diverso
        for idx in others:
            df.loc[idx, "n_tessera"] = tc.get_first_available(num_tessera)

    logger.info("Tessera filler available: %d", tc.get_available())
    return df


def process_num_tessera_socio_presentatore(df: pd.DataFrame) -> pd.DataFrame:
    df = process_n_tessera(
        df,
        col_in='num_tessera_socio_presentatore',
        col_out='referring_member'
    )
    # resolve id
    tessera_to_id = df.set_index('n_tessera')['id'].to_dict()
    df['referring_member'] = df['referring_member'].map(tessera_to_id)
    df['referring_member'] = df['referring_member'].astype(pd.Int64Dtype())
    return df


def process_subscription(df: pd.DataFrame) -> pd.DataFrame:
    df = process_flags(df)
    df = process_n_tessera(df)
    df = process_socio_inattivo(df)
    df = process_start_end_date(df)
    df = process_n_tessera_duplicates(df)
    df = process_num_tessera_socio_presentatore(df)

    return df[_FINAL_COLUMNS]


if __name__ == '__main__':
    from vab_rt_import.source import get_data

    logging.basicConfig(level=logging.INFO)

    data = get_data()
    data = process_subscription(data)
    print(data)
