import allure
from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.auth.authentication_schema import RefreshRequestSchema, LoginRequestSchema, LoginResponseSchema


class AuthenticationClient(APIClient):
    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
            Метод выполняет аутентификацию пользователя.

            :param request: Словарь с email и password.
            :return: Ответ от сервера в виде объекта httpx.Response
            """
        return self.post(url="/api/v1/authentication/login", json=request.model_dump(by_alias=True))

    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
            Метод обновляет токен авторизации.

            :param request: Словарь с refreshToken.
            :return: Ответ от сервера в виде объекта httpx.Response
            """
        return self.post(url='/api/v1/authentication/refresh', json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(get_public_http_client())
