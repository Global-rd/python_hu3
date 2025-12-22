# models.py
import uuid
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer
from db import Base  


class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid1()))
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=True)



class ProductBase(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: str

    
    class Config:
        from_attributes = True