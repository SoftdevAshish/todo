from fastapi import APIRouter

health_router = APIRouter(prefix="/health")

@health_router.get("/")
async def health():
    return {"status": "ok"}

