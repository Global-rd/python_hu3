from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./webshop.db"  # itt fog létreönni a webshop adatbázis, sqlite, útvonalra figyelni

engine = create_async_engine(
    DATABASE_URL, echo=True
)  # adatbázis kapcsolat fog létrejönni, a történés kiírodik consol-ra

AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)  # az adott feladatok session-okba hajtódnak végre, ezek külön működnek, külön kezeljük őket, majd erre jelzünk vissza

Base = declarative_base()  # Ettől fog örökölni minden sqlite műveleti osztály


async def get_db():  # ez a function át lesz adva minden egyes request-nek, a yield kell, hogy a context managerbe vissza tudjunk térni, majd lezárni a context-et
    async with AsyncSessionLocal() as session:
        yield session
