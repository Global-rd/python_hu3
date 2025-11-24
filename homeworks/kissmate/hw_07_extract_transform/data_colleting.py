import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=250"

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()  # Assuming the data is in JSON format

df = pd.DataFrame(fetch_data(url))

#Single colum emty cells check
empty_cells = df.isnull().sum()
print(empty_cells)

#dataframe market cap sum
market_cap_sum = df['market_cap'].sum()
print(f"Total Market Cap: {market_cap_sum}")

#top 50 cryptocurrencies decending order by current price
price_change_percentage_24h = df['price_change_percentage_24h'].sort_values(ascending=False)
top_50_cryptos = df.nlargest(50, 'current_price')
print(top_50_cryptos[['name', 'current_price']])
df.addchange_diretion = df['price_change_percentage_24h'].apply(lambda x: '+' if x > 0 else '-' if x < 0 else '0')





