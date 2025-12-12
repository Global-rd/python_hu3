from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import Webshop, WebshopRequest, WebshopResponse
from database import Base, engine, get_db
from typing import List

app = FastAPI()

@app.post("/webshop/", response_model=WebshopResponse)

# Create a new product
async def create_product(product: WebshopRequest, db: AsyncSession = Depends(get_db)):
    new_product = Webshop(
        item_name=product.item_name,
        quality=product.quality,
        price=product.price,
        category=product.category
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return WebshopResponse(
        id=new_product.id,
        item_name=new_product.item_name,
        quality=new_product.quality,
        price=new_product.price,
        category=new_product.category
    )

#List all products
@app.get("/webshop/", response_model=List[WebshopResponse])
async def list_products(db: AsyncSession = Depends(get_db)) -> List[WebshopResponse]:
    result = await db.execute(select(Webshop))
    products = result.scalars().all()
    return [
        WebshopResponse(
            id=product.id,
            item_name=product.item_name,
            quality=product.quality,
            price=product.price,
            category=product.category
        ) for product in products
    ]
   
#List a product by id
@app.get("/webshop/{product_id}", response_model=WebshopResponse)
async def get_product(product_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Webshop).where(Webshop.id == product_id))
    product = result.scalar_one_or_none()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return WebshopResponse(
        id=product.id,
        item_name=product.item_name,
        quality=product.quality,
        price=product.price,
        category=product.category
    )

# Update a product by id
@app.put("/webshop/{product_id}", response_model=WebshopResponse)
async def update_product(product_id: str, updated_product: WebshopRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Webshop).where(Webshop.id == product_id))
    product = result.scalar_one_or_none()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product.item_name = updated_product.item_name
    product.quality = updated_product.quality
    product.price = updated_product.price
    product.category = updated_product.category
    
    await db.commit()
    await db.refresh(product)
    
    return WebshopResponse(
        id=product.id,
        item_name=product.item_name,
        quality=product.quality,
        price=product.price,
        category=product.category
    )

# Delete a product by id
@app.delete("/webshop/{product_id}")
def delete_product(product_id: str):
    return {"message": f"Product with id {product_id} has been deleted."}

