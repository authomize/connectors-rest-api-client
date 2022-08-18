import json

from apiclient_pydantic import serialize_all_methods, serialize_response
from pydantic.json import pydantic_encoder

from authomize.rest_api_client.client.base_client import BaseClient
from authomize.rest_api_client.generated.schemas import (
    BundleTransactionSchema,
    IsAliveResponse,
    ItemsBundleSchema,
    MeResponse,
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
    SubmitResponse,
)


@serialize_all_methods(decorator=serialize_response)
class Client(BaseClient):
    def is_alive(self) -> IsAliveResponse:
        return self.http_get('/is_alive')

    def me(self) -> MeResponse:
        return self.http_get('/me')

    def list_connectors(
        self,
        params=None,
    ) -> RestApiConnectorListSchema:
        return self.http_get('/v1/connectors', params=params)

    def create_transaction(
        self,
        connector_id: str,
    ) -> BundleTransactionSchema:
        if not connector_id:
            raise ValueError('Missing connector_id')
        return self.http_post(f'/v1/connectors/{connector_id}/transactions')

    def retrieve_transaction(
        self,
        connector_id: str,
        transaction_id: str,
    ) -> BundleTransactionSchema:
        if not connector_id:
            raise ValueError('Missing connector_id')
        if not transaction_id:
            raise ValueError('Missing transaction_id')
        return self.http_get(f'/v1/connectors/{connector_id}/transactions/{transaction_id}')

    def apply_transaction(
        self,
        connector_id: str,
        transaction_id: str,
    ) -> BundleTransactionSchema:
        if not connector_id:
            raise ValueError('Missing connector_id')
        if not transaction_id:
            raise ValueError('Missing transaction_id')
        return self.http_post(f'/v1/connectors/{connector_id}/transactions/{transaction_id}/apply')

    def extend_transaction_items(
        self,
        connector_id: str,
        transaction_id: str,
        items: ItemsBundleSchema,
    ) -> SubmitResponse:
        if not connector_id:
            raise ValueError('Missing connector_id')
        if not transaction_id:
            raise ValueError('Missing transaction_id')
        return self.http_post(
            f'/v1/connectors/{connector_id}/transactions/{transaction_id}/items',
            body=items.json(),
        )

    def delete_app_data(
        self,
        app_id: str,
    ) -> SubmitResponse:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_delete(url=f'/v2/apps/{app_id}/data')

    def create_users(
        self,
        app_id: str,
        body: NewUsersListRequestSchema,
    ) -> NewUserResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(
            url=f'/v2/apps/{app_id}/accounts/users',
            body=json.dumps(
                body,
                default=pydantic_encoder,
            ),
        )

    def create_groupings(
        self,
        app_id: str,
        body: NewGroupingsListRequestSchema,
    ) -> NewGroupingResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(
            url=f'/v2/apps/{app_id}/access/grouping',
            body=json.dumps(
                body,
                default=pydantic_encoder,
            ),
        )

    def create_permissions(
        self,
        app_id: str,
        body: NewPermissionsListRequestSchema,
    ) -> NewPermissionsResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(
            url=f'/v2/apps/{app_id}/access/permissions',
            body=json.dumps(
                body,
                default=pydantic_encoder,
            ),
        )

    def create_privileges(
        self,
        app_id: str,
        body: NewPrivilegesListRequestSchema,
    ) -> NewPrivilegesResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(
            url=f'/v2/apps/{app_id}/privileges',
            body=json.dumps(
                body,
                default=pydantic_encoder,
            ),
        )

    def create_privileges_grants(
        self,
        app_id: str,
        body: NewPrivilegesGrantsListRequestSchema,
    ) -> NewPrivilegeGrantsResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(
            url=f'/v2/apps/{app_id}/privileges/grants',
            body=json.dumps(
                body,
                default=pydantic_encoder,
            ),
        )

    def create_accounts_association(
        self,
        app_id: str,
        body: NewAccountsAssociationsListRequestSchema,
    ) -> NewAccountsAssociationResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(
            url=f'/v2/apps/{app_id}/association/accounts',
            body=json.dumps(
                body,
                default=pydantic_encoder,
            ),
        )

    def create_groupings_association(
        self,
        app_id: str,
        body: NewGroupingsAssociationsListRequestSchema,
    ) -> NewGroupingsAssociationResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(
            url=f'/v2/apps/{app_id}/association/groupings',
            body=json.dumps(
                body,
                default=pydantic_encoder,
            ),
        )

    def create_assets(
        self,
        app_id: str,
        body: NewAssetsListRequestSchema,
    ) -> NewAssetsResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(
            url=f'/v2/apps/{app_id}/assets',
            body=json.dumps(
                body,
                default=pydantic_encoder,
            ),
        )

    def create_assets_inheritance(
        self,
        app_id: str,
        body: NewAssetsInheritanceListRequestSchema,
    ) -> NewAssetsInheritanceResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(
            url=f'/v2/apps/{app_id}/assets/inheritance',
            body=json.dumps(
                body,
                default=pydantic_encoder,
            ),
        )

    def create_identities(
        self,
        app_id: str,
        body: NewIdentitiesListRequestSchema,
    ) -> NewIdentityResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(
            url=f'/v2/apps/{app_id}/identities',
            body=json.dumps(
                body,
                default=pydantic_encoder,
            ),
        )
