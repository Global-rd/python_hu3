# main.py
import uuid
from typing import List
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from db import get_db, init_db

from models import Product, ProductCreate, ProductResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/products", response_model=List[ProductResponse])
async def get_all_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    products = result.scalars().all()
    return products


@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str, db: AsyncSession = Depends(get_db)):
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products", response_model=ProductResponse)
async def create_product(product_in: ProductCreate, db: AsyncSession = Depends(get_db)):
   
    new_product = Product(**product_in.model_dump())
    
   
    if not new_product.id:
        new_product.id = str(uuid.uuid1())

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, product_update: ProductCreate, db: AsyncSession = Depends(get_db)):
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product.item_name = product_update.item_name
    product.quantity = product_update.quantity
    product.price = product_update.price
    product.category = product_update.category
    
    await db.commit()
    await db.refresh(product)
    return product


@app.delete("/products/{product_id}")
async def delete_product(product_id: str, db: AsyncSession = Depends(get_db)):
    product = await db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
        
    await db.delete(product)
    await db.commit()
    return {"message": "Product successfully deleted"}