from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_member_job_list import PaginatedMemberJobList
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
        "url": "/api/members/member/{member_pk}/jobs/".format(
            member_pk=quote(str(member_pk), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedMemberJobList | None:
    if response.status_code == 200:
        response_200 = PaginatedMemberJobList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedMemberJobList]:
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
) -> Response[PaginatedMemberJobList]:
    """List all jobs for a member, or add a new one.

    company_detail is returned nested for display; use company (FK id) to write.

    Args:
        member_pk (int):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMemberJobList]
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
) -> PaginatedMemberJobList | None:
    """List all jobs for a member, or add a new one.

    company_detail is returned nested for display; use company (FK id) to write.

    Args:
        member_pk (int):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMemberJobList
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
) -> Response[PaginatedMemberJobList]:
    """List all jobs for a member, or add a new one.

    company_detail is returned nested for display; use company (FK id) to write.

    Args:
        member_pk (int):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMemberJobList]
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
) -> PaginatedMemberJobList | None:
    """List all jobs for a member, or add a new one.

    company_detail is returned nested for display; use company (FK id) to write.

    Args:
        member_pk (int):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMemberJobList
    """

    return (
        await asyncio_detailed(
            member_pk=member_pk,
            client=client,
            page=page,
        )
    ).parsed
