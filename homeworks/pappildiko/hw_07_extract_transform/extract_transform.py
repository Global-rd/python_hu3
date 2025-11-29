import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1,
    "sparkline": "false",  # no sparkline data
    "price_change_percentage": "24h"  # ensures price_change_percentage_24h field
}

response = requests.get(url, params=params)
response.raise_for_status()  # raises error if response code is not 200
data = response.json()

df = pd.DataFrame(data)

print('------- 1. Task: Count missing cells per column ----------')

missing_counts = df.isna().sum()
print("Missing (empty) cells per column:")
print(missing_counts)

print('------- 2. Task: Total market cap ----------')

total_market_cap = df["market_cap"].sum()
print(f"Total market cap (sum): {total_market_cap}")

# ------- 3. Task: Create top50_df ----------

top50_df = df.head(50).copy()

# ------- 4. Task: Sort top50_df by 24h price change ----------

top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

# ------- 5. Task: Create change_direction column ----------'

def change_dir(pct):
    if pd.isna(pct):
        return None
    if pct > 0:
        return "+"
    elif pct < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(change_dir)

print('------- Display selected columns from top50_df ----------')

print(top50_df[["id", "current_price", "price_change_percentage_24h", "change_direction"]])
