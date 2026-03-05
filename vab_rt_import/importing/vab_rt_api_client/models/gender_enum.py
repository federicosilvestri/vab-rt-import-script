from enum import Enum


class GenderEnum(str, Enum):
    F = "F"
    M = "M"

    def __str__(self) -> str:
        return str(self.value)
