import requests
import pandas as pd

class CoinGeckoExtractor:

    def __init__(self):
        self.base_url = "https://api.coingecko.com/api"

    def get_dataframe(self, endpoint, params):        
        url = f"{self.base_url}/{endpoint}"

        response = requests.get(url, params=params)
        if response.status_code == 200:
            df = pd.DataFrame(response.json())           
        else:
            print(f"Error: {response.status_code}: {response.text}")
        return df
    
    
if __name__ == "__main__":
    api = CoinGeckoExtractor()
    df = api.get_dataframe("v3/coins/markets", {"vs_currency": "usd", "per_page": 250, "page": 1})
    
    print("------------")
    print("1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.") 
   
    missing_per_col = df.isna().sum()
    missing_nonzero = missing_per_col[missing_per_col > 0]
    for col, count in missing_nonzero.items():
        print(f"Oszlop: {col}, üres cellák száma: {count}")
    
    print("------------")
    print("2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki..") 
    total_market_cap = df["market_cap"].sum()
    print(f"Összes market cap: {format(total_market_cap, ',d')} USD")
    
    print("------------")
    print("3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján") 
    top50_df = df.nlargest(50, "current_price").reset_index(drop=True)
    print(top50_df[["name", "current_price"]])

    print("------------")
    print("4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!") 
    top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False).reset_index(drop=True)
    print(top50_df[["name", "price_change_percentage_24h"]])

    print("------------")
    print("5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet ('+', '-', '0'):")

    def determine_change_direction(row):
        if row["price_change_percentage_24h"] > 0:
            return "+"
        elif row["price_change_percentage_24h"] < 0:
            return "-"
        else:
            return "0"
        
    top50_df["change_direction"] = top50_df.apply(determine_change_direction, axis=1)
    print(top50_df[["name", "price_change_percentage_24h", "change_direction"]])
