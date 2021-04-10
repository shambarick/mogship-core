from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

DataT = TypeVar("DataT")

class Error(BaseModel):
    code: int
    message: str


class Response(BaseModel):
    message: str
    error: Optional[Error]


class ResultsResponse(GenericModel, Generic[DataT]):
    results: List[DataT]
