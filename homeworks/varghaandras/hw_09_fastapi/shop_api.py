from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import Product, ProductRequest, ProductResponse
from database import engine, Base, get_db
from models import router as products_router
from fastapi.responses import RedirectResponse
from typing import List


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Webshop Products", lifespan=lifespan)
app.include_router(products_router, prefix="/items", tags=["items"])


# Root endpoint
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


async def get_product_by_id(product_id: UUID, db: AsyncSession) -> Product:
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(
            status_code=404, detail=f"Product id {product_id} not found"
        )
    return product


@app.get("/items/", response_model=List[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    products = result.scalars().all()
    return products


@app.post("/items/", response_model=ProductResponse)
async def add_product(product_in: ProductRequest, db: AsyncSession = Depends(get_db)):
    new_product = Product(**product_in.model_dump())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


@app.get("/items/{product_id}", response_model=ProductResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)
    return product


@app.put("/items/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: UUID,
    product_update: ProductRequest,
    db: AsyncSession = Depends(get_db),
):
    product = await get_product_by_id(product_id, db)

    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    await db.commit()
    await db.refresh(product)
    return product


@app.delete("/items/{product_id}", response_model=bool)
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)
    await db.delete(product)
    await db.commit()
    return True
