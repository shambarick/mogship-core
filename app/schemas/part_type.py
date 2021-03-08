from pydantic import BaseModel


class PartType(BaseModel):
    id: int
    name_en: str
    name_fr: str
    name_ja: str
    name_de: str
