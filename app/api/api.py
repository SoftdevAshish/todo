from fastapi import APIRouter

from .routes.health import health_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["Health"])