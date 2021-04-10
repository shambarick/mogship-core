import json
from typing import Dict, List

from loguru import logger

from app import schemas
from app.core.elasticsearch import get_client


def to_es_filter(filters: schemas.BuildsFilters):
    logger.debug(filters)
    es_query = []
    es_terms: Dict[string, List[int]] = {}
    for key, value in filters.to_part_slots_filters_dict().items():
        if value is not None:
            es_terms.update({key: [int(x) for x in value.split(",")]})
    if len(es_terms.keys()) > 0:
        es_query.append({
            "terms": es_terms,
        })
    for key, value in filters.to_stats_filters_dict().items():
        stat_query = to_es_stat_filter(key, value)
        es_query.append(stat_query) if stat_query is not None else None
    return es_query


async def find_builds(filters: schemas.BuildsFilters, sort: str, size: int, page: int):
    page = page - 1 if page > 0 else page
    es_query = to_es_filter(filters)
    logger.debug(json.dumps(es_query))

    es_sort = []
    sort_list = sort.split(",")
    if len(sort_list)%2 == 0:
        for i in range(0, len(sort_list), 2):
            es_sort.append({
                sort_list[i]: {
                    "order": sort_list[i + 1]
                }
            })
        logger.info(es_sort)
    else:
        es_sort.append({
            "stats.speed": {
                "order": "desc",
            }
        })

    query = {
            "size": size,
            "from": size * page,
            "query": {
                "bool": {
                    "filter": es_query,
                },
            },
            "sort": es_sort,
    }

    return await get_client().search(
        index="submarinebuilds",
        body=query,
    )

def to_es_stat_filter(stat_name: str, stat_filter: schemas.StatFilter):
    if stat_filter is not None:
        if stat_filter["exact"] is not None:
            return {
                "term": {
                    stat_name: stat_filter["exact"]
                },
            }
        elif stat_filter["min"] is not None or stat_filter["max"] is not None:
            return {
                "range": {
                    stat_name: {
                        "gte": 0 if stat_filter["min"] is None else stat_filter["min"],
                        "lte": 999 if stat_filter["max"] is None else stat_filter["max"],
                    },
                },
            }
    return None
