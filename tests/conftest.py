import pytest
from pydantic import BaseModel, EmailStr

from clients.auth.auth_api_client import get_authentication_client, AuthenticationClient
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema
    authentication_user: AuthenticationUserSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password


@pytest.fixture()
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()


@pytest.fixture()
def public_user_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture()
def private_users_client(function_user) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)


@pytest.fixture()
def function_user(public_user_client: PublicUsersClient):
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    auth_schema = AuthenticationUserSchema(email=request.email, password=request.password)
    return UserFixture(request=request, response=response, authentication_user=auth_schema)
