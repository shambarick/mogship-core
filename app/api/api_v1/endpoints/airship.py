from typing import List, Optional

from fastapi import APIRouter, Query, HTTPException

from app import schemas
from app.api import helpers
from app.services import AirshipService


router = APIRouter()


@router.get("/parts", response_model=schemas.ResultsResponse[schemas.Part])
async def get_parts(
    part_class: Optional[int] = Query(None, alias="class"),
    slot: Optional[int] = Query(None, gte=0, lte=3)
):
    return schemas.ResultsResponse[schemas.Part](results=helpers.filter_parts(AirshipService.get_parts(), part_class, slot))


@router.get("/part-types", response_model=schemas.ResultsResponse[schemas.PartType])
async def get_part_types():
    return schemas.ResultsResponse[schemas.PartType](results=AirshipService.get_part_types()["airship"])


@router.get("/ranks", response_model=schemas.ResultsResponse[schemas.Rank])
async def get_ranks():
    return schemas.ResultsResponse[schemas.Rank](results=AirshipService.get_ranks())


@router.get("/ranks/{id}", response_model=schemas.Rank)
async def get_rank(
    id: int = Query(None, ge=1),
):
    return helpers.filter_ranks_by_id(AirshipService.get_ranks(), id)
