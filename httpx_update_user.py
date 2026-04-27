import httpx

from tools.fakers import get_random_email

base_url = 'http://localhost:8000/api/v1'

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post(url=f"{base_url}/users", json=create_user_payload)

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post(url=f"{base_url}/authentication/login", json=login_payload)

token = login_response.json()['token']['accessToken']
user_id = create_user_response.json()['user']['id']
update_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
auth_header = {
    "Authorization": f"Bearer {token}"
}

update_response = httpx.patch(
    url=f'{base_url}/users/{user_id}',
    json=update_payload,
    headers=auth_header

)

print(update_response.json())
