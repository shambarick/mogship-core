import json
import pathlib
from functools import lru_cache


@lru_cache
def get_submarine_parts():
    with open(f"{pathlib.Path(__file__).parent}/../../data/submarine_parts.json") as json_file:
        data = json.load(json_file)
    return data

@lru_cache
def get_part_types():
    with open(f"{pathlib.Path(__file__).parent}/../../data/part_types.json") as json_file:
        data = json.load(json_file)
    return data
