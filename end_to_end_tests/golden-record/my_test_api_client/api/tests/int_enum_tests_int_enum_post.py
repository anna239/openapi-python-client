from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.an_int_enum import AnIntEnum
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    int_enum: AnIntEnum,
) -> Dict[str, Any]:
    url = "{}/tests/int_enum".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_int_enum = int_enum.value

    params: Dict[str, Any] = {
        "int_enum": json_int_enum,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    int_enum: AnIntEnum,
) -> Response[Union[Any, HTTPValidationError]]:
    kwargs = _get_kwargs(
        client=client,
        int_enum=int_enum,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    int_enum: AnIntEnum,
) -> Optional[Union[Any, HTTPValidationError]]:
    """ """

    return sync_detailed(
        client=client,
        int_enum=int_enum,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    int_enum: AnIntEnum,
) -> Response[Union[Any, HTTPValidationError]]:
    kwargs = _get_kwargs(
        client=client,
        int_enum=int_enum,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    int_enum: AnIntEnum,
) -> Optional[Union[Any, HTTPValidationError]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            int_enum=int_enum,
        )
    ).parsed
