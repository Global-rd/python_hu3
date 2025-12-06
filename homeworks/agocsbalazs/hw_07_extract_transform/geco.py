import os
from typing import Any, Dict, List  
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv
import requests
import settings as s
import pandas as pd

# némi vizualizáció
import plotly.express as px



def get_gecko_data() -> pd.DataFrame:
    url = s.GECKO_API_URL
    params = {
        "vs_currency": s.GECKO_CURRENCY,
        "order_list": s.GECKO_ORDER,
        "per_page": s.GECKO_PER_PAGE,
        "page": 1,  
    }

    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data)
    return df
#print(get_gecko_data())
if __name__ == "__main__":
    gecko_df=get_gecko_data()
    print(gecko_df)
    
#üres sorok száma oszloponként:
null_per_column = gecko_df.isna().sum()
print(null_per_column)

#összes részvény market cap szumma összege:
total_market_cap = gecko_df['market_cap'].sum() 
print(f"Total Market Cap: {total_market_cap:,.0f} USD")


#top 50 részvény a current_price alapján csökkenő sorrendben:
top_50_df = gecko_df.nlargest(50, 'current_price')
print(top_50_df[['id', 'market_cap', 'current_price']])

#top 50 részvény rendezése a price_change_percentage_24h alapján csökkenő sorrendben:
top_50_sorted_df = top_50_df.sort_values(by='price_change_percentage_24h', ascending=False)
print(top_50_sorted_df[['id', 'price_change_percentage_24h']])


#egyéni oszlop létrehozása a 24h változás alapján növekedés +/ csökkenés - jelzéssel, ha nincs változás akkor 0
def price_change_label(change):
    if change > 0:
        return '+'
    elif change < 0:
        return '-'
    else:
        return '0'
top_50_df["change_direction"] = top_50_df['price_change_percentage_24h'].apply(price_change_label)
#spyder df-ben látom de ide kell egy print vs alá
print(top_50_df[['id', 'price_change_percentage_24h', 'change_direction']])


#plotly vizualizáció készítése a top 50 részvény market_cap és current_price értékei alapján
"""fig = px.bar(top_50_df, x='name', y='current_price', 
             title='Top 50 curency by Current Price',
             labels={'name': 'Cryptocurrency', 'current_price': 'Current Price (USD)'},
             )
fig.show()
"""
fig = px.scatter(top_50_df, x='name', y='price_change_percentage_24h', 
                 color='change_direction',
                 #némi színezés a change_direction alapján
                 color_discrete_map={"+": "green", "-": "red", "0": "gray"},
                 title='Top 50 curency by 24h Price Change Percentage direction',
                 labels={'name': 'Cryptocurrency', '24h Price Change Percentage': '24h Change Direction'},
                 )
fig.show()