from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel, Field
from typing import Optional
from database import Base

# database model
class FictionalWebshop(Base):
    __tablename__ = "fictional_webshop"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)    
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[str] = Column(String, nullable=False)

# pydantic model:
class FictionalWebshopRequest(BaseModel):

    item_name: str = Field(..., min_length=5)
    quantity: int
    price: int
    category: Optional[str] = None

class FictionalWebshopResponse(FictionalWebshop):
    id: UUID
