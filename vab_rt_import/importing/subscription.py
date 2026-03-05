"""Importing fiscal data"""
import pandas as pd
import logging

from pydantic import ValidationError
from vab_rt_import.importing.vab_rt_api_client import AuthenticatedClient
from vab_rt_import.importing.vab_rt_api_client.models import Subscription
from vab_rt_import.importing.vab_rt_api_client.api.subscriptions import \
    subscriptions_subscriptions_import_create
from vab_rt_import.importing.utils.ids import load_id_mapping

# logger
_logger = logging.getLogger(__name__)

# Chunk size
CHUNK_SIZE = 500

_id_mapping = load_id_mapping("members_member")

def build_sub(row: pd.Series):
    # resolve member id
    member_id = _id_mapping.get(row["id"], None)
    if member_id is None:
        msg = f"Member with local_id={row['id']} not found in remote members."
        raise ValueError(msg)


    # resolve referring member
    referring_member = _id_mapping.get(row['referring_member'], None)

    # build sub
    sub = Subscription(
        member=member_id,
        n_tessera=row["n_tessera"],
        is_active=row["active"],
        start_date=row["start_date"],
        end_date=None if pd.isna(row["end_date"]) else row["end_date"],
        volontario=row["volontario"],
        socio=row["socio"],
        referring_member=referring_member,
        member_since=0
    )
    return sub


def import_entity(data: pd.DataFrame, client: AuthenticatedClient) -> None:
    subs = []
    for idx, row in data.iterrows():
        try:
            result = build_sub(row)
        except ValidationError:
            _logger.warning(f'Skipping row {row["id"]} due to validation error')
            continue
        except ValueError:
            _logger.error(f'Skipping row {row["id"]} due to invalid lookup')
            continue

        subs.append(result)

    for i in range(0, len(subs), CHUNK_SIZE):
        batch_subs = subs[i:i + CHUNK_SIZE]

        _logger.info(f'Importing batch {i // CHUNK_SIZE + 1} ({len(batch_subs)} '
                     f'subscriptions)...')
        response = subscriptions_subscriptions_import_create.sync(client=client,
                                                                  body=batch_subs)

        if response.errors:
            _logger.warning(f'Batch errors: {response.errors}')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    import pandas as pd
    EXPORT_FILE = "../process/data/preprocessed_fiscal_data"

    df = pd.read_parquet(EXPORT_FILE + ".parquet")
    from vab_rt_import.importing.utils.auth import get_client
    client = get_client()
    import_entity(df, client)