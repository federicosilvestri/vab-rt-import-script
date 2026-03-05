from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Abilitazione")


@_attrs_define
class Abilitazione:
    """Read-only lookup serializer for Abilitazione.

    Attributes:
        id (int):
        title (str):
        description (str):
        has_expiration (bool): Se falso, l'abilitazione non scade mai
    """

    id: int
    title: str
    description: str
    has_expiration: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        has_expiration = self.has_expiration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "description": description,
                "has_expiration": has_expiration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        description = d.pop("description")

        has_expiration = d.pop("has_expiration")

        abilitazione = cls(
            id=id,
            title=title,
            description=description,
            has_expiration=has_expiration,
        )

        abilitazione.additional_properties = d
        return abilitazione

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
