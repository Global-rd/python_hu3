from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid1

app = FastAPI()

class Item(BaseModel):
    id: str
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

class ItemCreate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

items = []

@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: str):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
def create_item(item: ItemCreate):
    new_item = {
        "id": str(uuid1()),
        "item_name": item.item_name,
        "quantity": item.quantity,
        "price": item.price,
        "category": item.category
    }
    items.append(new_item)
    return new_item

@app.put("/items/{item_id}")
def update_item(item_id: str, updated_item: ItemCreate):
    for item in items:
        if item["id"] == item_id:
            item["item_name"] = updated_item.item_name
            item["quantity"] = updated_item.quantity
            item["price"] = updated_item.price
            item["category"] = updated_item.category
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
