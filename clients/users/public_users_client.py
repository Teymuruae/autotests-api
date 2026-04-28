from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
             Метод создает пользователя.

             :param request: Словарь с email, password, lastName, firstName, middleName.
             :return: Ответ от сервера в виде объекта httpx.Response
             """
        return self.post(url='/api/v1/users', json=request)
