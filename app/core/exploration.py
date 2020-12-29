import json
import pathlib
from collections import OrderedDict
from functools import lru_cache
from typing import List


@lru_cache
def get_maps() -> List:
    with open(f"{pathlib.Path(__file__).parent}/../../data/maps.json") as json_file:
        data = json.load(json_file, object_pairs_hook=OrderedDict)
    maps = [{
        "ID": key,
        **data[key],
    } for key in data]
    return maps


@lru_cache
def get_sectors() -> List:
    with open(f"{pathlib.Path(__file__).parent}/../../data/sectors_names.json") as json_file:
        data = json.load(json_file, object_pairs_hook=OrderedDict)
    data = [{
        "ID": key,
        **data[key],
    } for key in data]
    return data


@lru_cache
def get_list_map_ids():
    return list(map(lambda x: x["ID"], get_maps()))


@lru_cache
def get_sectors_by_map(map_id: int) -> List:
    return list(filter(lambda x: x["Map"]["ID"] == map_id,get_sectors()))
