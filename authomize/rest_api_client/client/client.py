from apiclient_pydantic import serialize_all_methods, serialize_response

from authomize.rest_api_client.client.base_client import BaseClient
from authomize.rest_api_client.generated.schemas import (
    BundleTransactionSchema,
    ItemsBundleSchema,
    MeResponse,
    RestApiConnectorListSchema,
    SubmitResponse,
)


@serialize_all_methods(decorator=serialize_response)
class Client(BaseClient):
    def me(self) -> MeResponse:
        return self.http_get('/v1/me')

    def list_connectors(self, params=None) -> RestApiConnectorListSchema:
        return self.http_get('/v1/connectors', params=params)

    def create_transaction(self, connector_id: str) -> BundleTransactionSchema:
        if not connector_id:
            raise ValueError('Missing connector_id')
        return self.http_post(f'/v1/connectors/{connector_id}/transactions')

    def retrieve_transaction(
        self,
        connector_id: str,
        transaction_id: str
    ) -> BundleTransactionSchema:
        if not connector_id:
            raise ValueError('Missing connector_id')
        if not transaction_id:
            raise ValueError('Missing transaction_id')
        return self.http_get(f'/v1/connectors/{connector_id}/transactions/{transaction_id}')

    def apply_transaction(self, connector_id: str, transaction_id: str) -> BundleTransactionSchema:
        if not connector_id:
            raise ValueError('Missing connector_id')
        if not transaction_id:
            raise ValueError('Missing transaction_id')
        return self.http_post(f'/v1/connectors/{connector_id}/transactions/{transaction_id}/apply')

    def extend_transaction_items(
        self,
        connector_id: str,
        transaction_id: str,
        items: ItemsBundleSchema
    ) -> SubmitResponse:
        if not connector_id:
            raise ValueError('Missing connector_id')
        if not transaction_id:
            raise ValueError('Missing transaction_id')
        return self.http_post(
            f'/v1/connectors/{connector_id}/transactions/{transaction_id}/items',
            body=items.json()
        )
