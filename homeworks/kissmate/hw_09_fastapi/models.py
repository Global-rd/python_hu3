from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel, Field
from typing import Optional
from database import Base


# database model
class Webshop(Base):
    __tablename__ = "Webshop"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quality: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[Optional[str]] = Column(String, nullable=False)
    
# pydantic model:
class WebshopRequest(BaseModel):

    item_name: str = Field(..., min_length=5)
    quality: int
    price: int
    category: Optional[str] = "none"

class WebshopResponse(WebshopRequest):
    id: UUID
