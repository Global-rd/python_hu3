import requests
from coinGecko_info import get_top_250_cryptos
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,   
    "page": 1
}

response = requests.get(url, params=params)

if response.status_code != 200:
    print("API ERROR:", response.status_code)
    exit()

data = response.json()
df = pd.DataFrame(data)
#1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki. 

print("API SUCCESS:", len(df), "crypto")
print("-" * 50)
#2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki. 
print(df.isna().sum())
print("-" * 50)

total_market_cap = df["market_cap"].sum()
print(f"Market cap:{total_market_cap:,.0f} USD")
print("-" * 50)

#3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján 

top50_df = df.sort_values(by="current_price", ascending=False).head(50)
print("Top50 price change percentage (current price):")
print(top50_df[["name", "current_price"]].head())
print("-" * 50)

#4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe! 

top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

print("Top50 price change percentage (24h price):")
print(top50_df[["name", "price_change_percentage_24h"]].head())
print("-" * 50)

#5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet : (+ / 0 / -)

def change_direction(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(change_direction)

print("Trend of price changes: ")
print(top50_df[["name", "price_change_percentage_24h", "change_direction"]].head())
print("-" * 50)
