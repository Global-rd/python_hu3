from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid1

app = FastAPI(title="Termékek")


class ItemBase(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None


class Item(ItemBase):
    id: str


# Adatállomány

items_db: List[Item] = []


# CRUD endpointok


# Minden termék listázása
@app.get("/items", response_model=List[Item])
def get_all_items():
    return items_db


# 1 termék lekérése ID alapján
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="nincs ilyen ID-jú termék")


# Új termék hozzáadása (ID automatikus)


@app.post("/items", response_model=Item)
def create_item(item: ItemBase):
    new_item = Item(
        id=str(uuid1()),
        item_name=item.item_name,
        quantity=item.quantity,
        price=item.price,
        category=item.category,
    )
    items_db.append(new_item)
    return new_item


# Termék frissítése ID alapján
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, updated_item: ItemBase):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            new_item = Item(
                id=item_id,
                item_name=updated_item.item_name,
                quantity=updated_item.quantity,
                price=updated_item.price,
                category=updated_item.category,
            )
            items_db[index] = new_item
            return new_item
    raise HTTPException(status_code=404, detail="nincs ilyen termék")


# Termék törlése ID alapján
@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            return {"message": "termék törölve"}
    raise HTTPException(status_code=404, detail="nincs mit törölni")
