from typing import TypedDict

from clients.api_client import APIClient
from httpx import Response

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение упражнения
    """
    courseId: str

class CreateExerciseDict(TypedDict):
    """
    Описание структры запроса создания задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса обновления задания.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class ExercisesClient(APIClient):
    """
    Клиент к методу /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения упражнений к курсу.
        :param query: Словарь с CourseID
        :return: Словарь со списком упражнений
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.
        :param exercise_id: Индетивикатор упражнения
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseDict) -> Response:
        """
        Метод создания с задания
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления задания.
        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде httpx.Response
        """

    def delete_exercise_api(self, exercise_id: str):
        """
        Метод удаления задния.
        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")