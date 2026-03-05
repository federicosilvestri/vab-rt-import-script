from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAuthUser")


@_attrs_define
class PatchedAuthUser:
    """Base serializer - read only, generic replies

    Attributes:
        id (int | Unset):
        email (str | Unset):
        first_name (None | str | Unset):
        last_name (None | str | Unset):
        is_active (bool | Unset):
        is_staff (bool | Unset):
        date_joined (datetime.datetime | Unset):
        last_login (datetime.datetime | None | Unset):
        user_type (str | Unset):
    """

    id: int | Unset = UNSET
    email: str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_staff: bool | Unset = UNSET
    date_joined: datetime.datetime | Unset = UNSET
    last_login: datetime.datetime | None | Unset = UNSET
    user_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        is_active = self.is_active

        is_staff = self.is_staff

        date_joined: str | Unset = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.strftime('%Y-%m-%d')

        last_login: None | str | Unset
        if isinstance(self.last_login, Unset):
            last_login = UNSET
        elif isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.strftime('%Y-%m-%d')
        else:
            last_login = self.last_login

        user_type = self.user_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if user_type is not UNSET:
            field_dict["user_type"] = user_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        is_active = d.pop("is_active", UNSET)

        is_staff = d.pop("is_staff", UNSET)

        _date_joined = d.pop("date_joined", UNSET)
        date_joined: datetime.datetime | Unset
        if isinstance(_date_joined, Unset):
            date_joined = UNSET
        else:
            date_joined = isoparse(_date_joined)

        def _parse_last_login(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_type_0 = isoparse(data)

                return last_login_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_login = _parse_last_login(d.pop("last_login", UNSET))

        user_type = d.pop("user_type", UNSET)

        patched_auth_user = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            is_staff=is_staff,
            date_joined=date_joined,
            last_login=last_login,
            user_type=user_type,
        )

        patched_auth_user.additional_properties = d
        return patched_auth_user

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
