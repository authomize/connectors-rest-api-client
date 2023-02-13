from typing import Optional

from authomize.rest_api_client.client.base_client import BaseClient
from authomize.rest_api_client.generated.external_rest_api.schemas import (
    IncidentExpansion,
    IsAliveResponse,
    MeResponse,
    NonPaginatedResponseSchemaIncidentSchema,
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

    def retrieve_incident(
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
        return self.http_get(f'/v2/incidents/{incident_id}', params=params)
