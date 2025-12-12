import requests
import pandas as pd


url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'per_page': 250
}

response = requests.get(url, params=params)
data = response.json()


df = pd.DataFrame(data)

print("=" * 100)
print("FELADAT 1: Üres cellák száma oszloponként")
print("=" * 100)
empty_cells = df.isnull().sum()
print(empty_cells)

print("\n" + "=" * 100)
print("FELADAT 2: Teljes market cap összege")
print("=" * 100)
total_market_cap = df['market_cap'].sum()
print(f"Teljes market cap: ${total_market_cap:,.2f}")

print("\n" + "=" * 100)
print("FELADAT 3: Top 50 kriptovaluta current_price alapján")
print("=" * 100)
top50_df = df.nlargest(50, 'current_price').copy()#azért használom a copyt mert enélkül csak egy view

print("\n" + "=" * 100)
print("FELADAT 4: Top 50 rendezése price_change_percentage_24h alapján")
print("=" * 100)
top50_df = top50_df.sort_values('price_change_percentage_24h', ascending=False)
print(top50_df[['name', 'current_price', 'price_change_percentage_24h']])

print("\n" + "=" * 100)
print("FELADAT 5: change_direction oszlop hozzáadása")
print("=" * 100)
def get_change_direction(value):
    if pd.isnull(value):
        return None
    elif value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"

top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(get_change_direction)

print(top50_df[['name', 'current_price', 'price_change_percentage_24h', 'change_direction']])
