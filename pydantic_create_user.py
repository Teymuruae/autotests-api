import uuid

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from pydantic import EmailStr


class UserSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=False)
    id: str = Field(default_factory=lambda: uuid.uuid4())
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')


class CreateUserResponseSchema(BaseModel):
    user: UserSchema
