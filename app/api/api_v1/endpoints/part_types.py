from typing import Any, List

from fastapi import APIRouter

from app.core import parts


router = APIRouter()


@router.get("")
def get_part_types():
    return parts.get_part_types()

@router.get("/airship")
def get_airship_part_types():
    return parts.get_part_types()["Airship"]

@router.get("/submarine")
def get_submarine_part_types():
    return parts.get_part_types()["Submarine"]
