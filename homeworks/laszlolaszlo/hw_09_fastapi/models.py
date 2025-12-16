from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid1, UUID
from pydantic import BaseModel, Field
from typing import Optional
from database import Base


# database model
class Item(Base):
    """
    Database model for an item in the inventory.
    """

    __tablename__ = "items"
    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid1())
    )
    item_name: Mapped[str] = mapped_column(String, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=True)


# pydantic model:
class ItemRequest(BaseModel):
    """
    Model for creating a new item.
    """

    item_name: str = Field(..., min_length=5)
    quantity: int = Field(..., ge=0)
    price: int = Field(..., ge=0)
    category: Optional[str] = None


class ItemUpdate(BaseModel):
    """
    Model for updating an item.
    """

    item_name: Optional[str] = Field(None, min_length=5)
    quantity: Optional[int] = Field(None, ge=0)
    price: Optional[int] = Field(None, ge=0)
    category: Optional[str] = None


class ItemResponse(BaseModel):
    id: UUID
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None
    model_config = {"from_attributes": True}
