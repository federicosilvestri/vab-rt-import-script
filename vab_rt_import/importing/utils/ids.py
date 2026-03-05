import json
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent / "datamap"
if not _DATA_DIR.exists():
    _DATA_DIR.mkdir()


def _map_file(key) -> Path:
    return _DATA_DIR / f"{key}_id_mapping.json"


def load_id_mapping(key, key_type=int) -> dict:
    path = _map_file(key)
    if path.exists():
        with open(path) as f:
            return {key_type(k): v for k, v in json.load(f).items()}
    return {}


def save_id_mapping(key, mapping: dict):
    file = _map_file(key)
    with open(file, "w") as f:
        json.dump(mapping, f, indent=2)
