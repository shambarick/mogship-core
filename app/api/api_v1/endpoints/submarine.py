from typing import List, Optional

from loguru import logger
from fastapi import APIRouter, Depends, Query, HTTPException

from app import schemas
from app.api import helpers
from app.services import exploration, parts, ranks
from app.core.elasticsearch import get_client
from app.services import builds_calculator as BuildsCalculator


router = APIRouter()


@router.get("/builds-calculator", response_model=List[schemas.Build])
async def builds_calculator(filters:schemas.BuildsFilters = Depends()):
    query = BuildsCalculator.find_builds(filters)
    results = await get_client().search(
        index="submarinebuilds-0001",
        body=query,
    )
    return [ row["_source"] for row in results["hits"]["hits"] ]


@router.get("/parts", response_model=List[schemas.Part])
async def get_parts(
    part_class: Optional[int] = Query(None, alias="class"),
    slot: Optional[int] = Query(None, gte=0, lte=3)
):
    return helpers.filter_parts(parts.get_submarine_parts(), part_class, slot)


@router.get("/part-types", response_model=List[schemas.PartType])
async def get_part_types():
    return parts.get_part_types()["submarine"]


@router.get("/ranks", response_model=List[schemas.Rank])
async def get_ranks():
    return ranks.get_submarine_ranks()


@router.get("/ranks/{id}", response_model=schemas.Rank)
async def get_rank(
    id: int = Query(None, ge=1),
):
    return helpers.filter_ranks_by_id(ranks.get_submarine_ranks, id)


@router.get("/sectors", response_model=List[schemas.SubmarineSector], response_model_exclude_unset=True)
async def read_sectors(
    map_id: Optional[int] = Query(None, ge=1)
):
    if map_id is not None:
        print(exploration.get_list_map_ids())
        if str(map_id) not in exploration.get_list_map_ids():
            raise HTTPException(status_code=400, detail="map_id not found")
        data = exploration.get_sectors_by_map(map_id)
        return data
    return exploration.get_sectors()


@router.get("/sectors/{id}", response_model=schemas.SubmarineSector)
async def read_sector(
    id: int,
):
    try:
        return exploration.get_sectors()[id]
    except IndexError as ex:
        raise HTTPException(status_code=404, detail=f"Sector not found")
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)

