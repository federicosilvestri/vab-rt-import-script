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


T = TypeVar("T", bound="PatchedMemberJob")


@_attrs_define
class PatchedMemberJob:
    """Serializer for MemberJob.

    - is_active is a computed property (end_date is null) exposed as read-only.
    - company is represented as a nested read-only object for display;
      use company_id (write) to assign the FK.

        Attributes:
            id (int | Unset):
            member (int | Unset):
            company (int | Unset):
            company_detail (Company | Unset): Serializer for Company (employer).

                Handles both Italian and foreign legal addresses.
                The model's clean() method enforces conditional validation
                (Italian fields vs foreign_address).
            contract_type (ContractTypeEnum | Unset): * `DIP` - Lavoro dipendente
                * `AUT` - Lavoratore autonomo
                * `PIVA` - Partita IVA
                * `COCO` - Collaborazione (Co.co.co)
                * `TIR` - Tirocinio / Stage
                * `OCC` - Prestazione occasionale
            start_date (datetime.date | Unset): Data inizio rapporto lavorativo
            end_date (datetime.date | Unset): Data fine rapporto lavorativo, lasciare bianca se ancora in forza
            is_active (bool | Unset):
    """

    id: int | Unset = UNSET
    member: int | Unset = UNSET
    company: int | Unset = UNSET
    company_detail: Company | Unset = UNSET
    contract_type: ContractTypeEnum | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    is_active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        company = self.company

        company_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company_detail, Unset):
            company_detail = self.company_detail.to_dict()

        contract_type: str | Unset = UNSET
        if not isinstance(self.contract_type, Unset):
            contract_type = self.contract_type.value

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.strftime('%Y-%m-%d')

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.strftime('%Y-%m-%d')

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if member is not UNSET:
            field_dict["member"] = member
        if company is not UNSET:
            field_dict["company"] = company
        if company_detail is not UNSET:
            field_dict["company_detail"] = company_detail
        if contract_type is not UNSET:
            field_dict["contract_type"] = contract_type
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company import Company

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        member = d.pop("member", UNSET)

        company = d.pop("company", UNSET)

        _company_detail = d.pop("company_detail", UNSET)
        company_detail: Company | Unset
        if isinstance(_company_detail, Unset):
            company_detail = UNSET
        else:
            company_detail = Company.from_dict(_company_detail)

        _contract_type = d.pop("contract_type", UNSET)
        contract_type: ContractTypeEnum | Unset
        if isinstance(_contract_type, Unset):
            contract_type = UNSET
        else:
            contract_type = ContractTypeEnum(_contract_type)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        is_active = d.pop("is_active", UNSET)

        patched_member_job = cls(
            id=id,
            member=member,
            company=company,
            company_detail=company_detail,
            contract_type=contract_type,
            start_date=start_date,
            end_date=end_date,
            is_active=is_active,
        )

        patched_member_job.additional_properties = d
        return patched_member_job

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
