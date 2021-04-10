from typing import Dict, List

from pydantic import BaseModel, Field


class ShipStats(BaseModel):
    surveillance: int
    retrieval: int
    speed: int
    range: int
    favor: int


class Build(BaseModel):
    rank: int
    components: int
    repair_cost: int = Field(..., alias="repairCost")
    slots: Dict[int, int]
    stats: ShipStats

class BuildsResponse(BaseModel):
    results: List[Build]
