from typing import Any, List, Optional

from fastapi import APIRouter, HTTPException, Query

from app import schemas
from app.api import helpers
from app.core import parts


router = APIRouter()


@router.get("/airship", response_model=List[schemas.Part])
def get_parts(
    part_class: Optional[int] = Query(None, alias="class"),
    slot: Optional[int] = Query(None, gte=0, lte=3)
):
    return helpers.filter_parts(parts.get_airship_parts(), part_class, slot)


@router.get("/submarine", response_model=List[schemas.Part])
def get_parts(
    part_class: Optional[int] = Query(None, alias="class"),
    slot: Optional[int] = Query(None, gte=0, lte=3)
):
    return helpers.filter_parts(parts.get_submarine_parts(), part_class, slot)

