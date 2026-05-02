from functools import lru_cache

from httpx import Client
from pydantic import BaseModel

from clients.auth.auth_api_client import get_authentication_client
from clients.auth.authentication_schema import LoginRequestSchema


class AuthenticationUserSchema(BaseModel, frozen = True):
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
    return Client(timeout=100, base_url='http://localhost:8000', headers=headers)
