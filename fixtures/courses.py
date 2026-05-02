import pytest
from pydantic import BaseModel

from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FilesFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(user=function_user.authentication_user)


def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_files: FilesFixture
) -> CourseFixture:
    request = CreateCourseRequestSchema(
        created_by_user_id=function_user.response.user.id,
        preview_file_id=function_files.response.file.id

    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)
