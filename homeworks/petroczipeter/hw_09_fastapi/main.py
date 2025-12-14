from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# -------------------------------------------------
# DATABASE CONFIG
# -------------------------------------------------

DATABASE_URL = "sqlite:///./items.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# -------------------------------------------------
# SQLALCHEMY MODEL
# -------------------------------------------------

class ItemDB(Base):
    __tablename__ = "items"

    id = Column(String, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

# -------------------------------------------------
# PYDANTIC MODELS
# -------------------------------------------------

class Item(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

class ItemWithID(Item):
    id: str

    class Config:
        orm_mode = True

# -------------------------------------------------
# DB SESSION DEPENDENCY
# -------------------------------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------------------------
# FASTAPI APP
# -------------------------------------------------

app = FastAPI(title="HW09 FastAPI CRUD App")

# -------------------------------------------------
# CRUD ENDPOINTS
# -------------------------------------------------

# 1️ List all items
@app.get("/items", response_model=List[ItemWithID])
def list_items(db: Session = Depends(get_db)):
    return db.query(ItemDB).all()

# 2 Get item by ID
@app.get("/items/{item_id}", response_model=ItemWithID)
def get_item(item_id: str, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# 3️ Create item
@app.post("/items", response_model=ItemWithID)
def create_item(item: Item, db: Session = Depends(get_db)):
    db_item = ItemDB(
        id=str(uuid4()),
        item_name=item.item_name,
        quantity=item.quantity,
        price=item.price,
        category=item.category
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# 4️ Update item
@app.put("/items/{item_id}", response_model=ItemWithID)
def update_item(item_id: str, updated_item: Item, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item.item_name = updated_item.item_name
    item.quantity = updated_item.quantity
    item.price = updated_item.price
    item.category = updated_item.category

    db.commit()
    db.refresh(item)
    return item

# 5️ Delete item
@app.delete("/items/{item_id}")
def delete_item(item_id: str, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}