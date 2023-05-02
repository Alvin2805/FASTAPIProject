from enum import Enum
from fastapi import Response, status
from pydantic import BaseModel


class SortEnum(str, Enum):
    asc = "asc"
    desc = "desc"


class BasePayload(BaseModel):
    message: str
    data: list[object] | object | None = None


def to_model(model: object):
    class ModelPayload(BaseModel):
        message: str
        data: list[model] | model | None = None
    return ModelPayload


def to_payload(status_code: int = status.HTTP_200_OK,
               media_type: str = 'application/json',
               message: str = 'Success',
               data: list[object] | object | None = None):
    return Response(status_code=status_code,
                    media_type=media_type,
                    content=BasePayload(message=message, data=data).json())
