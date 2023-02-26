import asyncio
import functools
from datetime import datetime
from typing import Optional

from apiclient_pydantic import serialize_all_methods, serialize_response

from authomize.rest_api_client.client.async_base_client import AUTHOMIZE_API_URL
from authomize.rest_api_client.client.async_connectors_client import AsyncConnectorsClient
from authomize.rest_api_client.client.async_platform_client import AsyncPlatformClient
from authomize.rest_api_client.generated.connectors_rest_api.schemas import (
    BundleTransactionSchema,
    ItemsBundleSchema,
    NewAccountsAssociationResponseSchema,
    NewAccountsAssociationsListRequestSchema,
    NewAssetsInheritanceListRequestSchema,
    NewAssetsInheritanceResponseSchema,
    NewAssetsListRequestSchema,
    NewAssetsResponseSchema,
    NewGroupingResponseSchema,
    NewGroupingsAssociationResponseSchema,
    NewGroupingsAssociationsListRequestSchema,
    NewGroupingsListRequestSchema,
    NewIdentitiesListRequestSchema,
    NewIdentityResponseSchema,
    NewPermissionsListRequestSchema,
    NewPermissionsResponseSchema,
    NewPrivilegeGrantsResponseSchema,
    NewPrivilegesGrantsListRequestSchema,
    NewPrivilegesListRequestSchema,
    NewPrivilegesResponseSchema,
    NewUserResponseSchema,
    NewUsersListRequestSchema,
    RestApiConnectorListSchema,
    SearchAccountsAssociationsListResponseSchema,
    SearchAssetsInheritanceListResponseSchema,
    SearchAssetsListResponseSchema,
    SearchGroupingResponseSchema,
    SearchGroupingsAssociationsListResponseSchema,
    SearchIdentitiesListResponseSchema,
    SearchPermissionResponseSchema,
    SearchPrivilegeGrantsListResponseSchema,
    SearchPrivilegesListResponseSchema,
    SearchUsersListResponseSchema,
    SubmitResponse,
)
from authomize.rest_api_client.generated.external_rest_api.schemas import (
    IncidentExpansion,
    IsAliveResponse,
    MeResponse,
)


def syncify(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return asyncio.ensure_future(func(*args, **kwargs))

    return wrapped


@serialize_all_methods(decorator=serialize_response)
class Client:
    def __init__(
        self,
        *args,
        auth_token: str,
        base_url: str = AUTHOMIZE_API_URL,
        **kwargs,
    ):
        self.auth_token = auth_token
        self.base_url = base_url
        self.connectors_client = AsyncConnectorsClient(
            *args,
            auth_token=auth_token,
            base_url=base_url,
            **kwargs,
        )
        self.platform_client = AsyncPlatformClient(
            *args,
            auth_token=auth_token,
            base_url=base_url,
            **kwargs,
        )

    @syncify
    async def is_alive(self) -> IsAliveResponse:
        return await self.platform_client.is_alive()

    @syncify
    async def me(self) -> MeResponse:
        return await self.platform_client.me()

    @syncify
    async def list_connectors(
        self,
        params=None,
    ) -> RestApiConnectorListSchema:
        return await self.connectors_client.list_connectors(
            params=params,
        )

    @syncify
    async def create_transaction(
        self,
        connector_id: str,
    ) -> BundleTransactionSchema:
        return await self.connectors_client.create_transaction(
            connector_id=connector_id,
        )

    @syncify
    async def retrieve_transaction(
        self,
        connector_id: str,
        transaction_id: str,
    ) -> BundleTransactionSchema:
        return await self.connectors_client.retrieve_transaction(
            connector_id=connector_id,
            transaction_id=transaction_id,
        )

    @syncify
    async def apply_transaction(
        self,
        connector_id: str,
        transaction_id: str,
    ) -> BundleTransactionSchema:
        return await self.connectors_client.apply_transaction(
            connector_id=connector_id,
            transaction_id=transaction_id,
        )

    @syncify
    async def extend_transaction_items(
        self,
        connector_id: str,
        transaction_id: str,
        items: ItemsBundleSchema,
    ) -> SubmitResponse:
        return await self.connectors_client.extend_transaction_items(
            connector_id=connector_id,
            transaction_id=transaction_id,
            items=items,
        )

    @syncify
    async def delete_app_data(
        self,
        app_id: str,
        modified_before: Optional[datetime] = None,
    ) -> SubmitResponse:
        return await self.connectors_client.delete_app_data(
            app_id=app_id,
            modified_before=modified_before,
        )

    @syncify
    async def search_users(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchUsersListResponseSchema:
        return await self.connectors_client.search_users(
            app_id=app_id,
            start_date=start_date,
        )

    @syncify
    async def create_users(
        self,
        app_id: str,
        body: NewUsersListRequestSchema,
    ) -> NewUserResponseSchema:
        return await self.connectors_client.create_users(
            app_id=app_id,
            body=body,
        )

    @syncify
    async def search_groupings(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchGroupingResponseSchema:
        return await self.connectors_client.search_groupings(
            app_id=app_id,
            start_date=start_date,
        )

    @syncify
    async def create_groupings(
        self,
        app_id: str,
        body: NewGroupingsListRequestSchema,
    ) -> NewGroupingResponseSchema:
        return await self.connectors_client.create_groupings(
            app_id=app_id,
            body=body,
        )

    @syncify
    async def search_permissions(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchPermissionResponseSchema:
        return await self.connectors_client.search_permissions(
            app_id=app_id,
            start_date=start_date,
        )

    @syncify
    async def create_permissions(
        self,
        app_id: str,
        body: NewPermissionsListRequestSchema,
    ) -> NewPermissionsResponseSchema:
        return await self.connectors_client.create_permissions(
            app_id=app_id,
            body=body,
        )

    @syncify
    async def search_privileges(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchPrivilegesListResponseSchema:
        return await self.connectors_client.search_privileges(
            app_id=app_id,
            start_date=start_date,
        )

    @syncify
    async def create_privileges(
        self,
        app_id: str,
        body: NewPrivilegesListRequestSchema,
    ) -> NewPrivilegesResponseSchema:
        return await self.connectors_client.create_privileges(
            app_id=app_id,
            body=body,
        )

    @syncify
    async def search_privileges_grants(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchPrivilegeGrantsListResponseSchema:
        return await self.connectors_client.search_privileges_grants(
            app_id=app_id,
            start_date=start_date,
        )

    @syncify
    async def create_privileges_grants(
        self,
        app_id: str,
        body: NewPrivilegesGrantsListRequestSchema,
    ) -> NewPrivilegeGrantsResponseSchema:
        return await self.connectors_client.create_privileges_grants(
            app_id=app_id,
            body=body,
        )

    @syncify
    async def search_accounts_association(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchAccountsAssociationsListResponseSchema:
        return await self.connectors_client.search_accounts_association(
            app_id=app_id,
            start_date=start_date,
        )

    @syncify
    async def create_accounts_association(
        self,
        app_id: str,
        body: NewAccountsAssociationsListRequestSchema,
    ) -> NewAccountsAssociationResponseSchema:
        return await self.connectors_client.create_accounts_association(
            app_id=app_id,
            body=body,
        )

    @syncify
    async def search_groupings_association(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchGroupingsAssociationsListResponseSchema:
        return await self.connectors_client.search_groupings_association(
            app_id=app_id,
            start_date=start_date,
        )

    @syncify
    async def create_groupings_association(
        self,
        app_id: str,
        body: NewGroupingsAssociationsListRequestSchema,
    ) -> NewGroupingsAssociationResponseSchema:
        return await self.connectors_client.create_groupings_association(
            app_id=app_id,
            body=body,
        )

    @syncify
    async def search_assets(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchAssetsListResponseSchema:
        return await self.connectors_client.search_assets(
            app_id=app_id,
            start_date=start_date,
        )

    @syncify
    async def create_assets(
        self,
        app_id: str,
        body: NewAssetsListRequestSchema,
    ) -> NewAssetsResponseSchema:
        return await self.connectors_client.create_assets(
            app_id=app_id,
            body=body,
        )

    @syncify
    async def search_assets_inheritance(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchAssetsInheritanceListResponseSchema:
        return await self.connectors_client.search_assets_inheritance(
            app_id=app_id,
            start_date=start_date,
        )

    @syncify
    async def create_assets_inheritance(
        self,
        app_id: str,
        body: NewAssetsInheritanceListRequestSchema,
    ) -> NewAssetsInheritanceResponseSchema:
        return await self.connectors_client.create_assets_inheritance(
            app_id=app_id,
            body=body,
        )

    @syncify
    async def search_identities(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchIdentitiesListResponseSchema:
        return await self.connectors_client.search_identities(
            app_id=app_id,
            start_date=start_date,
        )

    @syncify
    async def create_identities(
        self,
        app_id: str,
        body: NewIdentitiesListRequestSchema,
    ) -> NewIdentityResponseSchema:
        return await self.connectors_client.create_identities(
            app_id=app_id,
            body=body,
        )

    @syncify
    async def retrieve_incident(
        self,
        incident_id: str,
        expand: Optional[list[IncidentExpansion]] = None,
    ):
        return self.platform_client.retrieve_incident(
            incident_id=incident_id,
            expand=expand,
        )

    @syncify
    async def close(self):
        await asyncio.gather(self.connectors_client.close(), self.platform_client.close())
