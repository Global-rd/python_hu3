from typing import Optional
from uuid import UUID, uuid1

from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field

from database import Base


# -------------------------
# SQLAlchemy adatbázis modell
# -------------------------
class WebshopShop(Base):
    __tablename__ = "inventory"

    id = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=True)   # opcionális mező


# -------------------------
# Pydantic modellek
# -------------------------
class WebshopShopRequest(BaseModel):
    item_name: str = Field(..., min_length=3)
    quantity: Optional[int] = 0
    price: int
    category: Optional[str] = None


class WebshopShopResponse(WebshopShopRequest):
    id: UUID
