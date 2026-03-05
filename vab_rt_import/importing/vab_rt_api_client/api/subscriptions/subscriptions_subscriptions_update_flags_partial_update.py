from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_subscription import PatchedSubscription
from ...models.subscription import Subscription
from ...types import UNSET, Response, Unset


def _get_kwargs(
    n_tessera: int,
    *,
    body: PatchedSubscription | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/subscriptions/subscriptions/{n_tessera}/update-flags/".format(
            n_tessera=quote(str(n_tessera), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Subscription | None:
    if response.status_code == 200:
        response_200 = Subscription.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Subscription]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    n_tessera: int,
    *,
    client: AuthenticatedClient,
    body: PatchedSubscription | Unset = UNSET,
) -> Response[Subscription]:
    """
    Args:
        n_tessera (int):
        body (PatchedSubscription | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscription]
    """

    kwargs = _get_kwargs(
        n_tessera=n_tessera,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    n_tessera: int,
    *,
    client: AuthenticatedClient,
    body: PatchedSubscription | Unset = UNSET,
) -> Subscription | None:
    """
    Args:
        n_tessera (int):
        body (PatchedSubscription | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscription
    """

    return sync_detailed(
        n_tessera=n_tessera,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    n_tessera: int,
    *,
    client: AuthenticatedClient,
    body: PatchedSubscription | Unset = UNSET,
) -> Response[Subscription]:
    """
    Args:
        n_tessera (int):
        body (PatchedSubscription | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscription]
    """

    kwargs = _get_kwargs(
        n_tessera=n_tessera,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    n_tessera: int,
    *,
    client: AuthenticatedClient,
    body: PatchedSubscription | Unset = UNSET,
) -> Subscription | None:
    """
    Args:
        n_tessera (int):
        body (PatchedSubscription | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscription
    """

    return (
        await asyncio_detailed(
            n_tessera=n_tessera,
            client=client,
            body=body,
        )
    ).parsed
