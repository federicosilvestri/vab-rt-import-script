from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_email import MemberEmail
from ...types import Response


def _get_kwargs(
    member_pk: int,
    *,
    body: MemberEmail,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/members/member/{member_pk}/emails/".format(
            member_pk=quote(str(member_pk), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MemberEmail | None:
    if response.status_code == 201:
        response_201 = MemberEmail.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MemberEmail]:
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
    body: MemberEmail,
) -> Response[MemberEmail]:
    """List all emails for a member, or add a new one.

    When creating with primary=True, the model automatically demotes
    the previous primary email.
    A PEC address cannot be set as primary (enforced by model clean).

    Args:
        member_pk (int):
        body (MemberEmail): Serializer for MemberEmail.

            - verified is read-only: set internally via verification flow.
            - primary flag management is handled by the model's save() method,
              which automatically demotes the previous primary when a new one is set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberEmail]
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
    body: MemberEmail,
) -> MemberEmail | None:
    """List all emails for a member, or add a new one.

    When creating with primary=True, the model automatically demotes
    the previous primary email.
    A PEC address cannot be set as primary (enforced by model clean).

    Args:
        member_pk (int):
        body (MemberEmail): Serializer for MemberEmail.

            - verified is read-only: set internally via verification flow.
            - primary flag management is handled by the model's save() method,
              which automatically demotes the previous primary when a new one is set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberEmail
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
    body: MemberEmail,
) -> Response[MemberEmail]:
    """List all emails for a member, or add a new one.

    When creating with primary=True, the model automatically demotes
    the previous primary email.
    A PEC address cannot be set as primary (enforced by model clean).

    Args:
        member_pk (int):
        body (MemberEmail): Serializer for MemberEmail.

            - verified is read-only: set internally via verification flow.
            - primary flag management is handled by the model's save() method,
              which automatically demotes the previous primary when a new one is set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberEmail]
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
    body: MemberEmail,
) -> MemberEmail | None:
    """List all emails for a member, or add a new one.

    When creating with primary=True, the model automatically demotes
    the previous primary email.
    A PEC address cannot be set as primary (enforced by model clean).

    Args:
        member_pk (int):
        body (MemberEmail): Serializer for MemberEmail.

            - verified is read-only: set internally via verification flow.
            - primary flag management is handled by the model's save() method,
              which automatically demotes the previous primary when a new one is set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberEmail
    """

    return (
        await asyncio_detailed(
            member_pk=member_pk,
            client=client,
            body=body,
        )
    ).parsed
