from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from modells import WebShop, WebShopRequest, WebShopResponse
from database import Base, engine, get_db
from typing import List


@asynccontextmanager  # mikor elindul az alkalmazás, történjen valami
async def lifespan(app: FastAPI):  #
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get(
    "/products/", response_model=List[WebShopResponse]
)  # Fogadjuk a kérést, hogy az összes termékre kíváncsiak a webshop-ban,
# opcionálisan visszaadjuk 'response_modell'-ben megadott adatokat, ami minden adatot jelent az adatbázisból
async def get_products(
    db: AsyncSession = Depends(get_db),
):  # itt érjük el, hogy minden request külön db session-ban fusson
    result = await db.execute(
        select(WebShop)
    )  # SELECT * FROM WEBSHOP db utasítás asyncron módon, mert időbe telhet...
    products = result.scalars().all()

    return products


@app.post(
    "/products/", response_model=WebShopResponse
)  # hozzáadunk egy terméket a db-hez
async def add_product(product: WebShopRequest, db: AsyncSession = Depends(get_db)):

    new_product = WebShop(**product.model_dump())  # létrehozom az új terméket

    db.add(new_product)  # hozzáadom az adatbázishoz
    await db.commit()  # véglegesítem a db beírást
    await db.refresh(new_product)  # frissítem az objektumot
    return new_product  # fisszaadom az új elem adatait


@app.get("/products/{product_id}", response_model=WebShopResponse)
async def get_products(
    product_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(WebShop).where(WebShop.id == str(product_id)))
    # select * from webshop where id = <UUID>
    product = result.scalar_one_or_none()

    if not product:  # hibát kezelünk, ha nincs iyen id-s termék
        raise HTTPException(
            status_code=404, detail=f"Product id {product_id} not found."
        )

    return product


@app.put("/products/{product_id}", response_model=WebShopResponse)
async def update_product(
    product_id: UUID, product_update: WebShopRequest, db: AsyncSession = Depends(get_db)
):

    product = await get_product_by_id(product_id, db)

    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def get_product_by_id(product_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WebShop).where(WebShop.id == str(product_id)))
    # select * from webshop where id = <UUID>
    product = result.scalar_one_or_none()

    if not product:  # hibát kezelünk, ha nincs iyen id-s termék
        raise HTTPException(
            status_code=404, detail=f"Product id {product_id} not found."
        )

    return product


@app.delete("/products/{product_id}", response_model=WebShopResponse)
async def update_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id(product_id, db)
    await db.delete(product)
    await db.commit()
    return product


# az alábbi utasítás az uvicorn telepített asgi asyncron protokol szerint működő szerver,
# az uvicorn parancsal hivatkozunk az alkalmazásra, az app változóra, ami az alkalmazás belépési pontja.
# Gyakorlatilag ezzel hozzuk működésbe az alkalmazásunkat, látjuk mi történik, mikozben változtatunk rajta dolgokat.
# --reload csinálja, hogy mindig mentés után frissüljenek az alkalmazások, mindig látjuk a változást, ha rissítjük a böngészőt.
# ezt futtatni, hogy menjen az app:

# PS C:\Users\konstantin.reder\python_hu3\homeworks\rederkonstantin\hw_09_fastapi> uvicorn webshop:app --reload
# az elérési útra figyleni kell, meg a szintaktikára.... :)
