from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel, Field
from typing import Optional
from database import Base


# Database model
class Product(Base):
    __tablename__ = "products"

    id: Mapped[str] = Column(
        String, primary_key=True, index=True, default=lambda: str(uuid1())
    )
    item_name: Mapped[str] = Column(String, nullable=False, index=True)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[str] = Column(String, nullable=True)


# pydantic model:
class ProductRequest(BaseModel):
    item_name: str = Field(..., min_length=5, examples=["morzsaporszívó"])
    quantity: int = Field(..., ge=0, examples=[12])
    price: int = Field(..., ge=0, examples=[24900])
    category: Optional[str] = Field(
        default=None, examples=["háztartási gép"]
    )  # optional category


class ProductResponse(ProductRequest):
    id: UUID
