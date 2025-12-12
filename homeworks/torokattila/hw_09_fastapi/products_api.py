from unittest import result
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import Product, ProductRequest, ProductResponse
from database import get_db, Base, engine
from typing import List


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/products/", response_model=List[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    products = result.scalars().all()
    return products


@app.post("/products/", response_model=ProductResponse)
async def add_product(
    product_request: ProductRequest, db: AsyncSession = Depends(get_db)
):
    new_product = Product(**product_request.model_dump())

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_products(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)
    return product


@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: UUID, product_update: ProductRequest, db: AsyncSession = Depends(get_db)
):

    product = await get_product_by_id(product_id, db)
    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


@app.delete("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)

    await db.delete(product)
    await db.commit()

    return True


async def get_product_by_id(product_id: UUID, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    products = result.scalar_one_or_none()
    if products is None:
        raise HTTPException(
            status_code=404, detail=f"Product id: {product_id} not found"
        )

    return products
