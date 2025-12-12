# FastPI Házi Feladat

## Leírás

Hozz létre egy FastAPI app-ot ami egy képzeletbeli webshop termék
nyílvántartójaként működik az alapvető CRUD endpoint-okkal.

Az adatbázis modell tartalmazza a következő oszlopokat (állíts be primary key-t is):

- id (egyedi azonosító, pl uuid1 által generált)
- item_name (pl: morzsaporszívó)
- quantity (pl: 12)
- price (pl: 24900)
- category (ez a field legyen opcionális, pl: háztartási gép)

A típusokat válaszd meg a bennük tárolt adatoknak megfelelően. Az endpoint-ok
segítségével a következőkre kell alkalmasnak lennie az app-nak:

- Minden termék listázása
- 1 termék listázása id alapján
- 1 termék hozzáadása (ne kelljen id-t megadni, de a response-ban legyen benne miután létrejött)
- 1 termék adatainak frissítése id alapján
- 1 termék törlése id alapján

[
  {
    "item_name": "1 kg teljes kiőrlésű liszt",
    "quantity": 100,
    "price": 950,
    "category": "tartós élelmiszer",
    "id": "6a13107a-d724-11f0-b58c-cbaae1cfe9c5"
  },
  {
    "item_name": "Pisztácia",
    "quantity": 0,
    "price": 950,
    "category": "Olajos mag",
    "id": "94f96afe-d725-11f0-bdd8-47fcab1162eb"
  },
  {
    "item_name": "Körte (kg)",
    "quantity": 20,
    "price": 854,
    "category": "Gyümölcs",
    "id": "9f472460-d725-11f0-bdd8-47fcab1162eb"
  }
]
