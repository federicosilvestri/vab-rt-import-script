from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.member_driver_license_category import MemberDriverLicenseCategory


T = TypeVar("T", bound="MemberDriverLicenseDocument")


@_attrs_define
class MemberDriverLicenseDocument:
    """Serializer for MemberDriverLicenseDocument.

    - categories are nested and read-only on this serializer.
      Use the MemberDriverLicenseCategorySerializer endpoint to add/remove categories.
    - is_valid and is_complete are computed properties exposed as read-only.

        Attributes:
            id (int):
            member (int):
            number (str): Numero seriale del documento
            release_authority (str):
            release_date (datetime.date): Indicare la data di ultimo rilascio della patente
            expiration_date (datetime.date):
            document (str): Documento in PDF fronte retro a colori
            categories (list[MemberDriverLicenseCategory]):
            is_valid (bool):
            is_complete (bool):
    """

    id: int
    member: int
    number: str
    release_authority: str
    release_date: datetime.date
    expiration_date: datetime.date
    document: str
    categories: list[MemberDriverLicenseCategory]
    is_valid: bool
    is_complete: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        number = self.number

        release_authority = self.release_authority

        release_date = self.release_date.strftime('%Y-%m-%d')

        expiration_date = self.expiration_date.strftime('%Y-%m-%d')

        document = self.document

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        is_valid = self.is_valid

        is_complete = self.is_complete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member": member,
                "number": number,
                "release_authority": release_authority,
                "release_date": release_date,
                "expiration_date": expiration_date,
                "document": document,
                "categories": categories,
                "is_valid": is_valid,
                "is_complete": is_complete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.member_driver_license_category import MemberDriverLicenseCategory

        d = dict(src_dict)
        id = d.pop("id")

        member = d.pop("member")

        number = d.pop("number")

        release_authority = d.pop("release_authority")

        release_date = isoparse(d.pop("release_date")).date()

        expiration_date = isoparse(d.pop("expiration_date")).date()

        document = d.pop("document")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = MemberDriverLicenseCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        is_valid = d.pop("is_valid")

        is_complete = d.pop("is_complete")

        member_driver_license_document = cls(
            id=id,
            member=member,
            number=number,
            release_authority=release_authority,
            release_date=release_date,
            expiration_date=expiration_date,
            document=document,
            categories=categories,
            is_valid=is_valid,
            is_complete=is_complete,
        )

        member_driver_license_document.additional_properties = d
        return member_driver_license_document

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
