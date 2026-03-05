from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auth_user import AuthUser
from ...models.patched_auth_user import PatchedAuthUser
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchedAuthUser | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/users/me/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuthUser | None:
    if response.status_code == 200:
        response_200 = AuthUser.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuthUser]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PatchedAuthUser | Unset = UNSET,
) -> Response[AuthUser]:
    """Retrieve or partially update the currently authenticated user's profile.

    The response is polymorphic: the serializer is chosen based on the user type
    (MemberUser, ExternalUser, or base AuthUser), so Angular does not need to
    know the user type before calling this endpoint.

    Args:
        body (PatchedAuthUser | Unset): Base serializer - read only, generic replies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthUser]
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
    body: PatchedAuthUser | Unset = UNSET,
) -> AuthUser | None:
    """Retrieve or partially update the currently authenticated user's profile.

    The response is polymorphic: the serializer is chosen based on the user type
    (MemberUser, ExternalUser, or base AuthUser), so Angular does not need to
    know the user type before calling this endpoint.

    Args:
        body (PatchedAuthUser | Unset): Base serializer - read only, generic replies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthUser
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PatchedAuthUser | Unset = UNSET,
) -> Response[AuthUser]:
    """Retrieve or partially update the currently authenticated user's profile.

    The response is polymorphic: the serializer is chosen based on the user type
    (MemberUser, ExternalUser, or base AuthUser), so Angular does not need to
    know the user type before calling this endpoint.

    Args:
        body (PatchedAuthUser | Unset): Base serializer - read only, generic replies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthUser]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PatchedAuthUser | Unset = UNSET,
) -> AuthUser | None:
    """Retrieve or partially update the currently authenticated user's profile.

    The response is polymorphic: the serializer is chosen based on the user type
    (MemberUser, ExternalUser, or base AuthUser), so Angular does not need to
    know the user type before calling this endpoint.

    Args:
        body (PatchedAuthUser | Unset): Base serializer - read only, generic replies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthUser
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
