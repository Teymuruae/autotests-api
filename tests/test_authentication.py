import http

import pytest

from clients.auth.auth_api_client import get_authentication_client
from clients.auth.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema

@pytest.mark.authentication
@pytest.mark.regression
def test_login():
    auth_api_client = get_authentication_client()
    public_users_client = get_public_users_client()

    create_user_request = CreateUserRequestSchema()
    public_users_client.create_user(create_user_request)

    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )

    login_response = auth_api_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, http.HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), LoginResponseSchema.model_json_schema())
