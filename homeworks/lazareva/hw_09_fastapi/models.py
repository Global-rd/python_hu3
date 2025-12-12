from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel, Field
from typing import Optional
from database import Base


# database model
class WebshopShop(Base):
    __tablename__ = "inventory"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[str] = Column(String, nullable=False)

# pydantic model:
class WebshopShopRequest(BaseModel):

    item_name: str = Field(..., min_length=3)   #kötelező mező, ezt a három pont jelöli, legalább 5 karakter
    quantity: Optional[int] = 0                 #nem kötelező mező, alapértelmezett érték 0
    price: int
    category: str

class WebshopShopResponse(WebshopShopRequest):  #WebshopProductRequest-ből örököl (annak összes mezője + id)
    id: UUID        #UUID típusú id mező
