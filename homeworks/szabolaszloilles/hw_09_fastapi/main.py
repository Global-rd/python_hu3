from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()

# --- Data Models (Pydantic) ---

# Creating a new product (id is not required here yet)
# The category field is optional.
class ProductCreate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

# Stored product (it already includes the id)
class Product(ProductCreate):
    id: str

# --- "Database" ---
# List to store products in memory
products_db: List[Product] = []

# --- Endpoints ---

# 1. List all products
@app.get("/products", response_model=List[Product])
def get_all_products():
    return products_db

# 2. Get 1 product by id
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    for product in products_db:
        if product.id == product_id:
            return product
    # If not found, raise a 404 error
    raise HTTPException(status_code=404, detail="Product not found")

# 3. Add 1 product
# No need to provide an id, it will be generated automatically
@app.post("/products", response_model=Product)
def create_product(product_in: ProductCreate):
    # Generate UUID1 for the id
    new_id = str(uuid.uuid1())
    
    # Create new product object with the generated id and incoming data
    new_product = Product(
        id=new_id,
        item_name=product_in.item_name,
        quantity=product_in.quantity,
        price=product_in.price,
        category=product_in.category
    )
    
    # Add to the "database"
    products_db.append(new_product)
    return new_product

# 4. Update 1 product by id
@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: str, product_update: ProductCreate):
    for index, product in enumerate(products_db):
        if product.id == product_id:
            # Create the updated product (keeping the original id)
            updated_product = Product(
                id=product_id,
                item_name=product_update.item_name,
                quantity=product_update.quantity,
                price=product_update.price,
                category=product_update.category
            )
            # Replace the old item in the list with the new one
            products_db[index] = updated_product
            return updated_product
            
    raise HTTPException(status_code=404, detail="Product not found")

# 5. Delete 1 product by id
@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    for index, product in enumerate(products_db):
        if product.id == product_id:
            # Remove from the list
            del products_db[index]
            return {"message": "Product successfully deleted"}
            
    raise HTTPException(status_code=404, detail="Product not found")