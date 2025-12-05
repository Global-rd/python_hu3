from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ProductBase(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None
    