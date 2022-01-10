"""Make sure we have single test"""
from authomize.rest_api_client import Client


def test_import():
    """Test import"""
    client = Client(auth_token='invalid')
    assert client.base_url is not None
