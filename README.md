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

Get openapi.json by

```
curl https://api.authomize.com/openapi-extended.json | jq . > authomize/rest_api_client/openapi/openapi.json
```

Update schema by

```
pip install -e .[codegen]
datamodel-codegen --input authomize/rest_api_client/openapi/openapi.json --output authomize/rest_api_client/generated/schemas.py
```
