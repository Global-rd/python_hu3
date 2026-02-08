from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from typing import List

from models import WebshopShop, WebshopShopRequest, WebshopShopResponse
from database import Base, engine, get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/inventory/", response_model=List[WebshopShopResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WebshopShop))
    return result.scalars().all()


@app.post("/inventory/", response_model=WebshopShopResponse)
async def add_product(product: WebshopShopRequest, db: AsyncSession = Depends(get_db)):
    new_product = WebshopShop(**product.model_dump())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


@app.get("/inventory/{product_id}", response_model=WebshopShopResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    return await get_product_by_id(product_id, db)


@app.put("/inventory/{product_id}", response_model=WebshopShopResponse)
async def update_product(
    product_id: UUID,
    product_update: WebshopShopRequest,
    db: AsyncSession = Depends(get_db)
):
    product = await get_product_by_id(product_id, db)
    for key, value in product_update.model_dump().items():
        setattr(product, key, value)
    await db.commit()
    await db.refresh(product)
    return product


@app.delete("/inventory/{product_id}", response_model=bool)
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)
    await db.delete(product)
    await db.commit()
    return True


async def get_product_by_id(product_id: UUID, db: AsyncSession):
    result = await db.execute(
        select(WebshopShop).where(WebshopShop.id == str(product_id))
    )
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail=f"id {product_id} not found")
    return product
