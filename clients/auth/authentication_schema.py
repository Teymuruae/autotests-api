
from pydantic import BaseModel, Field


class LoginRequestSchema(BaseModel):
    """
      Описание структуры запроса на аутентификацию.
      """
    email: str
    password: str


class RefreshRequestSchema(BaseModel):
    refresh_token: str = Field(alias='refreshToken')


class TokenSchema(BaseModel):
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginResponseSchema(BaseModel):
    token: TokenSchema
