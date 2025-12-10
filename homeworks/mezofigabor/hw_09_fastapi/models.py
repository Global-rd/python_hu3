from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel, Field
from typing import Optional
from database import Base


# database model
class Product(Base):
    __tablename__ = "products"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[int] = Column(Integer, nullable=False)


# pydantic model:
class ProductRequest(BaseModel):

    item_name: str = Field(..., min_length=5)
    quantity: int
    price: int
    category: Optional[int] = 0


class ProductResponse(ProductRequest):
    id: UUID
