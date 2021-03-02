from typing import List

from fastapi import APIRouter, HTTPException, Query

from app import schemas
from app.api import helpers
from app.core import ranks


router = APIRouter()

@router.get("/airship", response_model=List[schemas.Rank])
def get_airship_ranks():
    return ranks.get_airship_ranks()

@router.get("/submarine", response_model=List[schemas.Rank])
def get_submarine_ranks() -> List[schemas.Rank]:
    return ranks.get_submarine_ranks()

@router.get("/airship/{id}", response_model=schemas.Rank)
def get_airship_rank(
    id: int = Query(None, ge=1),
) -> schemas.Rank:
    return helpers.filter_ranks_by_id(ranks.get_airship_ranks, id)

@router.get("/submarine/{id}", response_model=schemas.Rank)
def get_submarine_rank(
    id: int = Query(None, ge=1),
) -> schemas.Rank:
    return helpers.filter_ranks_by_id(ranks.get_submarine_ranks, id)
