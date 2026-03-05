import time

import geonamescache
from comuniitaliani.exceptions import ComuneNotFoundError
from geopy.exc import GeocoderRateLimited, GeocoderNotFound
from pandas._libs.missing import NAType
import pycountry
import gettext
from rapidfuzz import process, fuzz
from gettext import gettext as _

from vab_rt_import.utils import utils
import pandas as pd
import re
from comuniitaliani import Comuni
import logging
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

logger = logging.getLogger(__name__)

# Translation set up
_italian = gettext.translation('iso3166-1', pycountry.LOCALES_DIR, languages=['it'])
_ = _italian.gettext

# DB comuni
_db = Comuni()

# Junk pattern
_JUNK_PATTERN = re.compile(
    r'^(x+|a+|d+|n+|prova|test|caserma|paperopoli|[a-z]{1,2}|'
    r'[^a-zA-Z\s]{0,3}|\d+|[a-z]{4,}\d.*)$',
    re.IGNORECASE
)

# Matching all items inside parenthesis
_PARENTHESIS_PATTERN = re.compile(r"\(([A-Za-z\s]+)\)")

# Title of province or country without # for findall
_SINGLE_TITLE_PATTERN = re.compile(r'(?<!\S)([A-Za-z]{2})(?!\S)')

it_to_en = {}
for _country in pycountry.countries:
    italian_name = _(_country.name).lower()
    it_to_en[italian_name] = _country.name

_gc = geonamescache.GeonamesCache()
_cities = _gc.get_cities()
_city_names = {utils.normalize_txt(v['name']): v for v in _cities.values()}

_geolocator = Nominatim(
    user_agent="vab-rt@fsilvestri.me"
)
_geolocator = RateLimiter(_geolocator.geocode, min_delay_seconds=1, error_wait_seconds=5)


# Internal class
class _GeoObject(object):

    def __init__(self, country: str | NAType = pd.NA, province: str | NAType = pd.NA, comune: str | NAType = pd.NA):
        self._country = country
        self._province = province
        self._comune = comune

    @property
    def country(self) -> str:
        return self._country

    @property
    def province(self) -> str:
        return self._province

    @property
    def comune(self) -> str:
        return self._comune

    @country.setter
    def country(self, country: str | NAType):
        if pd.isna(self._country):
            self._country = country

    @province.setter
    def province(self, province: str | NAType):
        if pd.isna(self._province):
            self._province = province

    @comune.setter
    def comune(self, comune: str | NAType):
        if pd.isna(self._comune):
            self._comune = comune

    def is_foreign(self):
        return not pd.isna(self._country) and self._country != 'IT'

    def is_complete(self):
        if self.is_foreign():
            return True
        return all(not pd.isna(x) for x in [self._country, self._province, self._comune])

    def to_tuple(self):
        return (self.country, self.province, self.comune)

    def __str__(self) -> str:
        return f"{self._country}, {str(self._province)}, {self._comune}"


def _clean_query(query: str) -> str:
    query = utils.normalize_txt(query)
    query = re.sub(r'[^A-Za-z\s()]', '', query)
    query = re.sub(r'\b[A-Za-z]\b', '', query)
    query = re.sub(r'\s+', ' ', query).strip()
    return query


def is_province_code(code: str) -> bool:
    return code.upper() in _db._by_name.keys()


def get_province_by_code(query: str) -> str | None:
    if utils.is_empty(query):
        return None
    if not (1 <= len(query) <= 2):
        msg = "Province code must be between 1 and 2 characters"
        raise ValueError(msg)
    try:
        comune_data = _db.comuni_per_provincia(query)
        if comune_data and 'provincia' in comune_data[0]:
            return comune_data[0]['provincia']
    except ComuneNotFoundError:
        pass
    return None


def get_province_code_by_name(name: str) -> str | None:
    if utils.is_empty(name):
        return None
    try:
        result = _db.cerca_comune(name)
        return result['sigla_provincia'] if result else None
    except ComuneNotFoundError:
        return None


def get_province_by_name_or_code(query: str) -> str | None:
    if utils.is_empty(query):
        return None

    result = process.extractOne(query.lower(), _db._by_name.keys(), scorer=fuzz.WRatio, score_cutoff=80)
    if result:
        return _db._by_name[result[0]][0]['provincia']


def get_country_by_code(query: str) -> str | None:
    data = pycountry.countries.get(
        alpha_2=query.upper()
    )
    if not data:
        return None
    return _(data.name)


def get_country_by_name(query: str) -> str | None:
    query = query.lower().strip()

    if query in it_to_en:
        return it_to_en[query]

    results = process.extractOne(query, it_to_en.keys(), scorer=fuzz.WRatio, score_cutoff=80)
    if results:
        return it_to_en[results[0]]

    try:
        results = pycountry.countries.search_fuzzy(query)
        return _(results[0].name) if results else None
    except LookupError:
        return None


def get_country_alpha_from_name(country: str) -> str | NAType:
    if utils.is_empty(country):
        return pd.NA

    try:
        data = pycountry.countries.search_fuzzy(country)
    except LookupError:
        return pd.NA

    if len(data) == 0:
        return pd.NA

    return data[0].alpha_2


### ------------- Search Functions ------------- ###

def _find_foreign_city_nominatim(query: str, result: _GeoObject, max_retry: int = 10) -> str:
    current_try = 0
    while current_try < max_retry:
        current_try += 1
        try:
            location = _geolocator(
                query,
                language='it',
                addressdetails=True,
                limit=1,
                timeout=10
            )
            if not location:
                return query

            address = location.raw.get('address', {})
            country_code = address.get('country_code', '').upper()

            result['countrycode'] = country_code
            return ""

        except GeocoderRateLimited as ex:
            logger.error("Geocoder rate limit exceeded, %s", ex)
            time_to_sleep = (2 ** current_try) * 1.5
            logger.error("Attempt %d/%d, sleeping for %d seconds", current_try, max_retry, time_to_sleep)
            time.sleep(time_to_sleep)
        except GeocoderNotFound as e:
            logger.error("Geocoding error for query=\"%s\": %s", query, e)
            return query

    return query


def _find_foreign_city(query: str, result: _GeoObject) -> str:
    """"TODOOOOOOOOOOO"""
    query = query.strip().lower()

    if query in _city_names:
        data = _city_names[query]
        result.country = data['countrycode']
        return ""

    data = process.extractOne(query, _city_names.keys(), scorer=fuzz.WRatio, score_cutoff=80)
    if data:
        data = _city_names[data[0]]
        result.country = data['countrycode']
        return ""

    words = query.split()
    for i in range(len(words), 0, -1):
        substring = ' '.join(words[:i])
        data = process.extractOne(substring, _city_names.keys(), scorer=fuzz.WRatio, score_cutoff=80)
        if data:
            data = data[data[0]]
            result.country = data['countrycode']
            return ""

    return ""


def _find_comune_by_name(query: str, result: _GeoObject) -> str:
    query = query.lower().strip()

    results = []
    if not pd.isna(result.province):
        # province is available,
        # we can reduce the index to the only comune inside province.
        _local_res = _db.comuni_per_provincia(result.province)
        if _local_res:
            # provincie may be wrong, search index
            lookup_index = set(x['nome'] for x in _local_res)
            # Try to search...
            results = process.extractOne(query, lookup_index, scorer=fuzz.WRatio, score_cutoff=90)
        else:
            logger.warning("No province found with title %s, searching inside all comuni index.",
                           result.province)
    if not results:
        # The whale comune index. mandatory...
        results = process.extractOne(query, _db._by_name.keys(), scorer=fuzz.WRatio, score_cutoff=90)

    if results:
        # it can not fail
        comune_data = _db.cerca_comune(results[0])
        result.country = 'IT'
        result.province = comune_data['provincia']
        result.comune = comune_data['nome']
        # query consumed
        return ""

    return query


def _re_analyze(regex, query: str, result: _GeoObject) -> str:
    """
    Analyzes the query against the given regex pattern.
    Extracts geographic info (country, province) and stores it in `result`.
    Removes matched portions from the query.
    :param regex: compiled regex pattern
    :param query: the query to be analyzed
    :param result: _GeoObject to be updated in place
    :return: the query with matched portions removed
    """
    matches = list(regex.finditer(query))
    if not matches:
        return query

    consumed_query = query
    offset = 0
    for m in matches:
        piece = m.group(1)
        start = m.start() - offset
        end = m.end() - offset
        consumed_query = (consumed_query[:start] + consumed_query[end:]).strip()
        offset += m.end() - m.start()
        logger.info(f"PIECE={piece}, query={consumed_query}")
        logger.info(f"PIECE={piece}, query={consumed_query}")

        is_code = len(piece) == 2
        if is_code and is_province_code(piece) is not None:
            result.country = 'IT'
            result.province = piece.upper()
        elif is_code and (c := get_country_by_code(piece)) is not None:
            result.country = c
        elif (p := get_province_code_by_name(piece)) is not None:
            result.country = 'IT'
            result.province = p
        elif (c := get_country_by_name(piece)) is not None:
            result.country = c
        else:
            logger.info(f"PAR FAIL:\tLEN={len(piece)}, piece={piece}")

    return consumed_query


def _analyze_comune(query) -> tuple[str, str | NAType, str | NAType]:
    return query, pd.NA, pd.NA


def _apply_result(c_query, c_country, c_province, c_comune, r_query, r_country, r_province, r_comune):
    return r_query, r_country, r_province, r_comune


def infer_place(query: str) -> tuple[NAType, NAType, NAType] | tuple[str, str, str]:
    _NULL = pd.NA, pd.NA, pd.NA

    if utils.is_empty(query):
        # null value
        return _NULL

    # normalize
    query = _clean_query(query)

    # junk check
    if len(query) < 2 or _JUNK_PATTERN.match(query):
        # trash
        return _NULL

    # Init data
    original_query = query
    result = _GeoObject()

    # check if province is available in ()
    if _PARENTHESIS_PATTERN.search(query):
        query = _re_analyze(_PARENTHESIS_PATTERN, query, result)

    # check if there are portions of text It, fi, IT
    single_portions = _SINGLE_TITLE_PATTERN.search(query)
    if single_portions:
        query = _re_analyze(_SINGLE_TITLE_PATTERN, query, result)

    if result.is_foreign():
        # If country is set, we can return
        return result.to_tuple()

    # try to identify each part of portion of the text
    resolvers = [
        # Priority 1: comune or italian place
        _find_comune_by_name,

        # Priority 2: country
        _find_foreign_city,

        # Priority 3: foreign city
        _find_foreign_city_nominatim,
    ]

    for resolver in resolvers:
        if not query:
            # Query is consumed. What's done is done.
            break
        query = resolver(query, result)

        if result.is_complete():
            break

    if not result.is_complete():
        logger.error("Failed to resolve query=\"%s\", original_query=\"%s\"", query, original_query)

    return result.to_tuple()


def build_place_inference(col_name: str, prefix: str):
    """
    Build the function to make inference.
    :param prefix: the prefix of columns
    :param col_name: the column names
    :return:
    """

    def _worker(row):
        country, province, comune = infer_place(row[col_name])
        row[f'{prefix}_country'] = country
        row[f'{prefix}_province'] = province
        row[f'{prefix}_comune'] = comune
        return row

    return _worker
