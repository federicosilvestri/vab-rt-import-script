from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.member_driver_license_category import MemberDriverLicenseCategory


T = TypeVar("T", bound="PatchedMemberDriverLicenseDocument")


@_attrs_define
class PatchedMemberDriverLicenseDocument:
    """Serializer for MemberDriverLicenseDocument.

    - categories are nested and read-only on this serializer.
      Use the MemberDriverLicenseCategorySerializer endpoint to add/remove categories.
    - is_valid and is_complete are computed properties exposed as read-only.

        Attributes:
            id (int | Unset):
            member (int | Unset):
            number (str | Unset): Numero seriale del documento
            release_authority (str | Unset):
            release_date (datetime.date | Unset): Indicare la data di ultimo rilascio della patente
            expiration_date (datetime.date | Unset):
            document (str | Unset): Documento in PDF fronte retro a colori
            categories (list[MemberDriverLicenseCategory] | Unset):
            is_valid (bool | Unset):
            is_complete (bool | Unset):
    """

    id: int | Unset = UNSET
    member: int | Unset = UNSET
    number: str | Unset = UNSET
    release_authority: str | Unset = UNSET
    release_date: datetime.date | Unset = UNSET
    expiration_date: datetime.date | Unset = UNSET
    document: str | Unset = UNSET
    categories: list[MemberDriverLicenseCategory] | Unset = UNSET
    is_valid: bool | Unset = UNSET
    is_complete: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        number = self.number

        release_authority = self.release_authority

        release_date: str | Unset = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.strftime('%Y-%m-%d')

        expiration_date: str | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.strftime('%Y-%m-%d')

        document = self.document

        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        is_valid = self.is_valid

        is_complete = self.is_complete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if member is not UNSET:
            field_dict["member"] = member
        if number is not UNSET:
            field_dict["number"] = number
        if release_authority is not UNSET:
            field_dict["release_authority"] = release_authority
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if document is not UNSET:
            field_dict["document"] = document
        if categories is not UNSET:
            field_dict["categories"] = categories
        if is_valid is not UNSET:
            field_dict["is_valid"] = is_valid
        if is_complete is not UNSET:
            field_dict["is_complete"] = is_complete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.member_driver_license_category import MemberDriverLicenseCategory

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        member = d.pop("member", UNSET)

        number = d.pop("number", UNSET)

        release_authority = d.pop("release_authority", UNSET)

        _release_date = d.pop("release_date", UNSET)
        release_date: datetime.date | Unset
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        _expiration_date = d.pop("expiration_date", UNSET)
        expiration_date: datetime.date | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date).date()

        document = d.pop("document", UNSET)

        _categories = d.pop("categories", UNSET)
        categories: list[MemberDriverLicenseCategory] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = MemberDriverLicenseCategory.from_dict(categories_item_data)

                categories.append(categories_item)

        is_valid = d.pop("is_valid", UNSET)

        is_complete = d.pop("is_complete", UNSET)

        patched_member_driver_license_document = cls(
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

        patched_member_driver_license_document.additional_properties = d
        return patched_member_driver_license_document

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
