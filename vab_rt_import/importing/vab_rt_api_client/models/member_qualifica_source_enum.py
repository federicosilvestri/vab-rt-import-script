from enum import Enum


class MemberQualificaSourceEnum(str, Enum):
    CORSO_EXT = "CORSO_EXT"
    CORSO_INT = "CORSO_INT"
    MERITO = "MERITO"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
