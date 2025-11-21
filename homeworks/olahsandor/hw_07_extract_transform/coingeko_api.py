import requests
import pandas as pd

#Konfiguráció
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
# Parameters: USD currency, 250 items 1 hívásból és innen a market cap majd
PARAMS = {
        "vs_currency": "usd",
        "per_page": 250,
        "page": 1
        }

print("Starting CoinGecko API request...")

#API Hívás és Adatlekérés
response = requests.get(API_URL, params=PARAMS)
response.raise_for_status() # Hibát dob, ha rossz az állapotkód.
data = response.json()
print(f"Successfully retrieved data for {len(data)} cryptocurrencies.")

#Adatok tárolása Pandas DataFrame-ben
df = pd.DataFrame(data)
print("DataFrame created.")

# --- Pandas Feladatok ---

#1.Üres cellák (NaN) száma oszloponként
print("\n--- 1. Count of Missing Values per Column ---")
missing_values = df.isnull().sum() # Megszámolja az üres (NaN) értékeket oszloponként.
print(missing_values)


#2.A teljes DataFrame market_cap összegének meghatározása
print("\n--- 2. Total Market Cap ---")
total_market_cap = df['market_cap'].sum() # Összegzi a 'market_cap' oszlop értékeit.
print(f"Total Market Cap: ${total_market_cap:,.2f} USD")

#3.Új DataFrame (top50_df) létrehozása az első 50 kriptovalutával
print("\n--- 3. Creating top50_df ---")
#Kiválasztja az első 50 sort, amelyek alapértelmezetten Market Cap szerint vannak rendezve az API-ban.
top50_df = df.head(50).copy()
print(f"Top50_df created with {len(top50_df)} items.")

#4.Top50_df rendezése price_change_percentage_24h alapján csökkenő sorrendbe
print("\n--- 4. Sorting top50_df by 24h Percentage Change (Descending) ---")
top50_df_sorted = top50_df.sort_values(
    by='price_change_percentage_24h',
    ascending=False # Csökkenő sorrend beállítása
)
print("Top 5 cryptocurrencies by 24h price change increase:")
print(top50_df_sorted[['name', 'price_change_percentage_24h']].head())

#5.Új oszlop létrehozása 'change_direction' néven ('+', '-', '0')
print("\n--- 5. Creating 'change_direction' Column ('+', '-', '0') ---")
#Segéd a feltételes hozzárendeléshez az apply metódussal
def get_change_direction(change_percentage):
    # Meghatározza az irányt a százalékos változás alapján.
    if change_percentage > 0:
        return '+'
    elif change_percentage < 0:
        return '-'
    else:
        return '0'

#Alkalmazza a függvényt a 'price_change_percentage_24h' oszlopra
top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(get_change_direction)
print("First 5 rows of the new column:")
print(top50_df[['name', 'price_change_percentage_24h', 'change_direction']].head())
print("\nAll tasks completed successfully!")
