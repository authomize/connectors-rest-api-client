# Authomize REST API Client
An automatically generated python client for the Authomize API.

## Usage

```python
import os

from authomize.rest_api_client import (
    AccessDescription,
    AssetDescription,
    AssetsInheritance,
    Client,
    IdentitiesInheritance,
    IdentityDescription,
    IdentityTypes,
    ItemsBundleSchema,
    ServiceDescription,
)

# Create a client using your Authomize secret Token
client = Client(auth_token=os.environ['AUTHOMIZE_TOKEN'])
# Using an existing connector
connector_id = os.environ['AUTHOMIZE_CONNECTOR_ID']
# Sanity test for Login
me = client.me()
# Create a new transaction
transaction = client.create_transaction(connector_id)
# Insert some typed items
client.extend_transaction_items(connector_id, transaction.id, ItemsBundleSchema(
    services=[],
    identities=[IdentityDescription(id='i0', name='John Smith', type=IdentityTypes.User.value)],
    assets=[],
    inheritanceIdentities=[],
    inheritanceAssets=[],
    access=[]
))
client.apply_transaction(connector_id, transaction.id)
```

## Installing

From PyPI:

```
pip install authomize-rest-api-client
```

## Making changes to this repository

For code automatically generated from openapi.json using [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator)

Fetching openapi.json and updating schema.

for connectors-rest-api:
```
curl --socks5-hostname 127.0.0.1:1337 http://connectors-rest-api.application.svc:8080/openapi-extended.json | jq --indent 2 . > authomize/rest_api_client/openapi/connectors_rest_api/openapi.json
```
```
pip install -e .[codegen]
datamodel-codegen --use-default-kwarg --encoding=utf-8 --input authomize/rest_api_client/openapi/connectors_rest_api/openapi.json --output authomize/rest_api_client/generated/connectors_rest_api/schemas.py
```

for external-rest-api:
```
curl https://apidev.authomize.com/openapi-platform.json | jq --indent 2 . > authomize/rest_api_client/openapi/external_rest_api/openapi.json
```
```
datamodel-codegen --use-default-kwarg --encoding=utf-8 --input authomize/rest_api_client/openapi/external_rest_api/openapi.json --output authomize/rest_api_client/generated/external_rest_api/schemas.py
```
