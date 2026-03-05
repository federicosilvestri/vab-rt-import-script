from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geographic_partition_enum import GeographicPartitionEnum

T = TypeVar("T", bound="Comune")


@_attrs_define
class Comune:
    """Serializer for Comune objects

    Attributes:
        id (int):
        code (str): Codice comune alfanumerico, gestito da ISTAT
        provincia (int):
        catasto_code (str): Codice catastale alfanumerico, gestito dall'Agenzia delle Entrate
        denomination (str):
        geographic_partition (GeographicPartitionEnum): * `1` - Nord
            * `2` - Nord-Est
            * `3` - Est
            * `4` - Sud-Est
            * `5` - Sud
            * `6` - Sud-Ovest
            * `7` - Ovest
            * `8` - Nord-Ovest
            * `9` - Centro
            * `10` - Isole
    """

    id: int
    code: str
    provincia: int
    catasto_code: str
    denomination: str
    geographic_partition: GeographicPartitionEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        code = self.code

        provincia = self.provincia

        catasto_code = self.catasto_code

        denomination = self.denomination

        geographic_partition = self.geographic_partition.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "code": code,
                "provincia": provincia,
                "catasto_code": catasto_code,
                "denomination": denomination,
                "geographic_partition": geographic_partition,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        code = d.pop("code")

        provincia = d.pop("provincia")

        catasto_code = d.pop("catasto_code")

        denomination = d.pop("denomination")

        geographic_partition = GeographicPartitionEnum(d.pop("geographic_partition"))

        comune = cls(
            id=id,
            code=code,
            provincia=provincia,
            catasto_code=catasto_code,
            denomination=denomination,
            geographic_partition=geographic_partition,
        )

        comune.additional_properties = d
        return comune

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
