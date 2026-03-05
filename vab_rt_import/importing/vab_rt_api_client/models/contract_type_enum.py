from enum import Enum


class ContractTypeEnum(str, Enum):
    AUT = "AUT"
    COCO = "COCO"
    DIP = "DIP"
    OCC = "OCC"
    PIVA = "PIVA"
    TIR = "TIR"

    def __str__(self) -> str:
        return str(self.value)
