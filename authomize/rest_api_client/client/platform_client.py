from authomize.rest_api_client.client.base_client import BaseClient
from authomize.rest_api_client.generated.external_rest_api.schemas import (
    IsAliveResponse,
    MeResponse,
)


class PlatformClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def authorization_header(self) -> str:
        return f'Bearer {self.auth_token}'

    def is_alive(self) -> IsAliveResponse:
        return self.http_get('/is_alive')

    def me(self) -> MeResponse:
        return self.http_get('/me')
