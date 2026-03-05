from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_address import MemberAddress
from ...types import Response


def _get_kwargs(
    member_pk: int,
    *,
    body: MemberAddress,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/members/member/{member_pk}/addresses/".format(
            member_pk=quote(str(member_pk), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MemberAddress | None:
    if response.status_code == 201:
        response_201 = MemberAddress.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: MemberAddress,
) -> Response[MemberAddress]:
    """List all addresses for a member, or add a new one.

    A member can have at most one residence and one domicilio
    (enforced by DB constraint).
    For Italian addresses, region/province/comune/postal_code/street/street_number
    are all required. For foreign addresses, only foreign_address is required.

    Args:
        member_pk (int):
        body (MemberAddress): Serializer for MemberAddress.

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
    body: MemberAddress,
) -> MemberAddress | None:
    """List all addresses for a member, or add a new one.

    A member can have at most one residence and one domicilio
    (enforced by DB constraint).
    For Italian addresses, region/province/comune/postal_code/street/street_number
    are all required. For foreign addresses, only foreign_address is required.

    Args:
        member_pk (int):
        body (MemberAddress): Serializer for MemberAddress.

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
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    member_pk: int,
    *,
    client: AuthenticatedClient,
    body: MemberAddress,
) -> Response[MemberAddress]:
    """List all addresses for a member, or add a new one.

    A member can have at most one residence and one domicilio
    (enforced by DB constraint).
    For Italian addresses, region/province/comune/postal_code/street/street_number
    are all required. For foreign addresses, only foreign_address is required.

    Args:
        member_pk (int):
        body (MemberAddress): Serializer for MemberAddress.

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
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    member_pk: int,
    *,
    client: AuthenticatedClient,
    body: MemberAddress,
) -> MemberAddress | None:
    """List all addresses for a member, or add a new one.

    A member can have at most one residence and one domicilio
    (enforced by DB constraint).
    For Italian addresses, region/province/comune/postal_code/street/street_number
    are all required. For foreign addresses, only foreign_address is required.

    Args:
        member_pk (int):
        body (MemberAddress): Serializer for MemberAddress.

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
            client=client,
            body=body,
        )
    ).parsed
