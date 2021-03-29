from typing import Dict, List, Optional

from fastapi import Depends, Query
from loguru import logger
from pydantic import BaseModel, Field


class StatFilter(BaseModel):
    min: Optional[int]
    exact: Optional[int]
    max: Optional[int]


class BuildsFilters(BaseModel):
    rank_min: Optional[int]
    rank_exact: Optional[int]
    rank_max: Optional[int]

    components_min: Optional[int]
    components_exact: Optional[int]
    components_max: Optional[int]

    repair_cost_min: Optional[int]
    repair_cost_exact: Optional[int]
    repair_cost_max: Optional[int]

    slot0: Optional[str]
    slot1: Optional[str]
    slot2: Optional[str]
    slot3: Optional[str]

    surveillance_min: Optional[int]
    surveillance_exact: Optional[int]
    surveillance_max: Optional[int]
    
    retrieval_min: Optional[int]
    retrieval_exact: Optional[int]
    retrieval_max: Optional[int]

    speed_min: Optional[int]
    speed_exact: Optional[int]
    speed_max: Optional[int]

    range_min: Optional[int]
    range_exact: Optional[int]
    range_max: Optional[int]

    favor_min: Optional[int]
    favor_exact: Optional[int]
    favor_max: Optional[int]


    def __get_stat_filter__(self, stat_name: str) -> StatFilter:
        return {
            "min": getattr(self, f'{stat_name}_min'),
            "exact": getattr(self, f'{stat_name}_exact'),
            "max": getattr(self, f'{stat_name}_max'),
        }


    def to_part_slots_filters_dict(self):
        if self.slot0 is None and self.slot1 is None and self.slot2 is None and self.slot3 is None:
            return {}
        return {
           "slots.0": self.slot0,
           "slots.1": self.slot1,
           "slots.2": self.slot2,
           "slots.3": self.slot3,
        }


    def to_stats_filters_dict(self):
        return {
            "rank": self.__get_stat_filter__("rank"),
            "components": self.__get_stat_filter__("components"),
            "repairCost": self.__get_stat_filter__("repair_cost"),
            "stats.surveillance": self.__get_stat_filter__("surveillance"),
            "stats.retrieval": self.__get_stat_filter__("retrieval"),
            "stats.speed": self.__get_stat_filter__("speed"),
            "stats.range": self.__get_stat_filter__("range"),
            "stats.favor": self.__get_stat_filter__("favor"),
        }
