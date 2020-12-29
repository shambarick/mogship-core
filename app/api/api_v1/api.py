from fastapi import APIRouter

from app.api.api_v1.endpoints import ranks, sectors

api_router = APIRouter()
api_router.include_router(sectors.router, prefix="/sectors")
api_router.include_router(ranks.router, prefix="/ranks")
