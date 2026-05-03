from typing import Any, Annotated

from pydantic import BaseModel, Field, ConfigDict


class ValidationErrorSchema(BaseModel):
    """
    Модель, описывающая структуру ошибки валидации API.
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str
    input: Any
    context: Annotated[dict[str, Any], Field(alias="ctx")]
    message: Annotated[str, Field(alias="msg")]
    location: Annotated[list[str], Field(alias="loc")]


class ValidationErrorResponseSchema(BaseModel):
    """
    Модель, описывающая структуру ответа API с ошибкой валидации.
    """
    model_config = ConfigDict(populate_by_name=True)

    details: Annotated[list[ValidationErrorSchema], Field(alias="detail")]


class InternalErrorResponseSchema(BaseModel):
    """
    Модель для описания внутренней ошибки.
    """

    model_config = ConfigDict(populate_by_name=True)

    details: Annotated[str, Field(alias="detail")]
