from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import FictionalWebshop, FictionalWebshopRequest, FictionalWebshopResponse
from database import Base, engine, get_db
from typing import List


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/fictional_webshop/", response_model=List[FictionalWebshopResponse])
async def get_item(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(FictionalWebshop))  # SELECT * FROM FICTIONAL_WEBSHOP
    items = result.scalars().all()

    return items

@app.get("/fictional_webshop/{item_id}", response_model=FictionalWebshopResponse)
async def get_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    item = await get_item_by_id(item_id, db)
    return item

@app.post("/fictional_webshop/", response_model=FictionalWebshopResponse)
async def add_item(item: FictionalWebshopRequest, db: AsyncSession = Depends(get_db)):

    new_item = FictionalWebshop(**item.model_dump())

    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item

@app.put("/fictional_webshop/{item_id}", response_model=FictionalWebshopResponse)
async def update_item(
    item_id: UUID, item_update: FictionalWebshopRequest, db: AsyncSession = Depends(get_db)
):
    item = await get_item_by_id(item_id, db)

    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(item, key, value)

    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item

@app.delete("/fictional_webshop/{item_id}", response_model=FictionalWebshopResponse)
async def delete_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    item = await get_item_by_id(item_id, db)

    await db.delete(item)
    await db.commit()

    return True

async def get_item_by_id(item_id: UUID, db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(FictionalWebshop).where(FictionalWebshop.id == str(item_id))
    )  # SELECT * FROM FICTIONAL_WEBSHOP where id = <uuid>
    item = result.scalar_one_or_none()

    if not item:
        raise HTTPException(status_code=404, detail=f"Item id {item_id} not found")

    return item


