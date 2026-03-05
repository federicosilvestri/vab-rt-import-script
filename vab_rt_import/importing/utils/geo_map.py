import difflib
import json
import logging
from pathlib import Path

import pandas as pd

from vab_rt_import.importing.utils.auth import get_client
from vab_rt_import.importing.vab_rt_api_client import AuthenticatedClient
from vab_rt_import.importing.vab_rt_api_client.api.geo import geo_comune_list, geo_regione_list, geo_provincia_list

logger = logging.getLogger(__name__)

_DATA_FOLDER = Path(__file__).parent / 'geo_data'
_DATA_FOLDER.mkdir(parents=True, exist_ok=True)
_DATA_FILE = lambda name: _DATA_FOLDER / f"{name}_map.json"


def _create_geo_map(client: AuthenticatedClient, fun) -> dict:
    initial_data = fun.sync(client=client, page=1)
    total = initial_data.count
    page_size = len(initial_data.results)
    del initial_data
    total_pages = (total + page_size - 1) // page_size  # ceil division
    logger.info("Total of {} pages".format(total_pages))

    id_map = {}
    for page_i in range(1, total_pages + 1):  # +1 per includere l'ultima pagina
        response = fun.sync(client=client, page=page_i)
        if not response:
            continue
        for res in response.results:
            id_map[res.denomination] = res.id

    return id_map


def _create_comune_catasto_map(client: AuthenticatedClient) -> dict:
    file = _DATA_FILE('comune_catasto')
    if file.exists():
        return json.load(open(file))  # usa la variabile `file` già calcolata

    initial_data = geo_comune_list.sync(client=client, page=1)
    total = initial_data.count
    page_size = len(initial_data.results)
    del initial_data
    total_pages = (total + page_size - 1) // page_size
    logger.info("Total of {} pages".format(total_pages))

    id_map = {}
    for page_i in range(1, total_pages + 1):
        response = geo_comune_list.sync(client=client, page=page_i)
        if not response:
            continue
        for res in response.results:
            id_map[res.catasto_code] = res.id

    with open(file, 'w') as f:
        json.dump(id_map, f)

    return id_map


def _create_entity_map(client, entity_name, entity_fun) -> dict:
    file = _DATA_FILE(entity_name)
    if file.exists():
        return json.load(open(file))

    _map = _create_geo_map(client, entity_fun)
    json.dump(_map, open(file, 'w'))

    return _map


class GeoLookup(object):

    ENTITIES = ["regione", "provincia", "comune"]
    FUNS = [geo_regione_list, geo_provincia_list, geo_comune_list]

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GeoLookup, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return

        self._client = get_client()
        self._maps = {}

        for entity, fun in zip(self.ENTITIES, self.FUNS):
            self._maps[entity] = _create_entity_map(self._client, entity, fun)

        self._maps['comune_catasto'] = _create_comune_catasto_map(self._client)
        self._initialized = True

    def lookup_entity(self, entity: str, entity_query: str) -> int:
        if pd.isna(entity_query):
            raise ValueError("No entity query provided")

        volume = self._maps[entity]
        matches = difflib.get_close_matches(entity_query, volume.keys(), n=1, cutoff=0.6)
        if matches:
            return volume[matches[0]]

        raise ValueError(f"Cannot map {entity} query=\"{entity_query}\" to local identity")