from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member import Member
from ...types import Response


def _get_kwargs(
    *,
    body: Member,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/members/member/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Member | None:
    if response.status_code == 201:
        response_201 = Member.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: Member,
) -> Response[Member]:
    """List all members or create a new one.

    GET  -> returns lightweight MemberListSerializer (no nested rank/status objects).
    POST -> uses full MemberSerializer with all validation.

    Args:
        body (Member): Full serializer for the Member model.

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
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Member,
) -> Member | None:
    """List all members or create a new one.

    GET  -> returns lightweight MemberListSerializer (no nested rank/status objects).
    POST -> uses full MemberSerializer with all validation.

    Args:
        body (Member): Full serializer for the Member model.

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
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Member,
) -> Response[Member]:
    """List all members or create a new one.

    GET  -> returns lightweight MemberListSerializer (no nested rank/status objects).
    POST -> uses full MemberSerializer with all validation.

    Args:
        body (Member): Full serializer for the Member model.

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
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Member,
) -> Member | None:
    """List all members or create a new one.

    GET  -> returns lightweight MemberListSerializer (no nested rank/status objects).
    POST -> uses full MemberSerializer with all validation.

    Args:
        body (Member): Full serializer for the Member model.

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
            client=client,
            body=body,
        )
    ).parsed
