from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base
from models import Item
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid1

Base.metadata.create_all(bind=engine)

app = FastAPI()


class ItemCreate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

class ItemResponse(ItemCreate):
    id: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/items", response_model=List[ItemResponse])
def get_all_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: str, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(id=str(uuid1()), **item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: str, updated_item: ItemCreate, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.item_name = updated_item.item_name
    item.quantity = updated_item.quantity
    item.price = updated_item.price
    item.category = updated_item.category
    db.commit()
    db.refresh(item)
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: str, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}
