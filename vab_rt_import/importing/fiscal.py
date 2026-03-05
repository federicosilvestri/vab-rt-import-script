"""Importing fiscal data"""
import pandas as pd
import logging

from pydantic import ValidationError

from vab_rt_import.importing.utils.geo_map import GeoLookup
from vab_rt_import.importing.vab_rt_api_client import AuthenticatedClient
from vab_rt_import.importing.vab_rt_api_client.models import Member, GenderEnum, BirthCountryEnum
from vab_rt_import.importing.vab_rt_api_client.api.members import members_member_import_create
from vab_rt_import.importing.utils.ids import save_id_mapping

_logger = logging.getLogger(__name__)

# Chunk size
CHUNK_SIZE = 500


def build_member(row: pd.Series, geo: GeoLookup) -> (Member, int):
    # Map comune
    try:
        birth_country = BirthCountryEnum(row['birth_country'])
        if birth_country != BirthCountryEnum.IT:
            comune = None
        else:
            comune = geo.lookup_entity('comune_catasto', row['birth_comune_code'])
    except ValueError as exc:
        logging.error("Skipping, due to %s", exc)
        return None

    try:
        member = Member(
            id=0,
            first_name=row['first_name'],
            last_name=row['last_name'],
            gender=GenderEnum.F if row['gender'] == 'F' else GenderEnum.M,
            birth_date=row['birthdate'],
            birth_country=birth_country,
            birth_comune=comune,
            fiscal_code=row['fiscal_code'],
            status=None,
            rank=None,
            operative=False,
            age=1,
            socio=False,
            volontario=False,
        )
        return member, row['id']
    except ValidationError as e:
        logging.error(e)


def import_entity(data: pd.DataFrame, client: AuthenticatedClient) -> None:
    geo = GeoLookup()
    # Local ID -> Remote ID
    id_map: dict[int, int] = {}
    # Map CF -> local ID
    cf_to_id = data.set_index('fiscal_code')['id'].to_dict()

    members = []
    local_ids = []
    for idx, row in data.iterrows():
        result = build_member(row, geo)
        if result is None:
            _logger.warning(f'Skipping row {row["id"]} due to validation error')
            continue
        member, local_id = result
        members.append(member)
        local_ids.append(local_id)

    for i in range(0, len(members), CHUNK_SIZE):
        batch_members = members[i:i + CHUNK_SIZE]

        _logger.info(
            f'Importing batch {i // CHUNK_SIZE + 1} ({len(batch_members)} members)...')
        response = members_member_import_create.sync(client=client, body=batch_members)

        if response.errors:
            _logger.warning(f'Batch errors: {response.errors}')

        for remote_cf, remote_id in response.map_.to_dict().items():
            id_map[cf_to_id.get(remote_cf)] = remote_id

    save_id_mapping('members_member', id_map)
