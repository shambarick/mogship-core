from pydantic import BaseModel, Field


class Part(BaseModel):
    id: int
    rank: int
    ship_class: int = Field(alias="class")
    slot: int
    name_fr: str
    name_en: str
    name_ja: str
    name_de: str
    shortname_fr: str
    shortname_en: str
    shortname_ja: str
    shortname_de: str
    components: int
    surveillance: int
    retrieval: int
    speed: int
    range: int
    favor: int
    repair_cost: int = Field(alias="repairCost")
