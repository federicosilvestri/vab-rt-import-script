from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.member_abilitazione_source_enum import MemberAbilitazioneSourceEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abilitazione import Abilitazione


T = TypeVar("T", bound="MemberAbilitazione")


@_attrs_define
class MemberAbilitazione:
    """Serializer for MemberAbilitazione (assignment of an Abilitazione to a Member).

    - is_valid and is_revoked are computed properties exposed as read-only.
    - abilitazione_detail exposes the full Abilitazione object for display.
    - For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
      expires_at become required. This is enforced by the model's clean().

        Attributes:
            id (int):
            member (int):
            abilitazione (int):
            abilitazione_detail (Abilitazione): Read-only lookup serializer for Abilitazione.
            source (MemberAbilitazioneSourceEnum): * `CORSO_INT` - Corso interno
                * `CORSO_EXT` - Corso esterno
                * `TITOLO` - Titolo professionale
                * `ALTRO` - Altro
            is_valid (bool):
            is_revoked (bool):
            issued_at (datetime.date | None | Unset):
            expires_at (datetime.date | None | Unset): Lasciare vuoto se l'abilitazione non ha scadenza
            certificate_code (str | Unset): Se disponibile, indicare il numero attestato, o il codice seriale.
            revoked_at (datetime.date | None | Unset):
    """

    id: int
    member: int
    abilitazione: int
    abilitazione_detail: Abilitazione
    source: MemberAbilitazioneSourceEnum
    is_valid: bool
    is_revoked: bool
    issued_at: datetime.date | None | Unset = UNSET
    expires_at: datetime.date | None | Unset = UNSET
    certificate_code: str | Unset = UNSET
    revoked_at: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        abilitazione = self.abilitazione

        abilitazione_detail = self.abilitazione_detail.to_dict()

        source = self.source.value

        is_valid = self.is_valid

        is_revoked = self.is_revoked

        issued_at: None | str | Unset
        if isinstance(self.issued_at, Unset):
            issued_at = UNSET
        elif isinstance(self.issued_at, datetime.date):
            issued_at = self.issued_at.strftime('%Y-%m-%d')
        else:
            issued_at = self.issued_at

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.date):
            expires_at = self.expires_at.strftime('%Y-%m-%d')
        else:
            expires_at = self.expires_at

        certificate_code = self.certificate_code

        revoked_at: None | str | Unset
        if isinstance(self.revoked_at, Unset):
            revoked_at = UNSET
        elif isinstance(self.revoked_at, datetime.date):
            revoked_at = self.revoked_at.strftime('%Y-%m-%d')
        else:
            revoked_at = self.revoked_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member": member,
                "abilitazione": abilitazione,
                "abilitazione_detail": abilitazione_detail,
                "source": source,
                "is_valid": is_valid,
                "is_revoked": is_revoked,
            }
        )
        if issued_at is not UNSET:
            field_dict["issued_at"] = issued_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if certificate_code is not UNSET:
            field_dict["certificate_code"] = certificate_code
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abilitazione import Abilitazione

        d = dict(src_dict)
        id = d.pop("id")

        member = d.pop("member")

        abilitazione = d.pop("abilitazione")

        abilitazione_detail = Abilitazione.from_dict(d.pop("abilitazione_detail"))

        source = MemberAbilitazioneSourceEnum(d.pop("source"))

        is_valid = d.pop("is_valid")

        is_revoked = d.pop("is_revoked")

        def _parse_issued_at(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                issued_at_type_0 = isoparse(data).date()

                return issued_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        issued_at = _parse_issued_at(d.pop("issued_at", UNSET))

        def _parse_expires_at(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data).date()

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        certificate_code = d.pop("certificate_code", UNSET)

        def _parse_revoked_at(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = isoparse(data).date()

                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at", UNSET))

        member_abilitazione = cls(
            id=id,
            member=member,
            abilitazione=abilitazione,
            abilitazione_detail=abilitazione_detail,
            source=source,
            is_valid=is_valid,
            is_revoked=is_revoked,
            issued_at=issued_at,
            expires_at=expires_at,
            certificate_code=certificate_code,
            revoked_at=revoked_at,
        )

        member_abilitazione.additional_properties = d
        return member_abilitazione

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
