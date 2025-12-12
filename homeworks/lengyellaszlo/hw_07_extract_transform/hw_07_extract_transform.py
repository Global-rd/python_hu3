import requests
import pandas as pd
import logging

# Log konfigurálása
logging.basicConfig(
    level=logging.INFO,  
    format="%(asctime)s - %(levelname)s - %(message)s"
)

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}

logging.info("API lekérés indítása...")

try:
    response = requests.get(url, params=params, timeout=10)  # timeout az esetleges akadás ellen
    response.raise_for_status()  # Hibát dob, ha pl. 404 vagy 500
    data = response.json()

    if not data:
        logging.error("Az API válasz üres! Nem folytatható az adatfeldolgozás.")
        exit(1)

    logging.info("Sikeres API válasz érkezett.")

except requests.exceptions.Timeout:
    logging.error("Timeout hiba: Az API túl sokáig nem válaszolt.")
    exit(1)
except requests.exceptions.RequestException as e:
    logging.error(f"API hiba történt: {e}")
    exit(1)

# Dataframe létrehozása
df = pd.DataFrame(data)

# 1. feladat
print("----- 1. FELADAT: Üres cellák száma oszloponként -----")
print(df.isnull().sum(), "\n")

# 2. feladat
total_market_cap = df["market_cap"].sum()
formatted_market_cap = f"{total_market_cap:,}"
print(f"----- 2. FELADAT: A teljes market_cap összege: {formatted_market_cap} -----\n")

# 3–4. feladat
top50_df = df.sort_values("current_price", ascending=False).head(50)
top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)

# 5. feladat
top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(
    lambda x: "+" if x > 0 else "-" if x < 0 else "0"
)

print("----- 3-4-5. FELADAT: top50_df eredménye (első 15 sor) -----")
print(top50_df[["id", "current_price", "price_change_percentage_24h", "change_direction"]].head(15))
