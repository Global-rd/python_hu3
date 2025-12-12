# product.py
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class ProductBase(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None


class Product(ProductBase):
    id: UUID

    