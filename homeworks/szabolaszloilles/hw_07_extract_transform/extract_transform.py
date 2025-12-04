import requests

import pandas as pd

# 1. Fetch data from the CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',             # Prices in USD
    'order': 'market_cap_desc',       # Sort by market capitalization (descending)
    'per_page': 250,                  # Fetch top 250 coins
    'page': 1                         # All in one request
}

response = requests.get(url, params=params)
data = response.json()

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# Task 1: Count missing values in each column
missing_values = df.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Task 2: Calculate total market capitalization
total_market_cap = df['market_cap'].sum()
print(f"\nTotal market capitalization: {total_market_cap:,.2f} USD")

# Task 3: Create a new DataFrame (top50_df) sorted by current_price
top50_df = df.sort_values(by='current_price', ascending=False).head(50)

# Task 4: Sort top50_df by price_change_percentage_24h in descending order
top50_df = top50_df.sort_values(by='price_change_percentage_24h', ascending=False)

# Task 5: Add a new column 'change_direction'
def direction_label(pct):
    if pct > 0:
        return '+'
    elif pct < 0:
        return '-'
    else:
        return '0'

top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(direction_label)

# Optional: Display a sample of the result
print("\nTop 5 rows from top50_df:")
print(top50_df[['id', 'current_price', 'price_change_percentage_24h', 'change_direction']].head())