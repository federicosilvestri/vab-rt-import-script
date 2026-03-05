from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MemberDriverLicenseCategory")


@_attrs_define
class MemberDriverLicenseCategory:
    """Serializer for a single driver license category entry.

    Attributes:
        id (int):
        driver_licence (int):
        category (int):
        achievement_date (datetime.date): Data di conseguimento della categoria, riportato sul retro della patente.
    """

    id: int
    driver_licence: int
    category: int
    achievement_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        driver_licence = self.driver_licence

        category = self.category

        achievement_date = self.achievement_date.strftime('%Y-%m-%d')

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "driver_licence": driver_licence,
                "category": category,
                "achievement_date": achievement_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        driver_licence = d.pop("driver_licence")

        category = d.pop("category")

        achievement_date = isoparse(d.pop("achievement_date")).date()

        member_driver_license_category = cls(
            id=id,
            driver_licence=driver_licence,
            category=category,
            achievement_date=achievement_date,
        )

        member_driver_license_category.additional_properties = d
        return member_driver_license_category

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
