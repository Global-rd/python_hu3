import streamlit as st
import plotly.express as px
import requests
import pandas as pd
import json
import sqlite3
from datetime import datetime
import os

#URL Create
#http://api.openweathermap.org/data/2.5/forecast/daily?q={city_name}&cnt=5&appid={API key}
#api.openweathermap.org/data/2.5/forecast?q=London&appid=f24268e65c45daa561b71131970e4b6f&units=metric


API_KEY=st.secrets["forcast"]["api_key"]
BASE_URL="https://api.openweathermap.org/data/2.5/forecast"

@st.cache_data(ttl=900)
def fetch_stock_data(city_name):
    print(f"Fetch data {city_name}")
    
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    print(url)
    
    response =requests.get(url)

    if response.status_code == 200:
        print(response.text)
        
        return response.json()
    else:
        st.error(f"Faild to fetch data: {response.status_code} - {response.text}")

#fetch_stock_data("London")


def process_data(data):

    if  "list" in data:
        df = pd.json_normalize(data['list'])
        
        df['timestamp'] = pd.to_datetime(df['dt'], unit='s')
        df_final = df.set_index('timestamp')[['main.temp']].copy()
        df_final.columns = ['Temp (°C)']

        df_final['Temp (°C)'] = df_final['Temp (°C)'].astype(float)
        
        print(df_final)
        return df_final
    
    else:
        st.error("Not data available")
        return None

def main():
    st.title("Weather Forecast For The Next 5 Days")
    
    stock_city_name = st.text_input(
        "Enter City Name: ", "Budapest"
    )
    
    data = fetch_stock_data(stock_city_name)

    if data:
        df_final = process_data(data)
        st.header(f"Next 5 days weather forecast for {stock_city_name}")

        if df_final is not None:
            st.line_chart(df_final)
            st.dataframe(df_final)
            

    else:
        st.error("No data!")


if __name__=="__main__":
    main()

