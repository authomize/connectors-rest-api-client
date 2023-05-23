from typing import Optional

import requests
from requests import Response

AUTHOMIZE_API_URL = 'https://api.authomize.com'


class ClientError(Exception):
    def __init__(self, message):
        self.message = message


class BaseClient:
    def __init__(self, auth_token: str, base_url: str = AUTHOMIZE_API_URL):
        self.auth_token = auth_token
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'Authorization': self.authorization_header})

    @property
    def authorization_header(self) -> str:
        raise NotImplementedError()

    @staticmethod
    def _handle_response(response: Response):
        if response.ok:
            return BaseClient._handle_ok_response(response)
        try:
            response_json = response.json()
            detail = response_json.get('detail')
            if 400 <= response.status_code < 500:
                response.reason = response.text
        except Exception:
            detail = None
        if detail:
            raise ClientError(str(detail))
        response.raise_for_status()

    @staticmethod
    def _handle_ok_response(response: Response) -> dict:
        if content_type := response.headers.get('content-type'):
            if content_type.startswith('application/json'):
                return response.json()

        raise ClientError(
            message={
                'status_code': response.status_code,
                'url': response.url,
                'message': 'Unexpected response from API',
                'raw': response.content,
            }
        )

    def http_get(self, url, params=None):
        url = self.base_url + url
        response = self.session.get(url, params=params)
        self._handle_response(response)

    def http_post(self, url: str, body: Optional[str] = None):
        url = self.base_url + url
        response = self.session.post(
            url,
            headers={'Content-Type': 'application/json'},
            data=body,
        )
        self._handle_response(response)

    def http_patch(self, url: str, body: Optional[str] = None):
        url = self.base_url + url
        response = self.session.patch(
            url,
            headers={'Content-Type': 'application/json'},
            data=body,
        )
        self._handle_response(response)

    def http_delete(self, url: str, params=None):
        url = self.base_url + url
        response = self.session.delete(url, params=params)
        self._handle_response(response)
