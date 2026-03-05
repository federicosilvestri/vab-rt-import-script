from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_driver_license_document import MemberDriverLicenseDocument
from ...types import Response


def _get_kwargs(
    member_pk: int,
    *,
    body: MemberDriverLicenseDocument,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/members/member/{member_pk}/licenses/".format(
            member_pk=quote(str(member_pk), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MemberDriverLicenseDocument | None:
    if response.status_code == 201:
        response_201 = MemberDriverLicenseDocument.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MemberDriverLicenseDocument]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    member_pk: int,
    *,
    client: AuthenticatedClient,
    body: MemberDriverLicenseDocument,
) -> Response[MemberDriverLicenseDocument]:
    """List all driver license documents for a member, or upload a new one.

    After creation, add categories via the MemberDriverLicenseCategoryListView.
    A license without categories is considered incomplete (is_complete=False).

    Args:
        member_pk (int):
        body (MemberDriverLicenseDocument): Serializer for MemberDriverLicenseDocument.

            - categories are nested and read-only on this serializer.
              Use the MemberDriverLicenseCategorySerializer endpoint to add/remove categories.
            - is_valid and is_complete are computed properties exposed as read-only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberDriverLicenseDocument]
    """

    kwargs = _get_kwargs(
        member_pk=member_pk,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    member_pk: int,
    *,
    client: AuthenticatedClient,
    body: MemberDriverLicenseDocument,
) -> MemberDriverLicenseDocument | None:
    """List all driver license documents for a member, or upload a new one.

    After creation, add categories via the MemberDriverLicenseCategoryListView.
    A license without categories is considered incomplete (is_complete=False).

    Args:
        member_pk (int):
        body (MemberDriverLicenseDocument): Serializer for MemberDriverLicenseDocument.

            - categories are nested and read-only on this serializer.
              Use the MemberDriverLicenseCategorySerializer endpoint to add/remove categories.
            - is_valid and is_complete are computed properties exposed as read-only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberDriverLicenseDocument
    """

    return sync_detailed(
        member_pk=member_pk,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    member_pk: int,
    *,
    client: AuthenticatedClient,
    body: MemberDriverLicenseDocument,
) -> Response[MemberDriverLicenseDocument]:
    """List all driver license documents for a member, or upload a new one.

    After creation, add categories via the MemberDriverLicenseCategoryListView.
    A license without categories is considered incomplete (is_complete=False).

    Args:
        member_pk (int):
        body (MemberDriverLicenseDocument): Serializer for MemberDriverLicenseDocument.

            - categories are nested and read-only on this serializer.
              Use the MemberDriverLicenseCategorySerializer endpoint to add/remove categories.
            - is_valid and is_complete are computed properties exposed as read-only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberDriverLicenseDocument]
    """

    kwargs = _get_kwargs(
        member_pk=member_pk,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    member_pk: int,
    *,
    client: AuthenticatedClient,
    body: MemberDriverLicenseDocument,
) -> MemberDriverLicenseDocument | None:
    """List all driver license documents for a member, or upload a new one.

    After creation, add categories via the MemberDriverLicenseCategoryListView.
    A license without categories is considered incomplete (is_complete=False).

    Args:
        member_pk (int):
        body (MemberDriverLicenseDocument): Serializer for MemberDriverLicenseDocument.

            - categories are nested and read-only on this serializer.
              Use the MemberDriverLicenseCategorySerializer endpoint to add/remove categories.
            - is_valid and is_complete are computed properties exposed as read-only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberDriverLicenseDocument
    """

    return (
        await asyncio_detailed(
            member_pk=member_pk,
            client=client,
            body=body,
        )
    ).parsed
