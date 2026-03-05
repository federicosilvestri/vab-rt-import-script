from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tipo_unita_enum import TipoUnitaEnum

T = TypeVar("T", bound="Provincia")


@_attrs_define
class Provincia:
    """
    Attributes:
        id (int):
        code (str): Sigla provincia a 2 caratteri
        regione (int):
        tipo_unita (TipoUnitaEnum): * `1` - Provincia
            * `2` - Provincia autonoma
            * `3` - Città Metropolitana
            * `4` - Libero consorzio di Comuni
            * `5` - Unità non amministrativa
        denomination (str):
    """

    id: int
    code: str
    regione: int
    tipo_unita: TipoUnitaEnum
    denomination: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        code = self.code

        regione = self.regione

        tipo_unita = self.tipo_unita.value

        denomination = self.denomination

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "code": code,
                "regione": regione,
                "tipo_unita": tipo_unita,
                "denomination": denomination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        code = d.pop("code")

        regione = d.pop("regione")

        tipo_unita = TipoUnitaEnum(d.pop("tipo_unita"))

        denomination = d.pop("denomination")

        provincia = cls(
            id=id,
            code=code,
            regione=regione,
            tipo_unita=tipo_unita,
            denomination=denomination,
        )

        provincia.additional_properties = d
        return provincia

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
