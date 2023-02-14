"""Configuration for connecting to authomize api"""
from pydantic import BaseSettings, Field


class AuthomizeApiConfiguration(BaseSettings):
    """
    Configuration for connecting to authomize api.
    """

    auth_token: str = Field(..., env="AUTHOMIZE_API_TOKEN")
    api_url: str = Field(..., env="AUTHOMIZE_API_URL")
