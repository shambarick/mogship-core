from typing import Dict, Optional

from pydantic import BaseModel, Field

from .exploration import ExplorationDistance, ExplorationUnlock


class SubmarineMap(BaseModel):
    id: int
    image: int
    name_en: str
    name_fr: str
    name_ja: str
    name_de: str


class SubmarineSector(BaseModel):
    id: int
    rank: int
    map: SubmarineMap
    name_en: str
    name_fr: str
    name_ja: str
    name_de: str
    shortname_en: str
    shortname_fr: str
    shortname_ja: str
    shortname_de: str
    lettername_en: str
    lettername_fr: str
    lettername_ja: str
    lettername_de: str
    isExplorable: bool
    ceruleumTankReq: int
    stars: int
    expReward: int
    surveyRange: int
    surveyDistance: int
    coordX: int
    coordY: int
    coordZ: int
    unlocks: Optional[ExplorationUnlock] = None
    toDestination: Optional[Dict[str, ExplorationDistance]] = Field(example={ "1": { "distance": 25000, "range": 13 } })
