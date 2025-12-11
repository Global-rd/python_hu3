# ez egy MINTA database.py fájl, ami az adatbázis kapcsolatot kezeli
# a későbbiekben, ha akarjuk, akkor szinte egy az egyben  majd importálhatjuk ezt a fájlt az alkalmazásunkba
# 
# Az SQLAlchemy könyvtárat használjuk az adatbázis kezelésére
# és az SQLite adatbázist használjuk példaként.
# Az aszinkron működéshez az async SQLAlchemy modult használjuk.
# Az adatbázis URL-je egy SQLite fájlra mutat, de ezt könnyen módosíthatjuk más adatbázisokra is.
# Az adatbázis kapcsolat létrehozásához egy aszinkron motort hozunk létre,
# és egy aszinkron munkamenet gyárat definiálunk.
# A Base osztályt használjuk az adatbázis modellek definiálásához.
# Végül egy get_db függvényt definiálunk, ami egy aszinkron munkamenetet ad vissza,
# amit a FastAPI útvonalakban használhatunk az adatbázis műveletekhez.

# avirtuális környezethez: env\scripts\activate (terminálban) -> * (env) PS C:\...
# telepítés: pip install sqlalchemy aiosqlite uvicorn

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./webshop.db"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
