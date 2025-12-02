from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import Movie, MovieRequest, MovieResponse
from database import Base, engine, get_db
from typing import List


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/movies/", response_model=List[MovieResponse])
async def get_movies(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie))  # SELECT * FROM MOVIES
    movies = result.scalars().all()

    return movies


@app.post("/movies/", response_model=MovieResponse)
async def add_movie(movie: MovieRequest, db: AsyncSession = Depends(get_db)):

    new_movie = Movie(**movie.model_dump())

    db.add(new_movie)
    await db.commit()
    await db.refresh(new_movie)

    return new_movie


@app.get("/movies/{movie_id}", response_model=MovieResponse)
async def get_movie(movie_id: UUID, db: AsyncSession = Depends(get_db)):
    movie = await get_movie_by_id(movie_id, db)
    return movie


@app.put("/movies/{movie_id}", response_model=MovieResponse)
async def update_movie(
    movie_id: UUID, movie_update: MovieRequest, db: AsyncSession = Depends(get_db)
):
    movie = await get_movie_by_id(movie_id, db)

    for key, value in movie_update.model_dump(exclude_unset=True).items():
        setattr(movie, key, value)

    db.add(movie)
    await db.commit()
    await db.refresh(movie)
    return movie


@app.delete("/movies/{movie_id}", response_model=MovieResponse)
async def delete_movie(movie_id: UUID, db: AsyncSession = Depends(get_db)):
    movie = await get_movie_by_id(movie_id, db)

    await db.delete(movie)
    await db.commit()

    return True


async def get_movie_by_id(movie_id: UUID, db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Movie).where(Movie.id == str(movie_id))
    )  # SELECT * FROM MOVIES where id = <uuid>
    movie = result.scalar_one_or_none()

    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie id {movie_id} not found")

    return movie
