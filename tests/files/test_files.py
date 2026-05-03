import os.path
from http import HTTPStatus

import pytest

from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from fixtures.files import FilesFixture
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_file_is_accessible, assert_get_file_response, \
    assert_create_file_with_empty_filename_response, assert_create_file_with_empty_directory_response, \
    assert_file_not_found_response, assert_get_file_with_incorrect_file_id_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.files
@pytest.mark.regression
class TestFiles:
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file="./testdata/files/cat.jpg")
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_file(self, files_client: FilesClient, function_files: FilesFixture):
        get_file_response = files_client.get_file_api(function_files.response.file.id)
        get_file_response_data = GetFileResponseSchema.model_validate_json(get_file_response.text)

        assert_status_code(get_file_response.status_code, HTTPStatus.OK)
        assert_get_file_response(get_file_response_data, function_files.response)

        validate_json_schema(get_file_response.json(), get_file_response_data.model_json_schema())

    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            filename="",
            upload_file="./testdata/files/cat.jpg")
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(response_data)

    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            directory="",
            upload_file="./testdata/files/cat.jpg")
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(response_data)

    def test_delete_file(self, files_client: FilesClient, function_files: FilesFixture):
        files_client.delete_file_api(function_files.response.file.id)
        get_file_response = files_client.get_file_api(function_files.response.file.id)
        get_file_response_data = InternalErrorResponseSchema.model_validate_json(get_file_response.text)

        assert_status_code(get_file_response.status_code, HTTPStatus.NOT_FOUND)
        assert_file_not_found_response(get_file_response_data)

        validate_json_schema(get_file_response.json(), get_file_response_data.model_json_schema())

    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient):
        get_file_response = files_client.get_file_api("incorrect-file-id")
        get_file_response_data = ValidationErrorResponseSchema.model_validate_json(get_file_response.text)

        assert_status_code(get_file_response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id_response(get_file_response_data)

        validate_json_schema(get_file_response.json(), get_file_response_data.model_json_schema())

