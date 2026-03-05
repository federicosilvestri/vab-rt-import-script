from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MemberList")


@_attrs_define
class MemberList:
    """Lightweight serializer for list endpoints.
    Avoids fetching nested rank/status objects for large querysets.

        Attributes:
            id (int):
            first_name (str): Nome indicato nella carta di identità. Eventuali secondi nomi devono essere indicati qui,
                separati da uno spazio.
            last_name (str): Cognome indicato nella carta di identità. Eventuali secondi cognomi devono essere indicati qui,
                separati da uno spazio.
            fiscal_code (str):
            socio (bool): Indica se la persona è un socio attivo.
            volontario (bool): Indica se la persona è un volontario attivo.
            operative (bool): Indica se la persona è operativa.
            rank_id (None | str):
            status_id (None | str):
    """

    id: int
    first_name: str
    last_name: str
    fiscal_code: str
    socio: bool
    volontario: bool
    operative: bool
    rank_id: None | str
    status_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        fiscal_code = self.fiscal_code

        socio = self.socio

        volontario = self.volontario

        operative = self.operative

        rank_id: None | str
        rank_id = self.rank_id

        status_id: None | str
        status_id = self.status_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "fiscal_code": fiscal_code,
                "socio": socio,
                "volontario": volontario,
                "operative": operative,
                "rank_id": rank_id,
                "status_id": status_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        fiscal_code = d.pop("fiscal_code")

        socio = d.pop("socio")

        volontario = d.pop("volontario")

        operative = d.pop("operative")

        def _parse_rank_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rank_id = _parse_rank_id(d.pop("rank_id"))

        def _parse_status_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status_id = _parse_status_id(d.pop("status_id"))

        member_list = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            fiscal_code=fiscal_code,
            socio=socio,
            volontario=volontario,
            operative=operative,
            rank_id=rank_id,
            status_id=status_id,
        )

        member_list.additional_properties = d
        return member_list

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
