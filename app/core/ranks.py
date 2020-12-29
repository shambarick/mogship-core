import json
import pathlib
from functools import lru_cache


@lru_cache
def get_ranks():
    with open(f"{pathlib.Path(__file__).parent}/../../data/ranks.json") as json_file:
        data = json.load(json_file)
    return data
