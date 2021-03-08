import json
import pathlib
from functools import lru_cache
from typing import List

from app import schemas


@lru_cache
def get_airship_ranks() -> List[schemas.Rank]:
    with open(f"{pathlib.Path(__file__).parent}/../../data/ranks_airship.json") as json_file:
        data = json.load(json_file)
    return data


@lru_cache
def get_submarine_ranks() -> List[schemas.Rank]:
    with open(f"{pathlib.Path(__file__).parent}/../../data/ranks_submarine.json") as json_file:
        data = json.load(json_file)
    return data
