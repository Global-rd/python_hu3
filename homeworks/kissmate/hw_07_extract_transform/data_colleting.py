import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=250"

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()  # Assuming the data is in JSON format

df = pd.DataFrame(fetch_data(url))

print(df.isnull().sum()) #Get every empty cell in the dataframe

print(df.market_cap).sum() #Get the total market cap of all cryptocurrencies in the dataframe