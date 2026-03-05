from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualifica import Qualifica
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Qualifica | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/members/qualifiche/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Qualifica | None:
    if response.status_code == 201:
        response_201 = Qualifica.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Qualifica]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Qualifica | Unset = UNSET,
) -> Response[Qualifica]:
    """List all available Qualifiche, or create a new one.

    Args:
        body (Qualifica | Unset): Read-only lookup serializer for Qualifica.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Qualifica]
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
    body: Qualifica | Unset = UNSET,
) -> Qualifica | None:
    """List all available Qualifiche, or create a new one.

    Args:
        body (Qualifica | Unset): Read-only lookup serializer for Qualifica.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Qualifica
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Qualifica | Unset = UNSET,
) -> Response[Qualifica]:
    """List all available Qualifiche, or create a new one.

    Args:
        body (Qualifica | Unset): Read-only lookup serializer for Qualifica.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Qualifica]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Qualifica | Unset = UNSET,
) -> Qualifica | None:
    """List all available Qualifiche, or create a new one.

    Args:
        body (Qualifica | Unset): Read-only lookup serializer for Qualifica.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Qualifica
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
