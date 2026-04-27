import httpx

url = "https://jsonplaceholder.typicode.com/todos"

# GET
headers = {"Authorization": "Bearer rugaga token"}

response_get = httpx.get(f"{url}/1", headers=headers)
print(response_get.request.headers)
print(response_get.json())

# POST
body = {'userId': 2, 'id': 54645, 'title': 'Rugaga', 'completed': False}

post_response = httpx.post(url=url, json=body)
print(post_response.status_code)
print(post_response.json())

# Отправка данных в application/x-www-form-urlencoded
data = {"username": "test_user", "password": "test_password"}
response_url_encoded = httpx.post("https://httpbin.org/post", data=data)

print(response_url_encoded.json())
# В ответе содержится: 'Content-Type': 'application/x-www-form-urlencoded'

# Передача параметров
params = {
    "userId": 1,
    "completed": True
}

response_params = httpx.get(f"{url}", params=params)
print(response_params.json())

#Загрузка файла
with open("cat.jpg", 'rb') as file:
    files = {"file": ("cat", file)}
    response_files = httpx.post("https://petstore.swagger.io/v2/pet/9/uploadImage", files=files)
    print(response_files.json())

#Client. Как в requests - sessions
#Задаем сразу headers, чтоб все запросы дальнейшие были с ними
client = httpx.Client(headers={"Authorization": "Bearer test_rugaga"})
response_client = client.get("https://httpbin.org/get")

print(response_client.json())
client.close()

#обработка ошибок
try:
    response_error = httpx.get("https://httpbin.org/post/invalid_url")
    response_error.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Произошла ошибка {e}")

#ошибка timeout

try:
    response_timeout = httpx.get("https://httpbin.org/delay/5", timeout=3)
except httpx.TimeoutException as e:
    print("Timeout ошибка " + str(e))
