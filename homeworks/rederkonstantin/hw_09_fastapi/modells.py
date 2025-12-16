"""
tábla adatok:
id (egyedi azonosító, pl uuid1 által generált)
item_name (pl: morzsaporszívó)
quantity (pl: 12)
price (pl: 24900)
category (ez a fi eld legyen opcionális, pl: háztartási gép)
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel, Field
from typing import Optional
from database import Base


# database modell
class WebShop(Base):
    __tablename__ = "shopinfo"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(
        String, nullable=False
    )  # nem lehet null értéket megadni
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[str] = Column(
        String, nullable=True
    )  # (ez a fi eld legyen opcionális, pl: háztartási gép)


# pydantic modell:
class WebShopRequest(BaseModel):

    item_name: str = Field(..., min_length=5)  # a ... kötelezővé teszi a kitöltést
    quantity: int
    price: int
    category: Optional[str] = "any"


class WebShopResponse(WebShopRequest):
    id: UUID
