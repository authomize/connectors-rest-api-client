from typing import Optional

from authomize.rest_api_client.client.base_client import BaseClient
from authomize.rest_api_client.generated.external_rest_api.schemas import (
    CampaignExpansion,
    CreateCampaignRequestSchema,
    CreateCampaignResponseSchema,
    IncidentExpansion,
    IsAliveResponse,
    MeResponse,
    NonPaginatedResponseSchemaCampaignSchema,
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

    def create_campaign(
        self,
        body: CreateCampaignRequestSchema,
    ) -> CreateCampaignResponseSchema:
        return self.http_post(
            '/v2/campaigns',
            body=body.json(),
        )

    def retrieve_campaign(
        self, campaign_id: str, expand: Optional[list[CampaignExpansion]] = None
    ) -> NonPaginatedResponseSchemaCampaignSchema:
        if not campaign_id:
            raise ValueError('Missing campaign_id')
        params = None
        if expand:
            params = dict(
                expand=expand,
            )
        return self.http_get(f'/v2/campaigns/{campaign_id}', params=params)
