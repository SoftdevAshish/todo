from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import settings
from app.core.database.database import init_db, close_db
from app.core.logger import get_logger, LOG_DIR

logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await init_db()
        logger.info(f"Database initialized...")
        print(LOG_DIR)

        yield
    except Exception as e:
        await close_db()
        logger.info(f"Database closed...")
        raise e
    finally:
        await close_db()


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    docs_url=f"{settings.APP_URL_PREFIX}/docs",
    redoc_url=f"{settings.APP_URL_PREFIX}/redoc",
    openapi_url=f"{settings.APP_URL_PREFIX}/openapi.json",
    lifespan=lifespan,
)

app.include_router(api_router, prefix=settings.APP_URL_PREFIX)
