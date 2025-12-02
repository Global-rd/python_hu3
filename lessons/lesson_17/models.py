from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel, Field
from typing import Optional
from database import Base


# database model
class Movie(Base):
    __tablename__ = "movies"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    title: Mapped[str] = Column(String, nullable=False)
    genre: Mapped[str] = Column(String, nullable=False)
    year: Mapped[int] = Column(Integer, nullable=False)
    length_in_mins: Mapped[int] = Column(Integer, nullable=False)
    rating: Mapped[int] = Column(Integer, nullable=False)


# pydantic model:
class MovieRequest(BaseModel):

    title: str = Field(..., min_length=5)
    genre: str
    year: int
    length_in_mins: int
    rating: Optional[int] = 0


class MovieResponse(MovieRequest):
    id: UUID
