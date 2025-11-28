import requests
import settings as s
import pandas as pd


url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": s.GECKO_CURRENCY}

response = requests.get(url, params=params)

data = response.json()
df = pd.DataFrame(data)

# 1 - Check for empty values in the DataFrame
empty_values = df.isna().sum().sum()
print(f"Empty values in each column: {empty_values}")
print("-------------------------------")

# 2 - Sum of the 'market_cap' column
market_cap_sum = df['market_cap'].sum()
print(f"Sum of market_cap: {market_cap_sum:.2f}")
print("-------------------------------")

# 3 - New DataFrame TOP 50 currency by current_price

top50_df = df.nlargest(50, 'current_price')
print("Top 50 currencies by current_price:")
print(top50_df[['id', 'current_price']])
print("-------------------------------")

# 4 - TOP 50  order

top50_ordered_df = top50_df.sort_values(by='price_change_percentage_24h', ascending=False)
print("Top 50 currencies ordered by price_change_percentage_24h:")
print(top50_ordered_df[['id', 'price_change_percentage_24h','current_price']])

print("-------------------------------")

# 5 - Add a new column 'change_direction'

def change_direction(value):
    if value["price_change_percentage_24h"] > 0:
        return '+'
    elif value["price_change_percentage_24h"] < 0:
        return '-'
    else:
        return '0'


top50_ordered_df['change_direction'] = top50_ordered_df.apply(change_direction, axis=1)
print("Top 50 currencies with change_direction:")
print(top50_ordered_df[['id', 'price_change_percentage_24h', 'change_direction']])
