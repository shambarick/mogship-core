import json
from abc import ABCMeta, abstractmethod
from functools import lru_cache
from pathlib import Path
from typing import OrderedDict

class ShipService(metaclass=ABCMeta):
    @property
    @abstractmethod
    def ship_type(self):
        raise NotImplementedError


    @lru_cache
    def get_maps(self):
        with open(f"{Path(__file__).parent}/../../data/maps_{self.ship_type}.json") as json_file:
            data = json.load(json_file, object_pairs_hook=OrderedDict)
        maps = [{
            "id": key,
            **data[key],
        } for key in data]
        return maps


    @lru_cache
    def get_sectors(self):
        with open(f"{Path(__file__).parent}/../../data/sectors_{self.ship_type}.json") as json_file:
            data = json.load(json_file, object_pairs_hook=OrderedDict)
        data = [{
            "id": key,
            **data[key],
        } for key in data]
        return data


    def get_sector(self, id: int):
        return self.get_sectors()[id]


    @lru_cache
    def get_list_map_ids(self):
        return list(map(lambda x: x["id"], get_maps()))


    @lru_cache
    def get_sectors_by_map(self, map_id: int):
        return list(filter(lambda x: x["map"]["id"] == map_id, get_sectors()))


    @lru_cache
    def get_parts(self):
        with open(f"{Path(__file__).parent}/../../data/parts_{self.ship_type}.json") as json_file:
            data = json.load(json_file)
        return data


    @lru_cache
    def get_part_types(self):
        with open(f"{Path(__file__).parent}/../../data/part_types.json") as json_file:
            data = json.load(json_file)
        return data


    @lru_cache
    def get_ranks(self):
        with open(f"{Path(__file__).parent}/../../data/ranks_{self.ship_type}.json") as json_file:
            data = json.load(json_file)
        return data

class AirshipService(ShipService):
    ship_type = 'airship'

class SubmarineService(ShipService):
    ship_type = 'submarine'
