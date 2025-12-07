from contextlib import asynccontextmanager
from typing import List
from uuid import UUID, uuid4

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from product import Product, ProductBase
from database import Base, engine, get_session
from models import Product as ProductModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


def to_schema(db_product: ProductModel) -> Product:
    return Product(
        id=UUID(db_product.id),
        item_name=db_product.item_name,
        quantity=db_product.quantity,
        price=db_product.price,
        category=db_product.category,
    )


@app.get("/products", response_model=List[Product])
async def list_products(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(ProductModel))
    products = result.scalars().all()
    return [to_schema(p) for p in products]


@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: UUID, session: AsyncSession = Depends(get_session)):
    db_product = await session.get(ProductModel, str(product_id))
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return to_schema(db_product)


@app.post("/products", response_model=Product)
async def create_product(product_data: ProductBase, session: AsyncSession = Depends(get_session)):
    new_id = uuid4()

    db_product = ProductModel(
        id=str(new_id),
        item_name=product_data.item_name,
        quantity=product_data.quantity,
        price=product_data.price,
        category=product_data.category,
    )

    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)
    return to_schema(db_product)


@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: UUID, updated_data: ProductBase, session: AsyncSession = Depends(get_session)):
    db_product = await session.get(ProductModel, str(product_id))
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db_product.item_name = updated_data.item_name
    db_product.quantity = updated_data.quantity
    db_product.price = updated_data.price
    db_product.category = updated_data.category

    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)
    return to_schema(db_product)


@app.delete("/products/{product_id}")
async def delete_product(product_id: UUID, session: AsyncSession = Depends(get_session)):
    db_product = await session.get(ProductModel, str(product_id))
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    await session.delete(db_product)
    await session.commit()
    return {"detail": "Product deleted"}






