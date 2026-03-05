from enum import Enum


class MemberAbilitazioneSourceEnum(str, Enum):
    ALTRO = "ALTRO"
    CORSO_EXT = "CORSO_EXT"
    CORSO_INT = "CORSO_INT"
    TITOLO = "TITOLO"

    def __str__(self) -> str:
        return str(self.value)
