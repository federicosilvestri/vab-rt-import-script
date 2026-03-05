from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_member_abilitazione_list import PaginatedMemberAbilitazioneList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    member_pk: int,
    *,
    page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/members/member/{member_pk}/abilitazioni/".format(
            member_pk=quote(str(member_pk), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedMemberAbilitazioneList | None:
    if response.status_code == 200:
        response_200 = PaginatedMemberAbilitazioneList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedMemberAbilitazioneList]:
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
    page: int | Unset = UNSET,
) -> Response[PaginatedMemberAbilitazioneList]:
    """List all abilitazioni assigned to a member, or assign a new one.

    For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
    expires_at are required. This is enforced by the model's clean().

    Args:
        member_pk (int):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMemberAbilitazioneList]
    """

    kwargs = _get_kwargs(
        member_pk=member_pk,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    member_pk: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
) -> PaginatedMemberAbilitazioneList | None:
    """List all abilitazioni assigned to a member, or assign a new one.

    For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
    expires_at are required. This is enforced by the model's clean().

    Args:
        member_pk (int):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMemberAbilitazioneList
    """

    return sync_detailed(
        member_pk=member_pk,
        client=client,
        page=page,
    ).parsed


async def asyncio_detailed(
    member_pk: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
) -> Response[PaginatedMemberAbilitazioneList]:
    """List all abilitazioni assigned to a member, or assign a new one.

    For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
    expires_at are required. This is enforced by the model's clean().

    Args:
        member_pk (int):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMemberAbilitazioneList]
    """

    kwargs = _get_kwargs(
        member_pk=member_pk,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    member_pk: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
) -> PaginatedMemberAbilitazioneList | None:
    """List all abilitazioni assigned to a member, or assign a new one.

    For non-internal sources (CORSO_EXT, TITOLO, ALTRO), issued_at and
    expires_at are required. This is enforced by the model's clean().

    Args:
        member_pk (int):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMemberAbilitazioneList
    """

    return (
        await asyncio_detailed(
            member_pk=member_pk,
            client=client,
            page=page,
        )
    ).parsed
