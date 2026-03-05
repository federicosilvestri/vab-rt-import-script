from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_qualifica_source_enum import MemberQualificaSourceEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualifica import Qualifica


T = TypeVar("T", bound="PatchedMemberQualifica")


@_attrs_define
class PatchedMemberQualifica:
    """Serializer for MemberQualifica (assignment of a Qualifica to a Member).

    - qualifica_detail exposes the full Qualifica object for display.
    - qualifica (FK) is the writable field.

        Attributes:
            id (int | Unset):
            member (int | Unset):
            qualifica (int | Unset):
            qualifica_detail (Qualifica | Unset): Read-only lookup serializer for Qualifica.
            source (MemberQualificaSourceEnum | Unset): * `CORSO_INT` - Assegnato da corso interno
                * `CORSO_EXT` - Assegnata da corso esterno
                * `MERITO` - Assegnata per merito
                * `OTHER` - Assegnata per altri motivi
    """

    id: int | Unset = UNSET
    member: int | Unset = UNSET
    qualifica: int | Unset = UNSET
    qualifica_detail: Qualifica | Unset = UNSET
    source: MemberQualificaSourceEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        qualifica = self.qualifica

        qualifica_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qualifica_detail, Unset):
            qualifica_detail = self.qualifica_detail.to_dict()

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if member is not UNSET:
            field_dict["member"] = member
        if qualifica is not UNSET:
            field_dict["qualifica"] = qualifica
        if qualifica_detail is not UNSET:
            field_dict["qualifica_detail"] = qualifica_detail
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualifica import Qualifica

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        member = d.pop("member", UNSET)

        qualifica = d.pop("qualifica", UNSET)

        _qualifica_detail = d.pop("qualifica_detail", UNSET)
        qualifica_detail: Qualifica | Unset
        if isinstance(_qualifica_detail, Unset):
            qualifica_detail = UNSET
        else:
            qualifica_detail = Qualifica.from_dict(_qualifica_detail)

        _source = d.pop("source", UNSET)
        source: MemberQualificaSourceEnum | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = MemberQualificaSourceEnum(_source)

        patched_member_qualifica = cls(
            id=id,
            member=member,
            qualifica=qualifica,
            qualifica_detail=qualifica_detail,
            source=source,
        )

        patched_member_qualifica.additional_properties = d
        return patched_member_qualifica

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
