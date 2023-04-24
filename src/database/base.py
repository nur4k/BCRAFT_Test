from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.config.settings import settings


async_engine = create_async_engine(settings.url())

async_session = sessionmaker(future=True, class_=AsyncSession, bind=async_engine, expire_on_commit=False)

Base = declarative_base()
