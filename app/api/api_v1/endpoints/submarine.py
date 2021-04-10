from typing import List, Optional

from loguru import logger
from fastapi import APIRouter, Depends, Query, HTTPException

from app import schemas
from app.api import helpers
from app.core.elasticsearch import get_client
from app.services import builds_calculator as BuildsCalculator, SubmarineService


router = APIRouter()


@router.get("/builds-calculator", response_model=schemas.ResultsResponse[schemas.Build])
async def builds_calculator(
    size: int = Query(100, gte=1, lte=10000),
    page: int = Query(1, gte=1),
    sort: str = Query("stats.speed,DESC"),
    filters: schemas.BuildsFilters = Depends()
):
    results = await BuildsCalculator.find_builds(filters, sort, size, page)
    return schemas.ResultsResponse[schemas.Build](results=[ row["_source"] for row in results["hits"]["hits"] ])


@router.get("/parts", response_model=schemas.ResultsResponse[schemas.Part])
async def get_parts(
    part_class: Optional[int] = Query(None, alias="class"),
    slot: Optional[int] = Query(None, gte=0, lte=3)
):
    return schemas.ResultsResponse[schemas.Part](results=helpers.filter_parts(SubmarineService.get_parts(), part_class, slot))


@router.get("/part-types", response_model=schemas.ResultsResponse[schemas.PartType])
async def get_part_types():
    return schemas.ResultsResponse[schemas.PartType](results=SubmarineService.get_part_types()["submarine"])


@router.get("/ranks", response_model=schemas.ResultsResponse[schemas.Rank])
async def get_ranks():
    return schemas.ResultsResponse[schemas.rank](results=SubmarineService.get_ranks())


@router.get("/ranks/{id}", response_model=schemas.Rank)
async def get_rank(
    id: int = Query(None, ge=1),
):
    return helpers.filter_ranks_by_id(SubmarineService.get_ranks, id)


@router.get("/sectors", response_model=schemas.ResultsResponse[schemas.SubmarineSector], response_model_exclude_unset=True)
async def read_sectors(
    map_id: Optional[int] = Query(None, ge=1)
):
    if map_id is not None:
        print(SubmarineService.get_list_map_ids())
        if str(map_id) not in SubmarineService.get_list_map_ids():
            raise HTTPException(status_code=400, detail="map_id not found")
        return schemas.ResultsResponse[schemas.SubmarineSector](results=SubmarineService.get_sectors_by_map(map_id))
    return schemas.ResultsResponse[schemas.SubmarineSector](results=SubmarineService.get_sectors())


@router.get("/sectors/{id}", response_model=schemas.SubmarineSector)
async def read_sector(
    id: int,
):
    try:
        return SubmarineService.get_sector(id)
    except IndexError as ex:
        raise HTTPException(status_code=404, detail=f"Sector not found")
    except Exception as ex:
        logger.error(ex)
        raise HTTPException(status_code=500, detail=ex)

