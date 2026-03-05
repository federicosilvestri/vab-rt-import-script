from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionImport")


@_attrs_define
class SubscriptionImport:
    """
    Attributes:
        n_tessera (int):
        member (int):
        start_date (datetime.date):
        socio (bool | Unset): Indica se la persona è iscritta come socio
        volontario (bool | Unset): Indica se la persona è iscritta come volontario
        referring_member (int | None | Unset): Persona che ha presentato l'associazione all'iscritto
        end_date (datetime.date | None | Unset):
    """

    n_tessera: int
    member: int
    start_date: datetime.date
    socio: bool | Unset = UNSET
    volontario: bool | Unset = UNSET
    referring_member: int | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        n_tessera = self.n_tessera

        member = self.member

        start_date = self.start_date.strftime('%Y-%m-%d')

        socio = self.socio

        volontario = self.volontario

        referring_member: int | None | Unset
        if isinstance(self.referring_member, Unset):
            referring_member = UNSET
        else:
            referring_member = self.referring_member

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.strftime('%Y-%m-%d')
        else:
            end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "n_tessera": n_tessera,
                "member": member,
                "start_date": start_date,
            }
        )
        if socio is not UNSET:
            field_dict["socio"] = socio
        if volontario is not UNSET:
            field_dict["volontario"] = volontario
        if referring_member is not UNSET:
            field_dict["referring_member"] = referring_member
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        n_tessera = d.pop("n_tessera")

        member = d.pop("member")

        start_date = isoparse(d.pop("start_date")).date()

        socio = d.pop("socio", UNSET)

        volontario = d.pop("volontario", UNSET)

        def _parse_referring_member(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        referring_member = _parse_referring_member(d.pop("referring_member", UNSET))

        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        subscription_import = cls(
            n_tessera=n_tessera,
            member=member,
            start_date=start_date,
            socio=socio,
            volontario=volontario,
            referring_member=referring_member,
            end_date=end_date,
        )

        subscription_import.additional_properties = d
        return subscription_import

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
