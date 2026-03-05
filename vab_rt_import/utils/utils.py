import unicodedata
import pandas as pd
import re
from .nomi_italiani import load_names

# used for denormalization
_APOSTROPHE_MAP = {
    "a'": "à", "e'": "è", "i'": "ì", "o'": "ò", "u'": "ù",
    "A'": "À", "E'": "È", "I'": "Ì", "O'": "Ò", "U'": "Ù",
}


def data_quality_report(df: pd.DataFrame) -> pd.DataFrame:
    total = len(df)

    report = pd.DataFrame({
        'missing': df.isna().sum(),
        'missing_%': (df.isna().sum() / total * 100).round(2),
        'empty_str': df.apply(lambda c: (c == '').sum()),
        'unique': df.nunique(),
        'dtype': df.dtypes,
    })

    report['present'] = total - report['missing']
    report['present_%'] = (100 - report['missing_%']).round(2)

    return report.sort_values('missing_%', ascending=False)


def is_empty(val) -> bool:
    if val is None:
        return True
    if isinstance(val, str):
        return val.strip() == ''
    if isinstance(val, float):
        import math
        return math.isnan(val)
    try:
        return pd.isna(val)
    except (TypeError, ValueError):
        return False


def normalize_txt(text):
    text = str(text).lower()
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    text = text.encode('utf-8', errors='ignore').decode('utf-8')
    return text


_INVALID_NAMES = [
    'test',
    'prova',
    'paperopoli',
    'xxx',
    'covid',
    'operatore',
]


def clean_name(name):
    if name is None or (isinstance(name, float) and pd.isna(name)):
        return pd.NA

    name = normalize_txt(name)
    name = name.strip()
    name = re.sub(r"\s+", " ", name)
    name = re.sub(r"[^A-Za-zÀ-ÖØ-öø-ÿ']", "", name)
    name = name.lower()

    def smart_cap(word):
        if "'" in word:
            return "'".join(w.capitalize() for w in word.split("'"))
        if "-" in word:
            return "-".join(w.capitalize() for w in word.split("-"))
        return word.capitalize()

    name = " ".join(smart_cap(w) for w in name.split())
    name = name if len(name) > 1 else pd.NA

    if not pd.isna(name):
        for x in _INVALID_NAMES:
            if x.lower() in name.lower():
                # no.
                return pd.NA

    return name


def clean_date(date):
    if not date or pd.isna(date):
        return pd.NaT
    return pd.to_datetime(date, errors='coerce', format="%d/%m/%Y")


def clean_cf(cf):
    if is_empty(cf):
        return pd.NA
    r = str(cf).strip().upper()
    if len(r) not in (15, 16):
        return pd.NA
    return r


class NameDenormalizer(object):
    """This class help with name denormalization. (from niccolo' to niccolò)"""

    def __init__(self):
        name_list = load_names()
        self._normalized_index = {self._strip_accents(k): k for k in name_list}

    def denormalize(self, name: str) -> str:
        normalized = self._strip_accents(name)
        normalized = self._remove_apostrophe(normalized)

        if normalized in self._normalized_index:
            return self._normalized_index[normalized]
        return normalized.title()

    @staticmethod
    def _strip_accents(s: str) -> str:
        return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
        ).lower().strip()

    @staticmethod
    def _remove_apostrophe(s: str) -> str:
        return s.replace("'", "")
