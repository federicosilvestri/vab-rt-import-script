from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberEmail")


@_attrs_define
class MemberEmail:
    """Serializer for MemberEmail.

    - verified is read-only: set internally via verification flow.
    - primary flag management is handled by the model's save() method,
      which automatically demotes the previous primary when a new one is set.

        Attributes:
            id (int):
            member (int):
            email (str):
            verified (bool):
            is_pec (bool | Unset): Indica se questa mail è una PEC
            primary (bool | Unset): Contrassegna questo campo per indicare che l'indirizzo email è quello principale.
    """

    id: int
    member: int
    email: str
    verified: bool
    is_pec: bool | Unset = UNSET
    primary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        email = self.email

        verified = self.verified

        is_pec = self.is_pec

        primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member": member,
                "email": email,
                "verified": verified,
            }
        )
        if is_pec is not UNSET:
            field_dict["is_pec"] = is_pec
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        member = d.pop("member")

        email = d.pop("email")

        verified = d.pop("verified")

        is_pec = d.pop("is_pec", UNSET)

        primary = d.pop("primary", UNSET)

        member_email = cls(
            id=id,
            member=member,
            email=email,
            verified=verified,
            is_pec=is_pec,
            primary=primary,
        )

        member_email.additional_properties = d
        return member_email

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
