from loguru import logger

from app import schemas
from app.core.elasticsearch import get_client


def get_filters(filters: schemas.BuildsFilters):
    logger.info(filters)


def find_builds(filters: schemas.BuildsFilters):
    size = 2
    return {
            'size': size,
            'query': {
                "bool": {
                    "filter": [
                        {
                            "terms": {
                                "slots.0": [23, 27],
                            },
                        },
                        {
                            "range": {
                                "rank": {
                                    "lte": 10,
                                },
                            },
                        },
                    ],
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
