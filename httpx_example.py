import httpx
#
# # response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
# #
# # print(response.status_code)
# # print(response.json())
# #
# # data = {
# #     "userId": 1,
# #     "title": "Новая задача",
# #     "completed": False
# # }
# #
# # response = httpx.post("https://jsonplaceholder.typicode.com/todos/", json=data)
# #
# # print(response.status_code)
# # print(response.json())
# #
# # data = {
# #     "name": "Kirill",
# #     "surname": "Zab",
# #     "middleName": "Ser",
# #     "email": "k.zab@example.com",
# #     "username": "Kirill",
# #     "password": "Kirill123",
# #     "isSubscribed": False
# # }
# #
# # response = httpx.post("https://futuramaapi.com/api/users", json=data)
# # print(response.status_code)
# # print(response.json())
# #
# # headers = {"authorization": "Bearer my_secret_token"}
# # response = httpx.get("https://futuramaapi.com/api/seasons/1", headers=headers)
# #
# # print(response.request.headers)
# # print("\n")
# # print(response.json())
# # print("\n")
#
# params = {"userId": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params )
#
# print(response.url)
# print("\n")
# print(response.json())
# print("\n")
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://postman-echo.com/post", files=files)
# print("\n", response.json())
#
# with httpx.Client() as client:
#     response1 = client.get("https://futuramaapi.com/api/seasons/1")
#     response2 = client.get("https://futuramaapi.com/api/seasons/2")
#
# print("\n", response1.json())
# print("\n", response2.json())
#
# client = httpx.Client(headers = {"authorization": "Bearer my_secret_token"})
# response = client.get("https://jsonplaceholder.typicode.com/todos/1")
# print("\n")
# print(response.request.headers)
# print("\n")
# print(response.json())
# print("\n")

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/todos/invalid")
    print("\n")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

try:
    response = httpx.get("https://httpbun.com/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")