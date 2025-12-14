from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite async adatbázis
DATABASE_URL = "sqlite+aiosqlite:///./webshop.db"

# Async engine létrehozása
engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

# Session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base osztály a modellekhez
Base = declarative_base()


# Dependency FastAPI-hoz
# minden kérés külön session-t kap
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
