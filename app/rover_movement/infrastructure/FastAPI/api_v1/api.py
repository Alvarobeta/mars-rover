from fastapi import APIRouter

from app.rover_movement.infrastructure.FastAPI.api_v1.endpoints import movement

api_router = APIRouter()
api_router.include_router(movement.router, tags=["genericendpoint"])
