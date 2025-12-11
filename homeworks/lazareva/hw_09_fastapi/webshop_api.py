# A webshop_api.py a terminálból a következő utasítással futtatható: uvicorn webshop_api:app --reload
# Előtte belépek a webshop_api.py fájl mappájába, és innen futtatom.
# Ha már elindult, akkor a terminálban megtalálom az url-t (http://127.0.0.1:8000/), 
# (http://127.0.0.1:8000/inventory/), automatikusan generált dokumentáció: http://127.0.0.1:8000/docs#/

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import WebshopShop, WebshopShopRequest, WebshopShopResponse
from database import Base, engine, get_db #get_db: minden egyes kérésnek külön session-t ad (session.id)
from typing import List

# ha még nincs meg az adatbázis, akkor hozza létre
# "yield" fogja átadni az irányítást az app-nak
# ez a lifespan = életciklus
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

# létrehozzuk a FastAPI alkalmazást
# innen már kipróbálhatom az alkalmazást :-)
# terminalból (az aktuális mappából): uvicorn movies_api:app --reload
# :app -> ez az alkalmazás neve (belépési pont)
# --reload -> automatikus újratöltés kódváltozás esetén
app = FastAPI(lifespan=lifespan)

# AsyncSession = Depends(get_db) -> külön session-okat hoz létre minden egyes kéréshez
@app.get("/inventory/", response_model=List[WebshopShopResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WebshopShop))  # SELECT * FROM INVENTORY
    products = result.scalars().all()               #.all() -> az összes találatot listába teszi    

    return products

# @app.post("/endpoint/")
@app.post("/inventory/", response_model=WebshopShopResponse)
async def add_product(product: WebshopShopRequest, db: AsyncSession = Depends(get_db)):

    new_product = WebshopShop(**product.model_dump())

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product              # visszaadom az új terméket

@app.get("/inventory/{product_id}", response_model=WebshopShopResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):

    product = await get_product_by_id(product_id, db) #db: session azonosító
 
    return product

@app.put("/inventory/{product_id}", response_model=WebshopShopResponse)
async def update_product(
    product_id: UUID, product_update: WebshopShopRequest, db: AsyncSession = Depends(get_db)
):
    product = await get_product_by_id(product_id, db)

    for key, value in product_update.model_dump(exclude_unset=False).items():   # ha exclude_unset=True: csak kötelező mezőket módosít
        setattr(product, key, value)                                            # settattr: olyan, mintha egymás alatt minden egyes mezőre meg lenne hívva: 
                                                                                # ->    inventory.item_name = product_update("item_name")

    db.add(product)             # hozzáadom a session-höz
    await db.commit()           # aztán kommitolok -- async function-okhoz kell az "await"
    await db.refresh(product)   # frissítek
    return product              # visszaadom az update-elt product-t

@app.delete("/inventory/{product_id}", response_model=bool)
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    print(product_id)
    product = await get_product_by_id(product_id, db)

    await db.delete(product)
    await db.commit()

    return True

async def get_product_by_id(product_id: UUID, db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(WebshopShop).where(WebshopShop.id == str(product_id))
    )  # SELECT * FROM inventory where id = <uuid>
    product = result.scalar_one_or_none()       # egyet ad vissza, vagy hibát, ha nem találja meg

    if not product:
        raise HTTPException(status_code=404, detail=f"id {product_id} not found")

    return product