import os.path

import pytest
from pydantic import BaseModel

from clients.files.files_client import FilesClient, get_files_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture


class FilesFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(user=function_user.authentication_user)


@pytest.fixture
def function_files(files_client: FilesClient) -> FilesFixture:
    here = os.path.dirname(os.path.abspath(__file__))
    request = CreateFileRequestSchema(upload_file=os.path.join(os.path.dirname(here), 'testdata/files/cat.jpg'))
    response = files_client.create_file(request)
    return FilesFixture(request=request, response=response)