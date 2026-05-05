from functools import lru_cache

from httpx import Client
from pydantic import BaseModel

from clients.auth.auth_api_client import get_authentication_client
from clients.auth.authentication_schema import LoginRequestSchema
from clients.event_hooks import curl_event_hook
from config import settings


class AuthenticationUserSchema(BaseModel, frozen=True):
    email: str
    password: str


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return
     """
    auth_api_client = get_authentication_client()
    login_response = auth_api_client.login(LoginRequestSchema(email=user.email, password=user.password))

    headers = {"Authorization": f"Bearer {login_response.token.access_token}"}
    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        headers=headers,
        event_hooks={'request': [curl_event_hook]}
    )
