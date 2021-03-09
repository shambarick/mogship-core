from loguru import logger

from app import schemas
from app.core.elasticsearch import get_client


def to_es_filter(filters: schemas.BuildsFilters):
    """TODO curse thing, fix it"""
    logger.debug(filters)
    es_query = []
    if filters.slot0 is not None:
        es_query.append({
            "terms": {
                "slots.0": list(map(lambda x: int(x), filters.slot0.split(","))),
            },
        })
    if filters.to_filters_dict().get("rank") is not None:
        if filters.to_filters_dict().get("rank")["exact"] is not None:
            es_query.append({
                "term": {
                    "rank": filters.to_filters_dict().get("rank")["exact"]
                },
            })
        elif filters.to_filters_dict().get("rank")["min"] is not None or filters.to_filters_dict().get("rank")["max"] is not None:
            es_query.append({
                "range": {
                    "rank": {
                        "gte": 0 if filters.to_filters_dict().get("rank")["min"] is None else filters.to_filters_dict().get("rank")["min"],
                        "lte": 999 if filters.to_filters_dict().get("rank")["max"] is None else filters.to_filters_dict().get("rank")["max"],
                    },
                },
            })
    return es_query


def find_builds(filters: schemas.BuildsFilters, size: int, page: int):
    page = page - 1 if page > 0 else page
    es_query = to_es_filter(filters)
    logger.debug(es_query)
    return {
            'size': size,
            'from': size * page,
            'query': {
                "bool": {
                    "filter": es_query,
                },
            },
            "sort": [
                {
                    "stats.speed": {
                        "order": "DESC"
                    },
                },
            ]
    }
