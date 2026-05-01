import http

import pytest


from clients.auth.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tests.conftest import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.authentication
@pytest.mark.regression
def test_login(authentication_client, function_user: UserFixture):
    login_request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password
    )

    login_response = authentication_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, http.HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), LoginResponseSchema.model_json_schema())
