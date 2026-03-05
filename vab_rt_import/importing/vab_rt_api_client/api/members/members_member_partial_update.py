from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member import Member
from ...models.patched_member import PatchedMember
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: PatchedMember | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/members/member/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Member | None:
    if response.status_code == 200:
        response_200 = Member.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Member]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMember | Unset = UNSET,
) -> Response[Member]:
    """Retrieve, update, or soft-delete a single Member.

    DELETE sets is_active=False on the linked AuthUser if present,
    but does NOT delete the Member record itself to preserve historical data.

    Args:
        id (int):
        body (PatchedMember | Unset): Full serializer for the Member model.

            - rank and status are read-only: managed internally via FSM transitions.
            - operative is read-only: computed field, not editable.
            - age is a computed property exposed as a read-only field.
            - fiscal_code is auto-filled by the model's clean() method when possible,
              so it can be left blank on creation if all birth data is provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Member]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMember | Unset = UNSET,
) -> Member | None:
    """Retrieve, update, or soft-delete a single Member.

    DELETE sets is_active=False on the linked AuthUser if present,
    but does NOT delete the Member record itself to preserve historical data.

    Args:
        id (int):
        body (PatchedMember | Unset): Full serializer for the Member model.

            - rank and status are read-only: managed internally via FSM transitions.
            - operative is read-only: computed field, not editable.
            - age is a computed property exposed as a read-only field.
            - fiscal_code is auto-filled by the model's clean() method when possible,
              so it can be left blank on creation if all birth data is provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Member
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMember | Unset = UNSET,
) -> Response[Member]:
    """Retrieve, update, or soft-delete a single Member.

    DELETE sets is_active=False on the linked AuthUser if present,
    but does NOT delete the Member record itself to preserve historical data.

    Args:
        id (int):
        body (PatchedMember | Unset): Full serializer for the Member model.

            - rank and status are read-only: managed internally via FSM transitions.
            - operative is read-only: computed field, not editable.
            - age is a computed property exposed as a read-only field.
            - fiscal_code is auto-filled by the model's clean() method when possible,
              so it can be left blank on creation if all birth data is provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Member]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMember | Unset = UNSET,
) -> Member | None:
    """Retrieve, update, or soft-delete a single Member.

    DELETE sets is_active=False on the linked AuthUser if present,
    but does NOT delete the Member record itself to preserve historical data.

    Args:
        id (int):
        body (PatchedMember | Unset): Full serializer for the Member model.

            - rank and status are read-only: managed internally via FSM transitions.
            - operative is read-only: computed field, not editable.
            - age is a computed property exposed as a read-only field.
            - fiscal_code is auto-filled by the model's clean() method when possible,
              so it can be left blank on creation if all birth data is provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Member
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
