from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_address import MemberAddress
from ...models.patched_member_address import PatchedMemberAddress
from ...types import UNSET, Response, Unset


def _get_kwargs(
    member_pk: int,
    id: int,
    *,
    body: PatchedMemberAddress | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/members/member/{member_pk}/addresses/{id}/".format(
            member_pk=quote(str(member_pk), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MemberAddress | None:
    if response.status_code == 200:
        response_200 = MemberAddress.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MemberAddress]:
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
    body: PatchedMemberAddress | Unset = UNSET,
) -> Response[MemberAddress]:
    """Retrieve, update, or delete a single address for a member.

    Args:
        member_pk (int):
        id (int):
        body (PatchedMemberAddress | Unset): Serializer for MemberAddress.

            Italian addresses require region/province/comune/postal_code/street/street_number.
            Foreign addresses only require country + foreign_address.
            The model's clean() method handles autofill and cross-field validation.

            The 'point' (geospatial) field is intentionally excluded: it is auto-computed
            and not meant to be set or displayed directly via the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberAddress]
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
    body: PatchedMemberAddress | Unset = UNSET,
) -> MemberAddress | None:
    """Retrieve, update, or delete a single address for a member.

    Args:
        member_pk (int):
        id (int):
        body (PatchedMemberAddress | Unset): Serializer for MemberAddress.

            Italian addresses require region/province/comune/postal_code/street/street_number.
            Foreign addresses only require country + foreign_address.
            The model's clean() method handles autofill and cross-field validation.

            The 'point' (geospatial) field is intentionally excluded: it is auto-computed
            and not meant to be set or displayed directly via the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberAddress
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
    body: PatchedMemberAddress | Unset = UNSET,
) -> Response[MemberAddress]:
    """Retrieve, update, or delete a single address for a member.

    Args:
        member_pk (int):
        id (int):
        body (PatchedMemberAddress | Unset): Serializer for MemberAddress.

            Italian addresses require region/province/comune/postal_code/street/street_number.
            Foreign addresses only require country + foreign_address.
            The model's clean() method handles autofill and cross-field validation.

            The 'point' (geospatial) field is intentionally excluded: it is auto-computed
            and not meant to be set or displayed directly via the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberAddress]
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
    body: PatchedMemberAddress | Unset = UNSET,
) -> MemberAddress | None:
    """Retrieve, update, or delete a single address for a member.

    Args:
        member_pk (int):
        id (int):
        body (PatchedMemberAddress | Unset): Serializer for MemberAddress.

            Italian addresses require region/province/comune/postal_code/street/street_number.
            Foreign addresses only require country + foreign_address.
            The model's clean() method handles autofill and cross-field validation.

            The 'point' (geospatial) field is intentionally excluded: it is auto-computed
            and not meant to be set or displayed directly via the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberAddress
    """

    return (
        await asyncio_detailed(
            member_pk=member_pk,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
