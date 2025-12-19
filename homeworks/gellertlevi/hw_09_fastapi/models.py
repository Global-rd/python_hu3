from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.sqlite import TEXT
from db import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=True)
