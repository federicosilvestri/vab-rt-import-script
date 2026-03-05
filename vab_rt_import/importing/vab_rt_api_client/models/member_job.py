from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.contract_type_enum import ContractTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company import Company


T = TypeVar("T", bound="MemberJob")


@_attrs_define
class MemberJob:
    """Serializer for MemberJob.

    - is_active is a computed property (end_date is null) exposed as read-only.
    - company is represented as a nested read-only object for display;
      use company_id (write) to assign the FK.

        Attributes:
            id (int):
            member (int):
            company (int):
            company_detail (Company): Serializer for Company (employer).

                Handles both Italian and foreign legal addresses.
                The model's clean() method enforces conditional validation
                (Italian fields vs foreign_address).
            contract_type (ContractTypeEnum): * `DIP` - Lavoro dipendente
                * `AUT` - Lavoratore autonomo
                * `PIVA` - Partita IVA
                * `COCO` - Collaborazione (Co.co.co)
                * `TIR` - Tirocinio / Stage
                * `OCC` - Prestazione occasionale
            start_date (datetime.date): Data inizio rapporto lavorativo
            is_active (bool):
            end_date (datetime.date | Unset): Data fine rapporto lavorativo, lasciare bianca se ancora in forza
    """

    id: int
    member: int
    company: int
    company_detail: Company
    contract_type: ContractTypeEnum
    start_date: datetime.date
    is_active: bool
    end_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        company = self.company

        company_detail = self.company_detail.to_dict()

        contract_type = self.contract_type.value

        start_date = self.start_date.strftime('%Y-%m-%d')

        is_active = self.is_active

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.strftime('%Y-%m-%d')

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member": member,
                "company": company,
                "company_detail": company_detail,
                "contract_type": contract_type,
                "start_date": start_date,
                "is_active": is_active,
            }
        )
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company import Company

        d = dict(src_dict)
        id = d.pop("id")

        member = d.pop("member")

        company = d.pop("company")

        company_detail = Company.from_dict(d.pop("company_detail"))

        contract_type = ContractTypeEnum(d.pop("contract_type"))

        start_date = isoparse(d.pop("start_date")).date()

        is_active = d.pop("is_active")

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        member_job = cls(
            id=id,
            member=member,
            company=company,
            company_detail=company_detail,
            contract_type=contract_type,
            start_date=start_date,
            is_active=is_active,
            end_date=end_date,
        )

        member_job.additional_properties = d
        return member_job

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
