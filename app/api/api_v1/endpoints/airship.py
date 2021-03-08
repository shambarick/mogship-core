from typing import List, Optional

from fastapi import APIRouter, Query, HTTPException

from app import schemas
from app.api import helpers
from app.services import exploration, parts, ranks


router = APIRouter()


@router.get("/parts", response_model=List[schemas.Part])
async def get_parts(
    part_class: Optional[int] = Query(None, alias="class"),
    slot: Optional[int] = Query(None, gte=0, lte=3)
):
    return helpers.filter_parts(parts.get_airship_parts(), part_class, slot)


@router.get("/part-types", response_model=List[schemas.PartType])
async def get_part_types():
    return parts.get_part_types()["airship"]


@router.get("/ranks", response_model=List[schemas.Rank])
async def get_ranks():
    return ranks.get_airship_ranks()


@router.get("/ranks/{id}", response_model=schemas.Rank)
async def get_rank(
    id: int = Query(None, ge=1),
):
    return helpers.filter_ranks_by_id(ranks.get_airship_ranks, id)
