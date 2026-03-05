from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MemberCIEDocument")


@_attrs_define
class MemberCIEDocument:
    """Serializer for MemberCIEDocument (Carta di Identità Elettronica).

    - is_valid is a computed property exposed as read-only.
    - document is a PDF file upload field.

        Attributes:
            id (int):
            member (int):
            number (str): Numero del documento, raffigurato in altro a destra nella parte frontale.
            release_date (datetime.date):
            release_authority (str): Indicare l'autorità che ha rilasciato il documento.
            expiration_date (datetime.date):
            document (str): Documento in PDF fronte retro a colori
            is_valid (bool):
    """

    id: int
    member: int
    number: str
    release_date: datetime.date
    release_authority: str
    expiration_date: datetime.date
    document: str
    is_valid: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        number = self.number

        release_date = self.release_date.strftime('%Y-%m-%d')

        release_authority = self.release_authority

        expiration_date = self.expiration_date.strftime('%Y-%m-%d')

        document = self.document

        is_valid = self.is_valid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member": member,
                "number": number,
                "release_date": release_date,
                "release_authority": release_authority,
                "expiration_date": expiration_date,
                "document": document,
                "is_valid": is_valid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        member = d.pop("member")

        number = d.pop("number")

        release_date = isoparse(d.pop("release_date")).date()

        release_authority = d.pop("release_authority")

        expiration_date = isoparse(d.pop("expiration_date")).date()

        document = d.pop("document")

        is_valid = d.pop("is_valid")

        member_cie_document = cls(
            id=id,
            member=member,
            number=number,
            release_date=release_date,
            release_authority=release_authority,
            expiration_date=expiration_date,
            document=document,
            is_valid=is_valid,
        )

        member_cie_document.additional_properties = d
        return member_cie_document

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
