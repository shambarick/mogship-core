import json
import pathlib
from functools import lru_cache


@lru_cache
def get_airship_parts():
    with open(f"{pathlib.Path(__file__).parent}/../../data/parts_airship.json") as json_file:
        data = json.load(json_file)
    return data


@lru_cache
def get_submarine_parts():
    with open(f"{pathlib.Path(__file__).parent}/../../data/parts_submarine.json") as json_file:
        data = json.load(json_file)
    return data


@lru_cache
def get_part_types():
    with open(f"{pathlib.Path(__file__).parent}/../../data/part_types.json") as json_file:
        data = json.load(json_file)
    return data
