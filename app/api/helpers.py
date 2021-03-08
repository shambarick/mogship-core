from typing import List, Optional

from fastapi import HTTPException

from app import schemas


def filter_parts(results: List[schemas.Part], part_class: Optional[int], slot: Optional[int]):
    if part_class is not None:
        results = list(filter(lambda x: x["class"] == part_class, results))

    if slot is not None:
        results = list(filter(lambda x: x["slot"] == slot, results))

    return results


def filter_ranks_by_id(data: List[schemas.Rank], id: int):
    try:
        return data[id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Rank not found")
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex)
