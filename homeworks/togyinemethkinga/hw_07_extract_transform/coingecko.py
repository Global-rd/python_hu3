import requests
import pandas as pd


url = "https://api.coingecko.com/api/v3/coins/markets"

params = {"vs_currency": "usd",
          "per_page": 250}

response = requests.get(url=url, params=params).json()
df = pd.DataFrame(response)

# 1. FELADAT:
print(df.isna().sum())

# 2. FELADAT:
total_market_cap = sum(df["market_cap"])
print(f"The total market cap in the database: {total_market_cap}")


# 3. FELADAT:
top50_df = (df
             .sort_values("current_price", ascending=False)
             .head(50)
             .reset_index()
             )

# 4. FELADAT:
top50_df_sorted = top50_df.sort_values("price_change_percentage_24h", ascending=False)

# 5. FELADAT:
def change_direction(row):
    if row["price_change_percentage_24h"] > 0:
        return "+"
    elif row["price_change_percentage_24h"] == 0:
        return "0"
    else:
        return "-"
    
top50_df_sorted["change_direction"] = top50_df_sorted.apply(change_direction, axis=1)
print(top50_df_sorted)
