from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_password import ChangePassword
from ...types import Response


def _get_kwargs(
    *,
    body: ChangePassword,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/users/change-password/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChangePassword | None:
    if response.status_code == 200:
        response_200 = ChangePassword.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChangePassword]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ChangePassword,
) -> Response[ChangePassword]:
    """Change the password for the currently authenticated user.

    After a successful password change, new JWT tokens are issued immediately
    so the Angular client does not need to perform a separate login request.
    Old tokens remain valid until expiry; issuing new ones here ensures a
    smooth UX without a security gap on the client side.

    Args:
        body (ChangePassword): Change password serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangePassword]
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
    body: ChangePassword,
) -> ChangePassword | None:
    """Change the password for the currently authenticated user.

    After a successful password change, new JWT tokens are issued immediately
    so the Angular client does not need to perform a separate login request.
    Old tokens remain valid until expiry; issuing new ones here ensures a
    smooth UX without a security gap on the client side.

    Args:
        body (ChangePassword): Change password serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangePassword
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ChangePassword,
) -> Response[ChangePassword]:
    """Change the password for the currently authenticated user.

    After a successful password change, new JWT tokens are issued immediately
    so the Angular client does not need to perform a separate login request.
    Old tokens remain valid until expiry; issuing new ones here ensures a
    smooth UX without a security gap on the client side.

    Args:
        body (ChangePassword): Change password serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangePassword]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ChangePassword,
) -> ChangePassword | None:
    """Change the password for the currently authenticated user.

    After a successful password change, new JWT tokens are issued immediately
    so the Angular client does not need to perform a separate login request.
    Old tokens remain valid until expiry; issuing new ones here ensures a
    smooth UX without a security gap on the client side.

    Args:
        body (ChangePassword): Change password serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangePassword
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
