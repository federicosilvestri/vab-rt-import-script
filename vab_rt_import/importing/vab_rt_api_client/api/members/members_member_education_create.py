from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_education import MemberEducation
from ...types import Response


def _get_kwargs(
    member_pk: int,
    *,
    body: MemberEducation,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/members/member/{member_pk}/education/".format(
            member_pk=quote(str(member_pk), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MemberEducation | None:
    if response.status_code == 201:
        response_201 = MemberEducation.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MemberEducation]:
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
    body: MemberEducation,
) -> Response[MemberEducation]:
    """List all education records for a member, or add a new one.

    Specialization is required for university-level education types.

    Args:
        member_pk (int):
        body (MemberEducation): Serializer for MemberEducation.

            Specialization is required for university-level education types.
            The model's clean() validates this constraint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberEducation]
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
    body: MemberEducation,
) -> MemberEducation | None:
    """List all education records for a member, or add a new one.

    Specialization is required for university-level education types.

    Args:
        member_pk (int):
        body (MemberEducation): Serializer for MemberEducation.

            Specialization is required for university-level education types.
            The model's clean() validates this constraint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberEducation
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
    body: MemberEducation,
) -> Response[MemberEducation]:
    """List all education records for a member, or add a new one.

    Specialization is required for university-level education types.

    Args:
        member_pk (int):
        body (MemberEducation): Serializer for MemberEducation.

            Specialization is required for university-level education types.
            The model's clean() validates this constraint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberEducation]
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
    body: MemberEducation,
) -> MemberEducation | None:
    """List all education records for a member, or add a new one.

    Specialization is required for university-level education types.

    Args:
        member_pk (int):
        body (MemberEducation): Serializer for MemberEducation.

            Specialization is required for university-level education types.
            The model's clean() validates this constraint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberEducation
    """

    return (
        await asyncio_detailed(
            member_pk=member_pk,
            client=client,
            body=body,
        )
    ).parsed
