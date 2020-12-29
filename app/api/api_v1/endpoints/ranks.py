from typing import Any, List

from fastapi import APIRouter, HTTPException, Query

from app.core import ranks


router = APIRouter()

@router.get("")
def get_ranks() -> List:
    return ranks.get_ranks()

@router.get("{id}")
def get_rank(
    id: int = Query(None, ge=1),
) -> Any:
    try:
        return ranks.get_ranks()[id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Rank not found")
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)
