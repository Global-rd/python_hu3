import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)

print("A DataFrame első 5 sora: ")
print(df.head())

print("\n1. feladat: ")
print(df.isna().sum())

total_market_cap = df["market_cap"].sum()
print("\n2. feladat: ")
print(total_market_cap)

top50_df = df.sort_values(by="current_price", ascending=False).head(50)
print("\n3. feladat: ")
print(top50_df[["id", "current_price"]].head())


top50_df = top50_df.sort_values(
    by="price_change_percentage_24h", ascending=False)
print("\n4. feladat: ")
print(top50_df[["id", "price_change_percentage_24h"]].head())


def change_direction(x):
    if x > 0:
        return "+"
    elif x < 0:
        return "-"
    else:
        return "0"


top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(
    change_direction)

print("\n5. feladat: ")
print(top50_df[["id", "price_change_percentage_24h", "change_direction"]].head())

# mentés egy .csv fájlba
top50_df.to_csv("top50_df.csv", index=False)
