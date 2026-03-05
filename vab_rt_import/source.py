import pandas as pd
from sqlalchemy import create_engine
import vab_rt_import.settings as settings

DEFAULT_QUERY = "SELECT * FROM {};".format(settings.SRC_SOCI_DB_TABLE)


def _build_uri() -> str:
    return "mariadb+pymysql://{}:{}@{}:{}/{}".format(
        settings.SRC_DB_USER,
        settings.SRC_DB_PASSWORD,
        settings.SRC_DB_HOST,
        settings.SRC_DB_PORT,
        settings.SRC_DB_NAME,
    )


def get_data(query: str = DEFAULT_QUERY) -> pd.DataFrame:
    sql_engine = create_engine(_build_uri(), echo=False)
    conn = sql_engine.connect()
    df = pd.read_sql(query, conn)
    conn.close()
    return df
