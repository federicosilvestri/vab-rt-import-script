from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedMemberEmail")


@_attrs_define
class PatchedMemberEmail:
    """Serializer for MemberEmail.

    - verified is read-only: set internally via verification flow.
    - primary flag management is handled by the model's save() method,
      which automatically demotes the previous primary when a new one is set.

        Attributes:
            id (int | Unset):
            member (int | Unset):
            email (str | Unset):
            is_pec (bool | Unset): Indica se questa mail è una PEC
            primary (bool | Unset): Contrassegna questo campo per indicare che l'indirizzo email è quello principale.
            verified (bool | Unset):
    """

    id: int | Unset = UNSET
    member: int | Unset = UNSET
    email: str | Unset = UNSET
    is_pec: bool | Unset = UNSET
    primary: bool | Unset = UNSET
    verified: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        email = self.email

        is_pec = self.is_pec

        primary = self.primary

        verified = self.verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if member is not UNSET:
            field_dict["member"] = member
        if email is not UNSET:
            field_dict["email"] = email
        if is_pec is not UNSET:
            field_dict["is_pec"] = is_pec
        if primary is not UNSET:
            field_dict["primary"] = primary
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        member = d.pop("member", UNSET)

        email = d.pop("email", UNSET)

        is_pec = d.pop("is_pec", UNSET)

        primary = d.pop("primary", UNSET)

        verified = d.pop("verified", UNSET)

        patched_member_email = cls(
            id=id,
            member=member,
            email=email,
            is_pec=is_pec,
            primary=primary,
            verified=verified,
        )

        patched_member_email.additional_properties = d
        return patched_member_email

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
