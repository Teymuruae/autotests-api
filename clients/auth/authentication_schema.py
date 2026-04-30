from pydantic import BaseModel, Field
from tools.fakers import fake


class LoginRequestSchema(BaseModel):
    """
      Описание структуры запроса на аутентификацию.
      """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class RefreshRequestSchema(BaseModel):
    refresh_token: str = Field(alias='refreshToken', default_factory=lambda: fake.sentence)


class TokenSchema(BaseModel):
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginResponseSchema(BaseModel):
    token: TokenSchema
