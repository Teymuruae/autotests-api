import allure

from clients.auth.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_is_true, assert_equal

@allure.step("Check login response")
def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет корректность ответа при успешной авторизации.

    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    assert_equal(response.token.token_type, 'bearer', "token_type")
    assert_is_true(response.token.access_token, name="access_token")
    assert_is_true(response.token.refresh_token, name="refresh_token")
