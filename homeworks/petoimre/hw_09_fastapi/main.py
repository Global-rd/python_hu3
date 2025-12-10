from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from typing import List

from models import Product, ProductRequest, ProductResponse
from database import Base, engine, get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Az adatbázis táblák létrehozása induláskor
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


# 1) Minden termék listázása
@app.get("/products/", response_model=List[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))  # SELECT * FROM products
    products = result.scalars().all()
    return products


# 2) 1 termék listázása id alapján
@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)
    return product


# 3) 1 termék hozzáadása
@app.post("/products/", response_model=ProductResponse)
async def add_product(product_req: ProductRequest, db: AsyncSession = Depends(get_db)):
    new_product = Product(**product_req.model_dump())

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product


# 4) 1 termék adatainak frissítése id alapján
@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: UUID,
    product_update: ProductRequest,
    db: AsyncSession = Depends(get_db),
):
    product = await get_product_by_id(product_id, db)

    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


# 5) 1 termék törlése id alapján
@app.delete("/products/{product_id}", response_model=ProductResponse)
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)

    # elmentjük a törölt terméket visszaküldéshez
    await db.delete(product)
    await db.commit()

    return product


# --- Segédfüggvény: lekérés id alapján ---

async def get_product_by_id(product_id: UUID, db: AsyncSession):
    result = await db.execute(
        select(Product).where(Product.id == str(product_id))
    )  # SELECT * FROM products WHERE id = <uuid>

    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail=f"Product id {product_id} not found")

    return product