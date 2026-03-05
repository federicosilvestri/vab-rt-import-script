from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_driver_license_category import MemberDriverLicenseCategory
from ...types import Response


def _get_kwargs(
    member_pk: int,
    license_pk: int,
    *,
    body: MemberDriverLicenseCategory,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/members/member/{member_pk}/licenses/{license_pk}/categories/".format(
            member_pk=quote(str(member_pk), safe=""),
            license_pk=quote(str(license_pk), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MemberDriverLicenseCategory | None:
    if response.status_code == 201:
        response_201 = MemberDriverLicenseCategory.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MemberDriverLicenseCategory]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    member_pk: int,
    license_pk: int,
    *,
    client: AuthenticatedClient,
    body: MemberDriverLicenseCategory,
) -> Response[MemberDriverLicenseCategory]:
    """List all categories for a specific driver license, or add a new one.

    URL requires both member_pk and license_pk.

    Args:
        member_pk (int):
        license_pk (int):
        body (MemberDriverLicenseCategory): Serializer for a single driver license category entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberDriverLicenseCategory]
    """

    kwargs = _get_kwargs(
        member_pk=member_pk,
        license_pk=license_pk,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    member_pk: int,
    license_pk: int,
    *,
    client: AuthenticatedClient,
    body: MemberDriverLicenseCategory,
) -> MemberDriverLicenseCategory | None:
    """List all categories for a specific driver license, or add a new one.

    URL requires both member_pk and license_pk.

    Args:
        member_pk (int):
        license_pk (int):
        body (MemberDriverLicenseCategory): Serializer for a single driver license category entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberDriverLicenseCategory
    """

    return sync_detailed(
        member_pk=member_pk,
        license_pk=license_pk,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    member_pk: int,
    license_pk: int,
    *,
    client: AuthenticatedClient,
    body: MemberDriverLicenseCategory,
) -> Response[MemberDriverLicenseCategory]:
    """List all categories for a specific driver license, or add a new one.

    URL requires both member_pk and license_pk.

    Args:
        member_pk (int):
        license_pk (int):
        body (MemberDriverLicenseCategory): Serializer for a single driver license category entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberDriverLicenseCategory]
    """

    kwargs = _get_kwargs(
        member_pk=member_pk,
        license_pk=license_pk,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    member_pk: int,
    license_pk: int,
    *,
    client: AuthenticatedClient,
    body: MemberDriverLicenseCategory,
) -> MemberDriverLicenseCategory | None:
    """List all categories for a specific driver license, or add a new one.

    URL requires both member_pk and license_pk.

    Args:
        member_pk (int):
        license_pk (int):
        body (MemberDriverLicenseCategory): Serializer for a single driver license category entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberDriverLicenseCategory
    """

    return (
        await asyncio_detailed(
            member_pk=member_pk,
            license_pk=license_pk,
            client=client,
            body=body,
        )
    ).parsed
