from datetime import datetime
from typing import Optional

from apiclient_pydantic import serialize_all_methods, serialize_response

from authomize.rest_api_client.client.base_client import AUTHOMIZE_API_URL
from authomize.rest_api_client.client.connectors_client import ConnectorsClient
from authomize.rest_api_client.client.platform_client import PlatformClient
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
        self.connectors_client = ConnectorsClient(
            *args,
            auth_token=auth_token,
            base_url=base_url,
            **kwargs,
        )
        self.platform_client = PlatformClient(
            *args,
            auth_token=auth_token,
            base_url=base_url,
            **kwargs,
        )

    def is_alive(self) -> IsAliveResponse:
        return self.platform_client.is_alive()

    def me(self) -> MeResponse:
        return self.platform_client.me()

    def list_connectors(
        self,
        params=None,
    ) -> RestApiConnectorListSchema:
        return self.connectors_client.list_connectors(
            params=params,
        )

    def create_transaction(
        self,
        connector_id: str,
    ) -> BundleTransactionSchema:
        return self.connectors_client.create_transaction(
            connector_id=connector_id,
        )

    def retrieve_transaction(
        self,
        connector_id: str,
        transaction_id: str,
    ) -> BundleTransactionSchema:
        return self.connectors_client.retrieve_transaction(
            connector_id=connector_id,
            transaction_id=transaction_id,
        )

    def apply_transaction(
        self,
        connector_id: str,
        transaction_id: str,
    ) -> BundleTransactionSchema:
        return self.connectors_client.apply_transaction(
            connector_id=connector_id,
            transaction_id=transaction_id,
        )

    def extend_transaction_items(
        self,
        connector_id: str,
        transaction_id: str,
        items: ItemsBundleSchema,
    ) -> SubmitResponse:
        return self.connectors_client.extend_transaction_items(
            connector_id=connector_id,
            transaction_id=transaction_id,
            items=items,
        )

    def delete_app_data(
        self,
        app_id: str,
        modified_before: Optional[datetime] = None,
    ) -> SubmitResponse:
        return self.connectors_client.delete_app_data(
            app_id=app_id,
            modified_before=modified_before,
        )

    def search_users(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchUsersListResponseSchema:
        return self.connectors_client.search_users(
            app_id=app_id,
            start_date=start_date,
        )

    def create_users(
        self,
        app_id: str,
        body: NewUsersListRequestSchema,
    ) -> NewUserResponseSchema:
        return self.connectors_client.create_users(
            app_id=app_id,
            body=body,
        )

    def search_groupings(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchGroupingResponseSchema:
        return self.connectors_client.search_groupings(
            app_id=app_id,
            start_date=start_date,
        )

    def create_groupings(
        self,
        app_id: str,
        body: NewGroupingsListRequestSchema,
    ) -> NewGroupingResponseSchema:
        return self.connectors_client.create_groupings(
            app_id=app_id,
            body=body,
        )

    def search_permissions(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchPermissionResponseSchema:
        return self.connectors_client.search_permissions(
            app_id=app_id,
            start_date=start_date,
        )

    def create_permissions(
        self,
        app_id: str,
        body: NewPermissionsListRequestSchema,
    ) -> NewPermissionsResponseSchema:
        return self.connectors_client.create_permissions(
            app_id=app_id,
            body=body,
        )

    def search_privileges(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchPrivilegesListResponseSchema:
        return self.connectors_client.search_privileges(
            app_id=app_id,
            start_date=start_date,
        )

    def create_privileges(
        self,
        app_id: str,
        body: NewPrivilegesListRequestSchema,
    ) -> NewPrivilegesResponseSchema:
        return self.connectors_client.create_privileges(
            app_id=app_id,
            body=body,
        )

    def search_privileges_grants(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchPrivilegeGrantsListResponseSchema:
        return self.connectors_client.search_privileges_grants(
            app_id=app_id,
            start_date=start_date,
        )

    def create_privileges_grants(
        self,
        app_id: str,
        body: NewPrivilegesGrantsListRequestSchema,
    ) -> NewPrivilegeGrantsResponseSchema:
        return self.connectors_client.create_privileges_grants(
            app_id=app_id,
            body=body,
        )

    def search_accounts_association(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchAccountsAssociationsListResponseSchema:
        return self.connectors_client.search_accounts_association(
            app_id=app_id,
            start_date=start_date,
        )

    def create_accounts_association(
        self,
        app_id: str,
        body: NewAccountsAssociationsListRequestSchema,
    ) -> NewAccountsAssociationResponseSchema:
        return self.connectors_client.create_accounts_association(
            app_id=app_id,
            body=body,
        )

    def search_groupings_association(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchGroupingsAssociationsListResponseSchema:
        return self.connectors_client.search_groupings_association(
            app_id=app_id,
            start_date=start_date,
        )

    def create_groupings_association(
        self,
        app_id: str,
        body: NewGroupingsAssociationsListRequestSchema,
    ) -> NewGroupingsAssociationResponseSchema:
        return self.connectors_client.create_groupings_association(
            app_id=app_id,
            body=body,
        )

    def search_assets(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchAssetsListResponseSchema:
        return self.connectors_client.search_assets(
            app_id=app_id,
            start_date=start_date,
        )

    def create_assets(
        self,
        app_id: str,
        body: NewAssetsListRequestSchema,
    ) -> NewAssetsResponseSchema:
        return self.connectors_client.create_assets(
            app_id=app_id,
            body=body,
        )

    def search_assets_inheritance(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchAssetsInheritanceListResponseSchema:
        return self.connectors_client.search_assets_inheritance(
            app_id=app_id,
            start_date=start_date,
        )

    def create_assets_inheritance(
        self,
        app_id: str,
        body: NewAssetsInheritanceListRequestSchema,
    ) -> NewAssetsInheritanceResponseSchema:
        return self.connectors_client.create_assets_inheritance(
            app_id=app_id,
            body=body,
        )

    def search_identities(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchIdentitiesListResponseSchema:
        return self.connectors_client.search_identities(
            app_id=app_id,
            start_date=start_date,
        )

    def create_identities(
        self,
        app_id: str,
        body: NewIdentitiesListRequestSchema,
    ) -> NewIdentityResponseSchema:
        return self.connectors_client.create_identities(
            app_id=app_id,
            body=body,
        )

    def retrieve_incident(
        self,
        incident_id: str,
        expand: Optional[list[IncidentExpansion]] = None,
    ):
        return self.platform_client.retrieve_incident(
            incident_id=incident_id,
            expand=expand,
        )
