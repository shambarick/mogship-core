from typing import Optional

from pydantic import BaseModel, Field


class Rank(BaseModel):
    rank: int
    capacity: int
    expToNext: int
    surveillance: Optional[int] = Field(None)
    retrieval: Optional[int] = Field(None)
    speed: Optional[int] = Field(None)
    range: Optional[int] = Field(None)
    favor: Optional[int] = Field(None)
