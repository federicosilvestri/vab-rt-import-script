from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedMemberCIEDocument")


@_attrs_define
class PatchedMemberCIEDocument:
    """Serializer for MemberCIEDocument (Carta di Identità Elettronica).

    - is_valid is a computed property exposed as read-only.
    - document is a PDF file upload field.

        Attributes:
            id (int | Unset):
            member (int | Unset):
            number (str | Unset): Numero del documento, raffigurato in altro a destra nella parte frontale.
            release_date (datetime.date | Unset):
            release_authority (str | Unset): Indicare l'autorità che ha rilasciato il documento.
            expiration_date (datetime.date | Unset):
            document (str | Unset): Documento in PDF fronte retro a colori
            is_valid (bool | Unset):
    """

    id: int | Unset = UNSET
    member: int | Unset = UNSET
    number: str | Unset = UNSET
    release_date: datetime.date | Unset = UNSET
    release_authority: str | Unset = UNSET
    expiration_date: datetime.date | Unset = UNSET
    document: str | Unset = UNSET
    is_valid: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        number = self.number

        release_date: str | Unset = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.strftime('%Y-%m-%d')

        release_authority = self.release_authority

        expiration_date: str | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.strftime('%Y-%m-%d')

        document = self.document

        is_valid = self.is_valid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if member is not UNSET:
            field_dict["member"] = member
        if number is not UNSET:
            field_dict["number"] = number
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if release_authority is not UNSET:
            field_dict["release_authority"] = release_authority
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if document is not UNSET:
            field_dict["document"] = document
        if is_valid is not UNSET:
            field_dict["is_valid"] = is_valid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        member = d.pop("member", UNSET)

        number = d.pop("number", UNSET)

        _release_date = d.pop("release_date", UNSET)
        release_date: datetime.date | Unset
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        release_authority = d.pop("release_authority", UNSET)

        _expiration_date = d.pop("expiration_date", UNSET)
        expiration_date: datetime.date | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date).date()

        document = d.pop("document", UNSET)

        is_valid = d.pop("is_valid", UNSET)

        patched_member_cie_document = cls(
            id=id,
            member=member,
            number=number,
            release_date=release_date,
            release_authority=release_authority,
            expiration_date=expiration_date,
            document=document,
            is_valid=is_valid,
        )

        patched_member_cie_document.additional_properties = d
        return patched_member_cie_document

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
