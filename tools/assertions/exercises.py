from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(
        create_exercise_response: CreateExerciseResponseSchema,
        create_exercise_request: CreateExerciseRequestSchema
):
    """
    Проверяет, что ответ на создание задания соответствует данным из запроса.

    :param create_exercise_request: Запрос на создание задания
    :param create_exercise_response:  API ответ при создании задания.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    assert_equal(create_exercise_response.exercise.title, create_exercise_request.title, "title")
    assert_equal(create_exercise_response.exercise.course_id, create_exercise_request.course_id, "course_id")
    assert_equal(create_exercise_response.exercise.max_score, create_exercise_request.max_score, "max_score")
    assert_equal(create_exercise_response.exercise.min_score, create_exercise_request.min_score, "min_score")
    assert_equal(create_exercise_response.exercise.order_index, create_exercise_request.order_index, "order_index")
    assert_equal(create_exercise_response.exercise.description, create_exercise_request.description, "description")
    assert_equal(create_exercise_response.exercise.estimated_time, create_exercise_request.estimated_time,
                 "estimated_time")
