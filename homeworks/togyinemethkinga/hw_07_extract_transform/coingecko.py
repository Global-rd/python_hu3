import requests
import settings as s
import pandas as pd


url = "https://api.coingecko.com/api/v3/coins/markets"

params = {"api.coingecko.com": s.api_coingecko_com,
          "vs_currency": "usd",
          "per_page": 250}

response = requests.get(url=url, params=params).json()
df = pd.DataFrame(response)

# 1. FELADAT:
def number_of_none_in_col(num):
    # adott oszlopban a none értékek száma, oszlop számának megadásával:
    col = df.columns[num]
    act_column = df[col]
    sum_none = sum(1 for i in act_column if i == None)
    print(f"{col} has {sum_none} none value.")

def none_in_col(column_name):
    # adott oszlopban a none értékek száma, oszlop nevének megadásával:
    if column_name in df.columns:
        sum_none = sum(1 for i in df[column_name] if i == None)
        print(f"{column_name} has {sum_none} none value.")
    else: 
        print("Not avaliable column.")

# összes oszlop none értéke:
for i in df.columns:
    none_in_col(i)


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
