import pandas as pd
#import numpy as np
import requests

def change_direction(row):
    if row["price_change_percentage_24h"] > 0:
        return '+'
    elif row["price_change_percentage_24h"] < 0:
         return '-'
    else:
        return '0'


url = "https://api.coingecko.com/api/v3/coins/markets"

params = {"vs_currency": "HUF",
          "per_page": 250}

response = requests.get(url=url, params=params).json()
df_coingecko=pd.DataFrame(response)

empty_cells = df_coingecko.isnull().sum()
print (empty_cells)

total_market_cap = df_coingecko['market_cap'].sum()
print(total_market_cap)

top50_df=df_coingecko.sort_values('current_price', ascending=False).head(50)

top50_df=top50_df.sort_values('price_change_percentage_24h',ascending=False)


#top50_df['change_direction']=np.where(
#    top50_df['price_change_percentage_24h']> 0,
#    '+',
#    np.where(
#        top50_df['price_change_percentage_24h']< 0,
#    '-',
#    0
#    )
#    )



top50_df['change_direction'] = top50_df.apply(change_direction, axis=1)
print(top50_df)


