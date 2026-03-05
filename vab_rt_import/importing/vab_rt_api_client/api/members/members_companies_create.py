from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company import Company
from ...types import Response


def _get_kwargs(
    *,
    body: Company,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/members/companies/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Company | None:
    if response.status_code == 201:
        response_201 = Company.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Company]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Company,
) -> Response[Company]:
    """List all companies or create a new one.

    Companies are a global registry shared across members' jobs.
    Not scoped to a specific member.

    Args:
        body (Company): Serializer for Company (employer).

            Handles both Italian and foreign legal addresses.
            The model's clean() method enforces conditional validation
            (Italian fields vs foreign_address).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Company]
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
    body: Company,
) -> Company | None:
    """List all companies or create a new one.

    Companies are a global registry shared across members' jobs.
    Not scoped to a specific member.

    Args:
        body (Company): Serializer for Company (employer).

            Handles both Italian and foreign legal addresses.
            The model's clean() method enforces conditional validation
            (Italian fields vs foreign_address).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Company
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Company,
) -> Response[Company]:
    """List all companies or create a new one.

    Companies are a global registry shared across members' jobs.
    Not scoped to a specific member.

    Args:
        body (Company): Serializer for Company (employer).

            Handles both Italian and foreign legal addresses.
            The model's clean() method enforces conditional validation
            (Italian fields vs foreign_address).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Company]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Company,
) -> Company | None:
    """List all companies or create a new one.

    Companies are a global registry shared across members' jobs.
    Not scoped to a specific member.

    Args:
        body (Company): Serializer for Company (employer).

            Handles both Italian and foreign legal addresses.
            The model's clean() method enforces conditional validation
            (Italian fields vs foreign_address).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Company
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
