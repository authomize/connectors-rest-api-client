import json
from datetime import datetime
from typing import Optional

from pydantic.json import pydantic_encoder

from authomize.rest_api_client.client.base_client import BaseClient
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


class ConnectorsClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def authorization_header(self) -> str:
        return self.auth_token

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
        modified_before: Optional[datetime] = None,
    ) -> SubmitResponse:
        if not app_id:
            raise ValueError('Missing app_id')
        date_filter = ''
        if modified_before:
            date_filter = f'?modifiedBefore={str(modified_before)}'
        return self.http_delete(url=f"/v2/apps/{app_id}/data{date_filter}")

    def search_users(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchUsersListResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        params = dict(
            start_date=start_date,
        )
        return self.http_get(
            url=f'/v2/apps/{app_id}/accounts/users',
            params={
                **params,
            },
        )

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

    def search_groupings(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchGroupingResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        params = dict(
            start_date=start_date,
        )
        return self.http_get(
            url=f'/v2/apps/{app_id}/access/grouping',
            params={
                **params,
            },
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

    def search_permissions(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchPermissionResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        params = dict(
            start_date=start_date,
        )
        return self.http_get(
            url=f'/v2/apps/{app_id}/access/permissions',
            params={
                **params,
            },
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

    def search_privileges(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchPrivilegesListResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        params = dict(
            start_date=start_date,
        )
        return self.http_get(
            url=f'/v2/apps/{app_id}/privileges',
            params={
                **params,
            },
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

    def search_privileges_grants(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchPrivilegeGrantsListResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        params = dict(
            start_date=start_date,
        )
        return self.http_get(
            url=f'/v2/apps/{app_id}/privileges/grants',
            params={
                **params,
            },
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

    def search_accounts_association(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchAccountsAssociationsListResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        params = dict(
            start_date=start_date,
        )
        return self.http_get(
            url=f'/v2/apps/{app_id}/association/accounts',
            params={
                **params,
            },
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

    def search_groupings_association(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchGroupingsAssociationsListResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        params = dict(
            start_date=start_date,
        )
        return self.http_get(
            url=f'/v2/apps/{app_id}/association/groupings',
            params={
                **params,
            },
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

    def search_assets(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchAssetsListResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        params = dict(
            start_date=start_date,
        )
        return self.http_get(
            url=f'/v2/apps/{app_id}/assets',
            params={
                **params,
            },
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

    def search_assets_inheritance(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchAssetsInheritanceListResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        params = dict(
            start_date=start_date,
        )
        return self.http_get(
            url=f'/v2/apps/{app_id}/assets/inheritance',
            params={
                **params,
            },
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

    def search_identities(
        self,
        app_id: str,
        start_date: Optional[datetime] = None,
    ) -> SearchIdentitiesListResponseSchema:
        if not app_id:
            raise ValueError('Missing app_id')
        params = dict(
            start_date=start_date,
        )
        return self.http_get(
            url=f'/v2/apps/{app_id}/identities',
            params={
                **params,
            },
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
