from typing import TypedDict

from httpx import Client

from clients.auth.auth_api_client import get_authentication_client, LoginRequestDict


class AuthenticationUserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return
     """
    auth_api_client = get_authentication_client()
    login_response = auth_api_client.login(LoginRequestDict(email=user['email'], password=user['password']))

    headers = {"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    return Client(timeout=100, base_url='http://localhost:8000', headers=headers)
