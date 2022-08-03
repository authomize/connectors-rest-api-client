import json

from apiclient_pydantic import serialize_all_methods, serialize_response

from authomize.rest_api_client.client.base_client import BaseClient
from authomize.rest_api_client.generated.schemas import (
    BundleTransactionSchema,
    IsAliveResponse,
    ItemsBundleSchema,
    MeResponse,
    NewAccountsAssociationRequestSchema,
    NewAccountsAssociationResponseSchema,
    NewAssetsInheritanceRequestSchema,
    NewAssetsInheritanceResponseSchema,
    NewAssetsRequestSchema,
    NewAssetsResponseSchema,
    NewGroupingRequestSchema,
    NewGroupingResponseSchema,
    NewGroupingsAssociationRequestSchema,
    NewGroupingsAssociationResponseSchema,
    NewPermissionsRequestSchema,
    NewPermissionsResponseSchema,
    NewUserRequestSchema,
    NewUserResponseSchema,
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
        body: list[NewUserRequestSchema],
    ) -> NewUserResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(url=f'/v2/apps/{app_id}/accounts/users', body=json.dumps(body))

    def create_groupings(
        self,
        app_id: str,
        body: list[NewGroupingRequestSchema],
    ) -> NewGroupingResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(url=f'/v2/apps/{app_id}/access/grouping', body=json.dumps(body))

    def create_permissions(
        self,
        app_id: str,
        body: list[NewPermissionsRequestSchema],
    ) -> NewPermissionsResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(url=f'/v2/apps/{app_id}/access/permissions', body=json.dumps(body))

    def create_accounts_association(
        self,
        app_id: str,
        body: NewAccountsAssociationRequestSchema,
    ) -> NewAccountsAssociationResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(url=f'/v2/apps/{app_id}/association/accounts', body=body.json())

    def create_groupings_association(
        self,
        app_id: str,
        body: NewGroupingsAssociationRequestSchema,
    ) -> NewGroupingsAssociationResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(url=f'/v2/apps/{app_id}/association/groupings', body=body.json())

    def create_assets(
        self,
        app_id: str,
        body: NewAssetsRequestSchema,
    ) -> NewAssetsResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(url=f'/v2/apps/{app_id}/assets', body=body.json())

    def create_assets_inheritance(
        self,
        app_id: str,
        body: NewAssetsInheritanceRequestSchema,
    ) -> NewAssetsInheritanceResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        return self.http_post(url=f'/v2/apps/{app_id}/assets/inheritance', body=body.json())
