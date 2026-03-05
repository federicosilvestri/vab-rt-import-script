from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthUser")


@_attrs_define
class AuthUser:
    """Base serializer - read only, generic replies

    Attributes:
        id (int):
        email (str):
        first_name (None | str):
        last_name (None | str):
        date_joined (datetime.datetime):
        last_login (datetime.datetime | None):
        user_type (str):
        is_active (bool | Unset):
        is_staff (bool | Unset):
    """

    id: int
    email: str
    first_name: None | str
    last_name: None | str
    date_joined: datetime.datetime
    last_login: datetime.datetime | None
    user_type: str
    is_active: bool | Unset = UNSET
    is_staff: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name: None | str
        first_name = self.first_name

        last_name: None | str
        last_name = self.last_name

        date_joined = self.date_joined.strftime('%Y-%m-%d')

        last_login: None | str
        if isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.strftime('%Y-%m-%d')
        else:
            last_login = self.last_login

        user_type = self.user_type

        is_active = self.is_active

        is_staff = self.is_staff

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "date_joined": date_joined,
                "last_login": last_login,
                "user_type": user_type,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        def _parse_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_name = _parse_first_name(d.pop("first_name"))

        def _parse_last_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_name = _parse_last_name(d.pop("last_name"))

        date_joined = isoparse(d.pop("date_joined"))

        def _parse_last_login(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_type_0 = isoparse(data)

                return last_login_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_login = _parse_last_login(d.pop("last_login"))

        user_type = d.pop("user_type")

        is_active = d.pop("is_active", UNSET)

        is_staff = d.pop("is_staff", UNSET)

        auth_user = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_joined=date_joined,
            last_login=last_login,
            user_type=user_type,
            is_active=is_active,
            is_staff=is_staff,
        )

        auth_user.additional_properties = d
        return auth_user

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
