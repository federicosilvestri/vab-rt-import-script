from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_email import MemberEmail
from ...models.patched_member_email import PatchedMemberEmail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    member_pk: int,
    id: int,
    *,
    body: PatchedMemberEmail | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/members/member/{member_pk}/emails/{id}/".format(
            member_pk=quote(str(member_pk), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MemberEmail | None:
    if response.status_code == 200:
        response_200 = MemberEmail.from_dict(response.json())

        return response_200

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
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMemberEmail | Unset = UNSET,
) -> Response[MemberEmail]:
    """Retrieve, update, or delete a single email for a member.

    Args:
        member_pk (int):
        id (int):
        body (PatchedMemberEmail | Unset): Serializer for MemberEmail.

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
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    member_pk: int,
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMemberEmail | Unset = UNSET,
) -> MemberEmail | None:
    """Retrieve, update, or delete a single email for a member.

    Args:
        member_pk (int):
        id (int):
        body (PatchedMemberEmail | Unset): Serializer for MemberEmail.

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
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    member_pk: int,
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMemberEmail | Unset = UNSET,
) -> Response[MemberEmail]:
    """Retrieve, update, or delete a single email for a member.

    Args:
        member_pk (int):
        id (int):
        body (PatchedMemberEmail | Unset): Serializer for MemberEmail.

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
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    member_pk: int,
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMemberEmail | Unset = UNSET,
) -> MemberEmail | None:
    """Retrieve, update, or delete a single email for a member.

    Args:
        member_pk (int):
        id (int):
        body (PatchedMemberEmail | Unset): Serializer for MemberEmail.

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
            id=id,
            client=client,
            body=body,
        )
    ).parsed
