from fastapi import FastAPI
from uuid import uuid1
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="HW09 FastAPI CRUD App")

# ---- Pydantic modellek ----
class Item(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

class ItemWithID(Item):
    id: str

# ---- "adatbázis" memóriában ----
db: List[ItemWithID] = []

# ---- CRUD ENDPOINTS ----

# 1) Minden termék listázása
@app.get("/items", response_model=List[ItemWithID])
def list_items():
    return db

# 2) Egy termék lekérése ID alapján
@app.get("/items/{item_id}", response_model=ItemWithID)
def get_item(item_id: str):
    for item in db:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

# 3) Új termék hozzáadása
@app.post("/items", response_model=ItemWithID)
def create_item(item: Item):
    new_item = ItemWithID(id=str(uuid1()), **item.dict())
    db.append(new_item)
    return new_item

# 4) Termék frissítése ID alapján
@app.put("/items/{item_id}", response_model=ItemWithID)
def update_item(item_id: str, updated_item: Item):
    for index, item in enumerate(db):
        if item.id == item_id:
            db[index] = ItemWithID(id=item_id, **updated_item.dict())
            return db[index]
    return {"error": "Item not found"}

# 5) Termék törlése ID alapján
@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    for item in db:
        if item.id == item_id:
            db.remove(item)
            return {"message": "Item deleted"}
    return {"error": "Item not found"}