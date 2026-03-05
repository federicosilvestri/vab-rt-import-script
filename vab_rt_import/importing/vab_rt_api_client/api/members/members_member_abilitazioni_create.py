from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_abilitazione import MemberAbilitazione
from ...types import Response


def _get_kwargs(
    member_pk: int,
    *,
    body: MemberAbilitazione,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/members/member/{member_pk}/abilitazioni/".format(
            member_pk=quote(str(member_pk), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MemberAbilitazione | None:
    if response.status_code == 201:
        response_201 = MemberAbilitazione.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MemberAbilitazione]:
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
    body: MemberAbilitazione,
) -> Response[MemberAbilitazione]:
    """List all abilitazioni assigned to a member, or assign a new one.

    For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
    expires_at are required. This is enforced by the model's clean().

    Args:
        member_pk (int):
        body (MemberAbilitazione): Serializer for MemberAbilitazione (assignment of an
            Abilitazione to a Member).

            - is_valid and is_revoked are computed properties exposed as read-only.
            - abilitazione_detail exposes the full Abilitazione object for display.
            - For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
              expires_at become required. This is enforced by the model's clean().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberAbilitazione]
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
    body: MemberAbilitazione,
) -> MemberAbilitazione | None:
    """List all abilitazioni assigned to a member, or assign a new one.

    For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
    expires_at are required. This is enforced by the model's clean().

    Args:
        member_pk (int):
        body (MemberAbilitazione): Serializer for MemberAbilitazione (assignment of an
            Abilitazione to a Member).

            - is_valid and is_revoked are computed properties exposed as read-only.
            - abilitazione_detail exposes the full Abilitazione object for display.
            - For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
              expires_at become required. This is enforced by the model's clean().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberAbilitazione
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
    body: MemberAbilitazione,
) -> Response[MemberAbilitazione]:
    """List all abilitazioni assigned to a member, or assign a new one.

    For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
    expires_at are required. This is enforced by the model's clean().

    Args:
        member_pk (int):
        body (MemberAbilitazione): Serializer for MemberAbilitazione (assignment of an
            Abilitazione to a Member).

            - is_valid and is_revoked are computed properties exposed as read-only.
            - abilitazione_detail exposes the full Abilitazione object for display.
            - For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
              expires_at become required. This is enforced by the model's clean().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberAbilitazione]
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
    body: MemberAbilitazione,
) -> MemberAbilitazione | None:
    """List all abilitazioni assigned to a member, or assign a new one.

    For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
    expires_at are required. This is enforced by the model's clean().

    Args:
        member_pk (int):
        body (MemberAbilitazione): Serializer for MemberAbilitazione (assignment of an
            Abilitazione to a Member).

            - is_valid and is_revoked are computed properties exposed as read-only.
            - abilitazione_detail exposes the full Abilitazione object for display.
            - For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
              expires_at become required. This is enforced by the model's clean().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberAbilitazione
    """

    return (
        await asyncio_detailed(
            member_pk=member_pk,
            client=client,
            body=body,
        )
    ).parsed
