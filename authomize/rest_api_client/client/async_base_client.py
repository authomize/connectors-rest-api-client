from typing import Optional

import aiohttp
from aiohttp import ClientResponse

AUTHOMIZE_API_URL = 'https://api.authomize.com'
STATUS_OK: int = 200


class AsyncClientError(Exception):
    def __init__(self, message):
        self.message = message


class AsyncBaseClient:
    def __init__(self, auth_token: str, base_url: str = AUTHOMIZE_API_URL):
        self.auth_token = auth_token
        self.base_url = base_url
        self.session = aiohttp.ClientSession()
        self.session.headers.update({'Authorization': self.authorization_header})

    @property
    def authorization_header(self) -> str:
        raise NotImplementedError()

    async def http_get(self, url, params=None):
        url = self.base_url + url
        response: ClientResponse = await self.session.get(url, params=params)
        if response.status == STATUS_OK:
            return response.json()
        try:
            response_json = await response.json()
            detail = response_json.get('detail')
        except Exception:
            detail = None
        if detail:
            raise AsyncClientError(str(detail))
        response.raise_for_status()

    async def http_post(self, url: str, body: Optional[str] = None):
        url = self.base_url + url
        response = await self.session.post(
            url,
            headers={'Content-Type': 'application/json'},
            data=body,
        )
        if response.status == STATUS_OK:
            return await response.json()
        try:
            response_json = await response.json()
            detail = response_json.get('detail')
        except Exception:
            detail = None
        if detail:
            raise AsyncClientError(str(detail))
        response.raise_for_status()

    async def http_delete(self, url: str, params=None):
        url = self.base_url + url
        response = await self.session.delete(url, params=params)
        if response.status == STATUS_OK:
            return await response.json()
        try:
            response_json = await response.json()
            detail = response_json.get('detail')
        except Exception:
            detail = None
        if detail:
            raise AsyncClientError(str(detail))
        response.raise_for_status()
