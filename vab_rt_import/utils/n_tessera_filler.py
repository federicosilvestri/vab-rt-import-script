"""Filler"""
import pandas as pd


class TesseraFiller(object):
    """Filler"""

    def __init__(self, n_series: pd.Series):
        self._missing = []
        self._execute(n_series.copy())

    def _execute(self, _n_series: pd.Series):
        n_series = _n_series.sort_values().reset_index(drop=True)

        missing = []
        for i in range(len(n_series) - 1):
            current, next_val = n_series[i], n_series[i + 1]
            if current + 1 != next_val:
                missing.extend(range(current + 1, next_val))

        self._missing = missing

    def get_first_available(self, n_tessera: int | None = None) -> int:
        """Returns first available tessera, similar to n_tessera"""
        if not self._missing:
            raise ValueError("No available tessera numbers")

        if n_tessera is None:
            selected = self._missing[0]
            self._missing.remove(selected)
            return selected

        if n_tessera in self._missing:
            self._missing.remove(n_tessera)
            return n_tessera

        diff = [abs(x - n_tessera) for x in self._missing]
        selected = self._missing[diff.index(min(diff))]
        self._missing.remove(selected)
        return selected

    def get_available(self) -> int:
        return len(self._missing)
