from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel, Field
from typing import Optional
from db import Base

# database model
class Article(Base):
    __tablename__ = "articles"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[Optional[str]] = Column(String, nullable=True, default=None)

# pydantic model:
class ArticleRequest(BaseModel):
    item_name: str 
    category: Optional[str] = None
    price: int
    quantity: int

class ArticleResponse(BaseModel):
    id: str
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None