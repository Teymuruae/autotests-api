import http
from tools.fakers import fake
import pytest

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response


@pytest.mark.parametrize('email', [
    fake.email(domain='mail.ru'),
    fake.email(domain='gmail.com'),
    fake.email(domain='example.com')
])
@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client, email):
    request = CreateUserRequestSchema(email=email)

    create_user_response = public_users_client.create_user_api(request)
    create_user_response_data = CreateUserResponseSchema.model_validate_json(create_user_response.text)

    assert_status_code(create_user_response.status_code, http.HTTPStatus.OK)
    assert_create_user_response(request, create_user_response_data)
    validate_json_schema(create_user_response.json(), CreateUserResponseSchema.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(function_user, private_users_client):
    get_user_me_api_response = private_users_client.get_user_me_api()
    get_user_response = GetUserResponseSchema.model_validate_json(get_user_me_api_response.text)

    assert_status_code(get_user_me_api_response.status_code, http.HTTPStatus.OK)
    assert_get_user_response(get_user_response.user, function_user.response.user)
    validate_json_schema(get_user_me_api_response.json(), GetUserResponseSchema.model_json_schema())
