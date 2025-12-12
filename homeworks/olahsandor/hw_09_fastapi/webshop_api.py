from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import Article, ArticleRequest, ArticleResponse
from typing import List


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Táblák létrehozása
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

async def get_article_by_id(article_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Article).where(Article.id == str(article_id))
    )
    article = result.scalar_one_or_none()

    if not article:
        raise HTTPException(status_code=404, detail=f"article id {article_id} not found")

    return article

@app.get("/articles/", response_model=List[ArticleResponse])
async def get_article(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Article))
    articles = result.scalars().all()
    return articles


@app.post("/articles/", response_model=ArticleResponse)
async def add_article(article: ArticleRequest, db: AsyncSession = Depends(get_db)):
    new_article = Article(**article.model_dump())

    db.add(new_article)
    await db.commit()
    await db.refresh(new_article)

    return new_article


@app.get("/articles/{article_id}", response_model=ArticleResponse)
async def get_article_by_id_endpoint(article_id: UUID, db: AsyncSession = Depends(get_db)):
    article = await get_article_by_id(article_id, db)
    return article


@app.put("/articles/{article_id}", response_model=ArticleResponse)
async def update_article(
    article_id: UUID, article_update: ArticleRequest, db: AsyncSession = Depends(get_db)
):
    article = await get_article_by_id(article_id, db)

    for key, value in article_update.model_dump(exclude_unset=True).items():
        setattr(article, key, value)

    db.add(article)
    await db.commit()
    await db.refresh(article)
    return article


@app.delete("/articles/{article_id}", response_model=ArticleResponse)
async def delete_article(article_id: UUID, db: AsyncSession = Depends(get_db)):
    article = await get_article_by_id(article_id, db)

    await db.delete(article)
    await db.commit()

    return article