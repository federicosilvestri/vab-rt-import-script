from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_cie_document import MemberCIEDocument
from ...types import Response


def _get_kwargs(
    member_pk: int,
    id: int,
    *,
    body: MemberCIEDocument,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/members/member/{member_pk}/cie/{id}/".format(
            member_pk=quote(str(member_pk), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MemberCIEDocument | None:
    if response.status_code == 200:
        response_200 = MemberCIEDocument.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MemberCIEDocument]:
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
    body: MemberCIEDocument,
) -> Response[MemberCIEDocument]:
    """Retrieve, update, or delete a single CIE document.

    Args:
        member_pk (int):
        id (int):
        body (MemberCIEDocument): Serializer for MemberCIEDocument (Carta di Identità
            Elettronica).

            - is_valid is a computed property exposed as read-only.
            - document is a PDF file upload field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberCIEDocument]
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
    body: MemberCIEDocument,
) -> MemberCIEDocument | None:
    """Retrieve, update, or delete a single CIE document.

    Args:
        member_pk (int):
        id (int):
        body (MemberCIEDocument): Serializer for MemberCIEDocument (Carta di Identità
            Elettronica).

            - is_valid is a computed property exposed as read-only.
            - document is a PDF file upload field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberCIEDocument
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
    body: MemberCIEDocument,
) -> Response[MemberCIEDocument]:
    """Retrieve, update, or delete a single CIE document.

    Args:
        member_pk (int):
        id (int):
        body (MemberCIEDocument): Serializer for MemberCIEDocument (Carta di Identità
            Elettronica).

            - is_valid is a computed property exposed as read-only.
            - document is a PDF file upload field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberCIEDocument]
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
    body: MemberCIEDocument,
) -> MemberCIEDocument | None:
    """Retrieve, update, or delete a single CIE document.

    Args:
        member_pk (int):
        id (int):
        body (MemberCIEDocument): Serializer for MemberCIEDocument (Carta di Identità
            Elettronica).

            - is_valid is a computed property exposed as read-only.
            - document is a PDF file upload field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberCIEDocument
    """

    return (
        await asyncio_detailed(
            member_pk=member_pk,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
