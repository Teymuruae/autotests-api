from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class LoginRequestDict(TypedDict):
    """
      Описание структуры запроса на аутентификацию.
      """
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    refreshToken: str


class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginResponseDict(TypedDict):
    token: Token


class AuthenticationClient(APIClient):
    def login_api(self, request: LoginRequestDict) -> Response:
        """
            Метод выполняет аутентификацию пользователя.

            :param request: Словарь с email и password.
            :return: Ответ от сервера в виде объекта httpx.Response
            """
        return self.post(url="/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
            Метод обновляет токен авторизации.

            :param request: Словарь с refreshToken.
            :return: Ответ от сервера в виде объекта httpx.Response
            """
        return self.post(url='/api/v1/authentication/refresh', json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)
        return response.json()


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(get_public_http_client())
