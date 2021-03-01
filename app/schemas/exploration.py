from typing import List, Optional

from pydantic import BaseModel, Field


class ExplorationDistance(BaseModel):
    distance: int = Field(example=23000)
    range: int = Field(example=14)


class ExplorationUnlock(BaseModel):
    sectors: List[int] = Field(example=[3, 4, 5])
    slot: Optional[int] = Field(example=2)
