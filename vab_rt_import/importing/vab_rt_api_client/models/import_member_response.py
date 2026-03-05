from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_member_response_map import ImportMemberResponseMap


T = TypeVar("T", bound="ImportMemberResponse")


@_attrs_define
class ImportMemberResponse:
    """
    Attributes:
        created (int):
        failed (int):
        errors (list[Any]):
        map_ (ImportMemberResponseMap):
    """

    created: int
    failed: int
    errors: list[Any]
    map_: ImportMemberResponseMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        failed = self.failed

        errors = self.errors

        map_ = self.map_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "failed": failed,
                "errors": errors,
                "map": map_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_member_response_map import ImportMemberResponseMap

        d = dict(src_dict)
        created = d.pop("created")

        failed = d.pop("failed")

        errors = cast(list[Any], d.pop("errors"))

        map_ = ImportMemberResponseMap.from_dict(d.pop("map"))

        import_member_response = cls(
            created=created,
            failed=failed,
            errors=errors,
            map_=map_,
        )

        import_member_response.additional_properties = d
        return import_member_response

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
