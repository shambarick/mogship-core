from fastapi import APIRouter

from app.api.api_v1.endpoints import airship, submarine


api_router = APIRouter()
api_router.include_router(airship.router, prefix="/airship")
api_router.include_router(submarine.router, prefix="/submarine")
