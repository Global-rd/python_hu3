from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from typing import List
from product import Product, ProductBase

app = FastAPI()

products: List[Product] = []

@app.get("/products")
def list_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: UUID):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products")
def create_product(product_data: ProductBase):
    new_id = uuid4()

    created_product = Product(
        id=new_id,
        item_name=product_data.item_name,
        quantity=product_data.quantity,
        price=product_data.price,
        category=product_data.category
    )

    products.append(created_product)
    return created_product


@app.put("/products/{product_id}")
def update_product(product_id: UUID, updated_data: ProductBase):
    for product in products:
        if product.id == product_id:
            product.item_name = updated_data.item_name
            product.quantity = updated_data.quantity
            product.price = updated_data.price
            product.category = updated_data.category
            return product

    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}")
def delete_product(product_id: UUID):
    for product in products:
        if product.id == product_id:
            products.remove(product)
            return {"message": "Product deleted successfully"}

    raise HTTPException(status_code=404, detail="Product not found")





