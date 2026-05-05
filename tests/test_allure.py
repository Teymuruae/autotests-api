import allure


@allure.step("Create user with username {username}")
def create_user(username: str):
    ...


def test_create_users():
    with allure.step("Get username list"):
        lst = ["one", "two"]

    for username in lst:
        create_user(username)
