from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
import uuid

app = FastAPI(title="Endre Webshopja (API)")


class Item(BaseModel):
    id: str
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None


class ItemCreate(BaseModel):
    item_name: str = Field(..., example="kávéfőző")
    quantity: int = Field(..., example=12)
    price: int = Field(..., example=24900)
    category: Optional[str] = Field(None, example="háztartási gép")


db: List[Item] = []


@app.get("/items", response_model=List[Item])
def list_items():
    return db


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Nem található termék")


@app.post("/items", response_model=Item)
def create_item(data: ItemCreate):
    new_item = Item(
        id=str(uuid.uuid1()),
        item_name=data.item_name,
        quantity=data.quantity,
        price=data.price,
        category=data.category
    )
    db.append(new_item)
    return new_item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, data: ItemCreate):
    for i, item in enumerate(db):
        if item.id == item_id:
            updated = Item(
                id=item_id,
                item_name=data.item_name,
                quantity=data.quantity,
                price=data.price,
                category=data.category
            )
            db[i] = updated
            return updated

    raise HTTPException(status_code=404, detail="Nem található termék")


@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    for i, item in enumerate(db):
        if item.id == item_id:
            db.pop(i)
            return {"message": "Termék sikeresen törölve"}

    raise HTTPException(status_code=404, detail="Nem található termék")
