import requests
import pandas as pd

# === ADF BETÖLTÉSE ===
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

# === FELADATOK ===

print(df.isna().sum())

total_market_cap = df["market_cap"].sum()
print("Total market cap:", total_market_cap)

top50_df = df.sort_values("current_price", ascending=False).head(50)

def get_direction(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(get_direction)

print(top50_df.head())