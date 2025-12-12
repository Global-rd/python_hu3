import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',      # target currency of coins and market data
    'order': 'market_cap_desc', # market cap szerint csökkenő sorrend
    'per_page': 250,           # 250 eredmény egy oldalon
    'page': 1                  # 1. oldal
}

response = requests.get(url, params=params)
data = response.json()





# Creating a DataFrame from data
df = pd.DataFrame(data)

# Statistic
print("The statistics of the dataframe:\n")

print(f"Retrieved {len(df)} db cryptocurrency data\n")
print(f"Total missing datas in dataframe: {df.isnull().sum().sum()} \n")
print(f"The proportion of missing data in the entire DataFrame: {df.isnull().sum().sum() / df.size * 100:.2f}%\n")
print(f"Number of columns in the DataFrame: {len(df.columns)} pcs\n")

print("-------------TASK 1-----------------\n")
# 1. Task empty cells of dataframe columns
info_df = pd.DataFrame({
    'Data type': df.dtypes,
    'Missing data (db)': df.isnull().sum(),
    'Missing data (%)': (df.isnull().mean() * 100).round(2) # Kerekítve 2 tizedesre
})

# Descending order by degree of deficiency
info_df = info_df.sort_values(by='Missing data (%)', ascending=False)

print(info_df)

print("-------------TASK 2-----------------\n")
# 2. Task the total dataframe market_cap amount
market_cap_sum = df["market_cap"].sum().sum()
print(f"The market cap sum: {market_cap_sum}")


print("-------------TASK 3-----------------\n")
# 3. top 50 datas
top50_df = df.loc[:50]
print(top50_df)

print("-------------TASK 4-----------------\n")
# 4. Task top 50 price_change_percentage_24h descending order
top50_df = top50_df.sort_values(by='price_change_percentage_24h', ascending=False)
print(top50_df)

print("-------------TASK 5-----------------\n")
# 5. Task new column in top50_df called change_direction which can have 3 values ​​(+, -, 0)

def new_colums(row):

    if row["price_change_percentage_24h"] > 0:
        return "+"
    elif row["price_change_percentage_24h"] < 0:
        return "-"
    else:
        return 0

top50_df['Change percent'] = top50_df.apply(new_colums, axis=1)
print(top50_df)