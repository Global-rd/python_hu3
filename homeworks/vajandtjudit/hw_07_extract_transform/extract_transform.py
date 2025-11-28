import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}
#Lekérés API-tól
response = requests.get(url, params=params)
data = response.json()

#Dataframe létrehozása
df = pd.DataFrame(data)

print("----- 1. FELADAT: Üres cellák száma oszloponként -----")
print(df.isnull().sum())
print("\n")

#market_cap összeg meghatározása

total_market_cap = df["market_cap"].sum()
print("----- 2. FELADAT: A teljes market_cap összege -----")
print(total_market_cap)
print("\n")

#új dataframe-et top50
top50_df = df.sort_values("current_price", ascending=False).head(50)

#Rendezés price_change_percentage_24h alapján csökkenő sorrendbe
top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)

#új oszlop
def get_direction(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"
top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(get_direction)
print("----- 3-4-5. FELADAT: top50_df eredménye -----")
print(top50_df[["id", "current_price", "price_change_percentage_24h", "change_direction"]].head(15))

    
    
    
