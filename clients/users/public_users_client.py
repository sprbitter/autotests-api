from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент к /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создане пользователя
        :param request:
        Объект с параметрами:
            email: str
            password: str
            lastName: str
            firstName: str
            middleName: str
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserRequestDict:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с базовыми настройками.

    :return: Готовый к успользованию объект PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())