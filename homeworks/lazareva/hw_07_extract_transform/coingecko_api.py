import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

# TOP 250 market cap desc

params = {
    "vs_currency": "usd"
    ,"order": "market_cap_desc"
    ,"per_page": 250
}

print(params)

result = requests.get(url=url, params=params).json()

df = pd.DataFrame(result)
print(df)

print("----- 1. Üres cellák száma oszloponként -----")
print(df.isnull().sum())
print("\n")

print("----- 2. A teljes market_cap összege -----")
total_market_cap = df["market_cap"].sum()
print(total_market_cap)
print("\n")

print("----- 3. top50_df by current_price asc -----")
top50_df =(df.sort_values("current_price", ascending=True).head(50))
print(top50_df[["id", "name", "current_price"]])
print("\n")

print("----- 4. top50_df by price_change_percentage_24h desc -----")
top50_sort1_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)
print(top50_sort1_df[["id", "name", "price_change_percentage_24h"]])
print("\n")

# új oszlop a top50_df-be "change_direction" néven, amelynek 3 értéke lehet : 
#  -  Ha a price_change_percentage_24h értéke nagyobb mint 0 -> “+” 
#  -  Ha negatív -> “-“ 
#  -  Ha kereken 0 -> “0”
print("----- 5. top50_df with change_direction -----")

def change_direction(row):
    if row["price_change_percentage_24h"] > 0:
        return "+"
    elif row["price_change_percentage_24h"] < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df.apply(change_direction, axis=1)

print(top50_df[["id", "current_price", "price_change_percentage_24h", "change_direction"]])
print("\n")


