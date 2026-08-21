from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    docs_url=f"{settings.APP_URL_PREFIX}/docs",
    redoc_url=f"{settings.APP_URL_PREFIX}/redoc",
    openapi_url=f"{settings.APP_URL_PREFIX}/openapi.json",
)

app.include_router(api_router, prefix=settings.APP_URL_PREFIX)
