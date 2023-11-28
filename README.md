# Authomize REST API Client
An automatically generated python client for the Authomize API.

## Usage

```python
import os

from authomize.rest_api_client import Client
from authomize.rest_api_client.generated.connectors_rest_api.schemas import (
    NewUserRequestSchema,
    NewUsersListRequestSchema,
)

# Create a client using your Authomize secret Token
client = Client(auth_token=os.environ['AUTHOMIZE_TOKEN'])
# Using an existing connector
app_id = os.environ['AUTHOMIZE_APP_ID']
# Sanity test for Login
me = client.me()
# Insert some typed items
client.create_users(
    app_id,
    NewUsersListRequestSchema(
        data=[
            NewUserRequestSchema(uniqueId='i0', name='John Smith', email='john.smith@example.com')
        ]
    ),
)
```

## Installing

From PyPI:

```
pip install authomize-rest-api-client
```

## Making changes to this repository

For code automatically generated from openapi.json using [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator)
```
pip install -e .[codegen]
```
Fetching openapi.json and updating schema.

for connectors-rest-api:
```
curl --socks5-hostname 127.0.0.1:1337 http://connectors-rest-api.application.svc:8080/openapi-extended.json | jq --indent 2 . > authomize/rest_api_client/openapi/connectors_rest_api/openapi.json
```
```
datamodel-codegen --use-default-kwarg --input authomize/rest_api_client/openapi/connectors_rest_api/openapi.json --output authomize/rest_api_client/generated/connectors_rest_api/schemas.py
```

for external-rest-api:
```
curl https://apidev.authomize.com/openapi-platform.json | jq --indent 2 . > authomize/rest_api_client/openapi/external_rest_api/openapi.json
```
```
datamodel-codegen --use-default-kwarg --encoding=utf-8 --input authomize/rest_api_client/openapi/external_rest_api/openapi.json --output authomize/rest_api_client/generated/external_rest_api/schemas.py
```
