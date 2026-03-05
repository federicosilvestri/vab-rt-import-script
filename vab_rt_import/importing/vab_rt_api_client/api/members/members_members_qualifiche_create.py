from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_qualifica import MemberQualifica
from ...types import Response


def _get_kwargs(
    member_pk: int,
    *,
    body: MemberQualifica,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/members/members/{member_pk}/qualifiche/".format(
            member_pk=quote(str(member_pk), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MemberQualifica | None:
    if response.status_code == 201:
        response_201 = MemberQualifica.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MemberQualifica]:
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
    body: MemberQualifica,
) -> Response[MemberQualifica]:
    """List all qualifiche assigned to a member, or assign a new one.

    qualifica_detail is returned nested for display; use qualifica (FK id) to write.

    Args:
        member_pk (int):
        body (MemberQualifica): Serializer for MemberQualifica (assignment of a Qualifica to a
            Member).

            - qualifica_detail exposes the full Qualifica object for display.
            - qualifica (FK) is the writable field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberQualifica]
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
    body: MemberQualifica,
) -> MemberQualifica | None:
    """List all qualifiche assigned to a member, or assign a new one.

    qualifica_detail is returned nested for display; use qualifica (FK id) to write.

    Args:
        member_pk (int):
        body (MemberQualifica): Serializer for MemberQualifica (assignment of a Qualifica to a
            Member).

            - qualifica_detail exposes the full Qualifica object for display.
            - qualifica (FK) is the writable field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberQualifica
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
    body: MemberQualifica,
) -> Response[MemberQualifica]:
    """List all qualifiche assigned to a member, or assign a new one.

    qualifica_detail is returned nested for display; use qualifica (FK id) to write.

    Args:
        member_pk (int):
        body (MemberQualifica): Serializer for MemberQualifica (assignment of a Qualifica to a
            Member).

            - qualifica_detail exposes the full Qualifica object for display.
            - qualifica (FK) is the writable field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberQualifica]
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
    body: MemberQualifica,
) -> MemberQualifica | None:
    """List all qualifiche assigned to a member, or assign a new one.

    qualifica_detail is returned nested for display; use qualifica (FK id) to write.

    Args:
        member_pk (int):
        body (MemberQualifica): Serializer for MemberQualifica (assignment of a Qualifica to a
            Member).

            - qualifica_detail exposes the full Qualifica object for display.
            - qualifica (FK) is the writable field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberQualifica
    """

    return (
        await asyncio_detailed(
            member_pk=member_pk,
            client=client,
            body=body,
        )
    ).parsed
