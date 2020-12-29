from typing import Any, List, Optional

from fastapi import APIRouter, HTTPException, Query

from app.core import exploration


router = APIRouter()


@router.get("")
def read_sectors(
    map_id: Optional[int] = Query(None, ge=1)
) -> Any:
    if map_id is not None:
        print(exploration.get_list_map_ids())
        if str(map_id) not in exploration.get_list_map_ids():
            raise HTTPException(status_code=400, detail="map_id not found")
        data = exploration.get_sectors_by_map(map_id)
        return data
    return exploration.get_sectors()


@router.get("/{id}")
def read_sector(
    id: int,
) -> Any:
    try:
        return exploration.get_sectors()[id]
    except IndexError as ex:
        raise HTTPException(status_code=404, detail=f"Sector not found")
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)
