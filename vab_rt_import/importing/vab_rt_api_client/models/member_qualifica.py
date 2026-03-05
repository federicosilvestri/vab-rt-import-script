from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_qualifica_source_enum import MemberQualificaSourceEnum

if TYPE_CHECKING:
    from ..models.qualifica import Qualifica


T = TypeVar("T", bound="MemberQualifica")


@_attrs_define
class MemberQualifica:
    """Serializer for MemberQualifica (assignment of a Qualifica to a Member).

    - qualifica_detail exposes the full Qualifica object for display.
    - qualifica (FK) is the writable field.

        Attributes:
            id (int):
            member (int):
            qualifica (int):
            qualifica_detail (Qualifica): Read-only lookup serializer for Qualifica.
            source (MemberQualificaSourceEnum): * `CORSO_INT` - Assegnato da corso interno
                * `CORSO_EXT` - Assegnata da corso esterno
                * `MERITO` - Assegnata per merito
                * `OTHER` - Assegnata per altri motivi
    """

    id: int
    member: int
    qualifica: int
    qualifica_detail: Qualifica
    source: MemberQualificaSourceEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        qualifica = self.qualifica

        qualifica_detail = self.qualifica_detail.to_dict()

        source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member": member,
                "qualifica": qualifica,
                "qualifica_detail": qualifica_detail,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qualifica import Qualifica

        d = dict(src_dict)
        id = d.pop("id")

        member = d.pop("member")

        qualifica = d.pop("qualifica")

        qualifica_detail = Qualifica.from_dict(d.pop("qualifica_detail"))

        source = MemberQualificaSourceEnum(d.pop("source"))

        member_qualifica = cls(
            id=id,
            member=member,
            qualifica=qualifica,
            qualifica_detail=qualifica_detail,
            source=source,
        )

        member_qualifica.additional_properties = d
        return member_qualifica

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
