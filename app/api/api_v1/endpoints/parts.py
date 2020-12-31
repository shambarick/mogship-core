from typing import Any, List, Optional

from fastapi import APIRouter, HTTPException, Query

from app.core import parts


router = APIRouter()


@router.get("/submarine")
def get_parts(
    part_class: Optional[int] = Query(None, alias="class"),
    slot: Optional[int] = Query(None, gte=0, lte=3)
):
    results = parts.get_submarine_parts()

    if part_class is not None:
        results = list(filter(lambda x: x["Class"] == part_class, results))

    if slot is not None:
        results = list(filter(lambda x: x["Slot"] == slot, results))

    return results
