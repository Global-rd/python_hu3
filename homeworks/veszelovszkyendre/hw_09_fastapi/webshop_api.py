import uuid
from contextlib import asynccontextmanager
from typing import Optional, List
from collections.abc import AsyncGenerator
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field
from sqlalchemy import String, Integer, select
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """SQLAlchemy ORM base class"""
    pass


class ItemORM(Base):
    __tablename__ = "items"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, index=True
    )
    item_name: Mapped[str] = mapped_column(
        String, nullable=False
    )
    quantity: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    price: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    category: Mapped[Optional[str]] = mapped_column(
        String, nullable=True
    )


DATABASE_URL = "sqlite+aiosqlite:///./webshop.db"

engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # A Debug-olás miatt tettem bele, ha kellene.
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Induláskor: a táblák létrehozása, ha még nem léteznek.
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Leálláskor: ide jöhet a Cleanup, ha kell.


app = FastAPI(
    title="Endre Webshopja (API)",
    lifespan=lifespan
)


@app.get("/", include_in_schema=False)
async def root():
    """Főoldal: irány a Swagger UI."""
    return RedirectResponse(url="/docs")


class Item(BaseModel):
    id: str
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

    class Config:
        from_attributes = True


class ItemCreate(BaseModel):
    item_name: str = Field(..., example="kávéfőző")
    quantity: int = Field(..., example=12)
    price: int = Field(..., example=24900)
    category: Optional[str] = Field(None, example="háztartási gép")


@app.get("/items", response_model=List[Item])
async def list_items(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(ItemORM))
    items = result.scalars().all()
    return items


@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: str, session: AsyncSession = Depends(get_session)):
    item = await session.get(ItemORM, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Nem található termék")
    return item


@app.post("/items", response_model=Item)
async def create_item(
    data: ItemCreate,
    session: AsyncSession = Depends(get_session),
):
    new_item = ItemORM(
        id=str(uuid.uuid1()),
        item_name=data.item_name,
        quantity=data.quantity,
        price=data.price,
        category=data.category,
    )
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item


@app.put("/items/{item_id}", response_model=Item)
async def update_item(
    item_id: str,
    data: ItemCreate,
    session: AsyncSession = Depends(get_session),
):
    item = await session.get(ItemORM, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Nem található termék")

    item.item_name = data.item_name
    item.quantity = data.quantity
    item.price = data.price
    item.category = data.category

    await session.commit()
    await session.refresh(item)
    return item


@app.delete("/items/{item_id}")
async def delete_item(
    item_id: str,
    session: AsyncSession = Depends(get_session),
):
    item = await session.get(ItemORM, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Nem található termék")

    await session.delete(item)
    await session.commit()
    return {"message": "Termék sikeresen törölve"}
