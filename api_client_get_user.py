from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_user_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

create_user_payload = CreateUserRequestDict(
    email=get_random_email(),
    password='str',
    lastName='str',
    firstName='str',
    middleName='str'
)

public_users_client = get_public_users_client()
create_user_response = public_users_client.create_user(create_user_payload)
print(f"Created user data: {create_user_response}")

auth_data = AuthenticationUserDict(email=create_user_payload['email'], password=create_user_payload['password'])
private_users_client = get_private_user_client(auth_data)

get_user_response = private_users_client.get_user(create_user_response['user']['id'])
print(f"Get user data: {get_user_response}")
