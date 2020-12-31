from fastapi import APIRouter

from app.api.api_v1.endpoints import part_types, parts, ranks, sectors

api_router = APIRouter()
api_router.include_router(sectors.router, prefix="/sectors")
api_router.include_router(ranks.router, prefix="/ranks")
api_router.include_router(parts.router, prefix="/parts")
api_router.include_router(part_types.router, prefix="/part-types")
