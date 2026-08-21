import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.core.database.models import load_models
from app.core.logger import get_logger

logger = get_logger()

engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800
)
async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncSession[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Database session error: {e}")
            session.rollback()
            raise


async def init_db():
    try:
        load_models()
        logger.info("Models load successfully....")

        max_retries = 3
        retry_delay = 2

        for attempt in range(max_retries):
            try:
                async with engine.begin() as conn:
                    await conn.execute(text("SELECT 1"))
                logger.info("Database connection verified...")
                break
            except Exception as e:
                if attempt == max_retries - 1:
                    logger.error(f"Failed to verify database connection after {max_retries} attempts, cause: {e}")
                    raise
                logger.error(f"Database connection {max_retries} attempts, cause: {e}")
                await asyncio.sleep(retry_delay * (attempt + 1))
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        raise

async def close_db():
    await engine.dispose()
    logger.info("Database connection closed")