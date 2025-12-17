from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import uuid1
from typing import Optional

from database import SessionLocal, engine, Base
from models import Item
from pydantic import BaseModel

app = FastAPI(title="Webshop termékek")

# táblák létrehozása
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ItemBase(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None


class ItemResponse(ItemBase):
    id: str

    class Config:
        orm_mode = True


# Minden termék
@app.get("/items", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()


# 1 termék ID alapján
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: str, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Nincs ilyen elem")
    return item


# Új termék
@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemBase, db: Session = Depends(get_db)):
    new_item = Item(
        id=str(uuid1()),
        item_name=item.item_name,
        quantity=item.quantity,
        price=item.price,
        category=item.category,
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


# Frissítés ID alapján
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: str, updated_item: ItemBase, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Nincs ilyen elem")

    item.item_name = updated_item.item_name
    item.quantity = updated_item.quantity
    item.price = updated_item.price
    item.category = updated_item.category

    db.commit()
    db.refresh(item)
    return item


# Törlés ID alapján
@app.delete("/items/{item_id}")
def delete_item(item_id: str, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Nincs ilyen elem")

    db.delete(item)
    db.commit()
    return {"message": "Törölve"}
