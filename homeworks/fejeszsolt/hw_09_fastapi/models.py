from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel, Field
from typing import Optional
from database import Base


# database model
class Product(Base):
    __tablename__ = "product"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, unique=True, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    category: Mapped[str] = Column(String, nullable=False)



# pydantic model:
class ProductRequest(BaseModel):

    item_name: str = Field(..., min_length=5)
    category: str = Field(..., min_length=5)
    price: float
    quantity: int


class ProductResponse(Product):
    id: UUID
