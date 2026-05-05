import os
from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, GetExercisesRequestSchema, \
    GetExercisesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
@allure.suite(AllureFeature.EXERCISES)
class TestExercises:
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Create exercise")
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_create_exercise(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture
    ):
        request = CreateExerciseRequestSchema(
            courseId=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(
            create_exercise_response=response_data,
            create_exercise_request=request)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("Get exercise")
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_get_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(
            get_exercise_response=response_data,
            create_exercise_responses=function_exercise.response
        )
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("Update exercise")
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(function_exercise.response.exercise.id, request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(
            request=request,
            response=response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.title("Delete exercise")
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_delete_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        response = exercises_client.delete_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(response.status_code, HTTPStatus.OK)

        error_get_response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        error_get_response_data = InternalErrorResponseSchema.model_validate_json(error_get_response.text)

        assert_status_code(error_get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(error_get_response_data)

        validate_json_schema(error_get_response.json(), error_get_response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("Get exercises")
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    @allure.severity(Severity.BLOCKER)
    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture
    ):
        create_exercise_request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id
        )
        create_exercise_response = exercises_client.create_exercise_api(create_exercise_request)
        create_exercise_response_data = CreateExerciseResponseSchema.model_validate_json(create_exercise_response.text)

        get_exercises_request = GetExercisesRequestSchema(course_id=function_course.response.course.id)
        get_exercises_response = exercises_client.get_exercises_api(get_exercises_request)
        get_exercises_response_data = GetExercisesResponseSchema.model_validate_json(get_exercises_response.text)

        assert_status_code(get_exercises_response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(
            get_exercises_response=get_exercises_response_data,
            create_exercise_responses=[create_exercise_response_data]
        )

        validate_json_schema(get_exercises_response.json(), get_exercises_response_data.model_json_schema())
