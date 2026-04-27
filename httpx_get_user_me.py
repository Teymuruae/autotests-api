import httpx

base_url = 'http://localhost:8000/api/v1'

login_payload = {
    "email": "admin@example.com",
    "password": "admin"
}
login_response = httpx.post(url=f'{base_url}/authentication/login', json=login_payload)
access_token = login_response.json()['token']['accessToken']

auth_header = {"Authorization": f"Bearer {access_token}"}
about_me_response = httpx.get(url=f'{base_url}/users/me', headers=auth_header)

print(about_me_response.status_code)
print(about_me_response.json())
