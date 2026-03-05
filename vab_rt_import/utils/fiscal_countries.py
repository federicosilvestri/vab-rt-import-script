"""Map used in fiscal clean to map Belfiore codes to Country"""
from pathlib import Path
import json

# DB File
DB_FILE = Path(__file__).parent / 'data' / 'fiscal_countries.json'




class FiscalCountries:
    """Mapper class to map fiscal country codes to Belfiore codes"""

    # Singleton instance
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return

        if not DB_FILE.exists():
            raise FileNotFoundError(f"Cannot load JSON. {DB_FILE}")

        with open(DB_FILE, 'r') as fp:
            data = json.load(fp)

        self._bel_to_country: dict[str, dict[str, str]] = dict()
        for d in data.values():
            key = d.get('italian_country_code') or d.get('taxcode_country_code')
            if not key:
                continue

            if key in self._bel_to_country:
                raise KeyError(f"Key {key} already exists")

            name = d.get('italian_country_name_1') or d.get('italian_country_name_2')
            if not name:
                raise KeyError(f"Cannot find name key for record {d}")

            alpha2 = d.get('iso3361_2_characters')
            if not alpha2:
                alpha2 = d.get('iso3361_3_characters')
            if not alpha2:
                raise KeyError(f"Cannot find alpha2 key for record {d}")

            self._bel_to_country[key] = {
                'name': name.title(),
                'alpha2': alpha2.upper()
            }

        self._initialized = True


    def get_name(self, code: str) -> str:
        return self._bel_to_country[code.strip().upper()]['name']


    def get_code(self, code: str) -> str:
        return self._bel_to_country[code.strip().upper()]['alpha2']

    def valid_country_code(self, code: str) -> bool:
        return code.upper() in self._bel_to_country.keys()