from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberPhone")


@_attrs_define
class MemberPhone:
    """Serializer for MemberPhone.

    - verified is read-only: set internally via verification flow.
    - phone_number is stored and returned in E.164 format (e.g. +393331234567).

        Attributes:
            id (int):
            member (int):
            phone_number (str):
            verified (bool):
            primary (bool | Unset): Contrassegna questo campo per indicare che questo è il numero di telefono principale.
    """

    id: int
    member: int
    phone_number: str
    verified: bool
    primary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        phone_number = self.phone_number

        verified = self.verified

        primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member": member,
                "phone_number": phone_number,
                "verified": verified,
            }
        )
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        member = d.pop("member")

        phone_number = d.pop("phone_number")

        verified = d.pop("verified")

        primary = d.pop("primary", UNSET)

        member_phone = cls(
            id=id,
            member=member,
            phone_number=phone_number,
            verified=verified,
            primary=primary,
        )

        member_phone.additional_properties = d
        return member_phone

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
