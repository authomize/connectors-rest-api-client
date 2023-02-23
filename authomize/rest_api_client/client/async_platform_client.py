from typing import Optional

from authomize.rest_api_client.client.async_base_client import AsyncBaseClient
from authomize.rest_api_client.generated.external_rest_api.schemas import (
    IncidentExpansion,
    IsAliveResponse,
    MeResponse,
    NonPaginatedResponseSchemaIncidentSchema,
)


class AsyncPlatformClient(AsyncBaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def authorization_header(self) -> str:
        return f'Bearer {self.auth_token}'

    async def is_alive(self) -> IsAliveResponse:
        return await self.http_get('/is_alive')

    async def me(self) -> MeResponse:
        return await self.http_get('/me')

    async def retrieve_incident(
        self,
        incident_id: str,
        expand: Optional[list[IncidentExpansion]] = None,
    ) -> NonPaginatedResponseSchemaIncidentSchema:
        if not incident_id:
            raise ValueError('Missing incident_id')
        params = None
        if expand:
            params = dict(
                expand=expand,
            )
        return await self.http_get(f'/v2/incidents/{incident_id}', params=params)
