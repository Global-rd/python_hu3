from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel, Field
from typing import Optional
from database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[UUID] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=True)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[Optional[str]] = Column(String, nullable=True)


class ProductRequest(BaseModel):
    item_name: str = Field(..., min_length=5)
    quantity: int
    price: int
    category: Optional[str]


class ProductResponse(ProductRequest):
    id: UUID
