"""
A következő feladatban a coinGecko public API-járól kell majd adatokat kinyerned,
és ezeket elemezni Python segítségével.
A kövekező endpoint-ról “https://api.coingecko.com/api/v3/coins/markets” húzd le
a 250 legnagyobb market cap-pel rendelkező kriptovalutát (értelmezd az api
dokumentációt, két paramétert kell összesen használnod, és 1 api hívásból
megszerezhető az adat). *market cap = kibocsátott darabszám * ár
Dokumentáció: https://docs.coingecko.com/reference/coins-markets (figyelj hogy itt
a url-ben “pro-api.coingecko.com” szerepel, neked viszont simán
“api.coingecko.com” kell, így regisztráció nélkül használhatod az api-t.
Tárold el ezeket egy dataframe-ben és oldd meg a következő feladatokat pandas
segítségével:
1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található
és printeld ki.
2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát
tárold current_price alapján
4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő
sorrendbe!
5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3
értéke lehet :
a. Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop
értéke legyen "+"
b. Ha negatív, az oszlop értéke legyen "-"
c. Ha kereken 0, az érték legyen "0"
"""

import requests
import pandas as pd
import pprint

pp = pprint.PrettyPrinter(indent=4)

COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3/coins/markets"

def get_change_direction(change: float) -> str:
    """Returns the change direction symbol based on the change value."""
    if change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"

def main() -> None:
    try:
        response: requests.Response = requests.get(url=f"{COINGECKO_BASE_URL}?vs_currency=usd&per_page=250&order=market_cap_desc")
        if response.status_code != 200:
            raise Exception(f"Response was not HTTP 200, but {response.status_code}")

        df = pd.DataFrame(response.json())

        # Task 1: Count empty cells
        print("Number of empty cells per column:")
        print(df.isna().sum())
        print("-" * 30)

        # Task 2: Sum of market_cap
        market_cap_sum = df["market_cap"].sum()
        print(f"Total market cap: {market_cap_sum:,.2f} USD")
        print("-" * 30)

        # Task 3: Create top 50 dataframe
        # The API call already sorts by market cap, so we just take the first 50 rows.
        top50_df: pd.DataFrame = df.head(n=50).copy()

        # Task 4: Sort the top 50 dataframe
        top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

        # Task 5: Create 'change_direction' column
        top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(get_change_direction)

        print("Top 50 cryptocurrencies by 24h change, with 'change_direction' column:")
        print(top50_df[['id', 'current_price', 'price_change_percentage_24h', 'change_direction']])
        print("-" * 30)

    except Exception as e:
        print("Something went wrong:")
        print(e)


if __name__ == "__main__":
    main()
