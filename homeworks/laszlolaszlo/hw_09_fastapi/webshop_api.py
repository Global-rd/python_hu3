from uuid import UUID
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from contextlib import asynccontextmanager
from models import Item, ItemRequest, ItemResponse, ItemUpdate
from database import Base, engine, get_db
from typing import List


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Create the database tables on startup.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


# Create FastAPI app
app = FastAPI(lifespan=lifespan)


@app.get("/items/", response_model=List[ItemResponse])
async def get_items(db: AsyncSession = Depends(get_db)) -> List[Item]:
    """
    Retrieve all items from the inventory.
    """
    result = await db.execute(select(Item))  # SELECT * FROM ITEMS
    return list(result.scalars().all())


@app.post("/items/", response_model=ItemResponse)
async def add_item(item: ItemRequest, db: AsyncSession = Depends(get_db)) -> Item:
    """
    Add a new item to the inventory.
    """
    new_item = Item(**item.model_dump())

    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item


@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: UUID, db: AsyncSession = Depends(get_db)) -> Item:
    """
    Retrieve a specific item by its ID.
    """
    item = await get_item_by_id(item_id, db)
    return item


@app.patch("/items/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: UUID, item_update: ItemUpdate, db: AsyncSession = Depends(get_db)
) -> Item:
    """
    Update an existing item in the inventory.
    """
    item = await get_item_by_id(item_id, db)

    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(item, key, value)

    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: UUID, db: AsyncSession = Depends(get_db)) -> None:
    """
    Delete an item from the inventory.
    """
    item = await get_item_by_id(item_id, db)
    await db.delete(item)
    await db.commit()
    return None


async def get_item_by_id(item_id: UUID, db: AsyncSession) -> Item:
    """
    Helper function to retrieve an item by its ID.
    """
    result = await db.execute(
        select(Item).where(Item.id == str(item_id))
    )  # SELECT * FROM ITEMS where id = <uuid>
    item = result.scalar_one_or_none()

    if not item:
        raise HTTPException(status_code=404, detail=f"Item id {item_id} not found")

    return item
