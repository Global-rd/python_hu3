from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import WebShop, ItemRequest, ItemResponse
from database import Base, engine, get_db
from typing import List

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/webshop/", response_model=List[ItemResponse])
async def get_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WebShop))  
    items = result.scalars().all()

    return items


@app.post("/webshop/", response_model=ItemResponse)
async def add_item(item: ItemRequest, db: AsyncSession = Depends(get_db)):

    new_item = WebShop(**item.model_dump())

    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item


@app.get("/webshop/{item_id}", response_model=ItemResponse)
async def get_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    item = await get_item_by_id(item_id, db)
    return item


@app.put("/webshop/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: UUID, item_update: ItemRequest, db: AsyncSession = Depends(get_db)
):
    item = await get_item_by_id(item_id, db)

    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(item, key, value)

    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


@app.delete("/webshop/{item_id}", response_model=ItemResponse)
async def delete_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    item = await get_item_by_id(item_id, db)

    await db.delete(item)
    await db.commit()

    return True


async def get_item_by_id(item_id: UUID, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(WebShop.where(WebShop.id == str(item_id))))  # SELECT * FROM MOVIES where id = <uuid>
    items = result.scalar_one_or_none()

    if not items:
        raise HTTPException(status_code=404, detail=f"Movie id {item_id} not found")

    return items