from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
      Описание структуры упражнения.
      """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str


class GetExercisesResponseDict(TypedDict):
    """
      Описание структуры ответа получения упражнений.
      """
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    """
      Описание структуры ответа получения упражнения.
      """
    exercise: Exercise


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
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
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, request: GetExercisesRequestDict) -> Response:
        """
         Метод получения списка упражнений.

         :param query: Словарь с courseId.
         :return: Ответ от сервера в виде объекта httpx.Response
         """
        return self.get(url='/api/v1/exercises', params=request)

    def get_exercises(self, request: GetExercisesRequestDict) -> GetExercisesResponseDict:
        return self.get_exercises_api(request).json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
           Метод получения упражнения.

           :param exercise_id: Идентификатор упражнения.
           :return: Ответ от сервера в виде объекта httpx.Response
           """
        return self.get(url=f'/api/v1/exercises/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        return self.get_exercise_api(exercise_id).json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, maxScore, minScore, orderIndex,
        description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url='/api/v1/exercises', json=request)

    def create_exercise(self, request: CreateExerciseRequestDict) -> GetExerciseResponseDict:
        return self.create_exercise_api(request).json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
         Метод обновления упражнения.

         :param exercise_id: Идентификатор упражнения.
         :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
         :return: Ответ от сервера в виде объекта httpx.Response
         """
        return self.patch(url=f'/api/v1/exercises/{exercise_id}', json=request)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> GetExerciseResponseDict:
        return self.update_exercise_api(exercise_id, request).json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'/api/v1/exercises/{exercise_id}')


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(get_private_http_client(user))
