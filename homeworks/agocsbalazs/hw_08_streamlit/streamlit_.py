import os
from typing import Any, Dict, List  
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv
import requests
import settings as s
import pandas as pd
import streamlit as st
import sqlite3
import datetime as dt

# némi vizualizáció
import plotly.express as px


#tény időjárás adatok:
@st.cache_data(ttl=600)
def get_streamlit_data(city: str) -> pd.DataFrame:
    url = s.OPENWEATHER_API_URL
    #  url = st.secrets["OPENWEATHER"]["OPENWEATHER_API_URL"] streamlit-ben ez van kint, de már nem írom itt is át bocsi
    try:
        params = {
        "q": city,
        "appid": s.OPENWEATHER_API_KEY,
        # "appid": st.secrets["OPENWEATHER"]["OPENWEATHER_API_KEY"],
        "units": "metric",
        "lang": "hu"
    }

   
        response = requests.get(url,params=params)
        data = response.json()
        df = pd.json_normalize(data)
        return df
    except Exception as e:
        st.error(f"Hiba: {e}")
        return None

#forecast adatok:
@st.cache_data(ttl=600)
def get_streamlit_forecastdata(city: str) -> pd.DataFrame:
    url = s.OPENWEATHER_API_URL_FORECAST
    try:
        params = {
            "q": city,
            "appid": s.OPENWEATHER_API_KEY,
            "units": "metric",
            "lang": "hu"
        }

    
        response = requests.get(url,params=params)
        data = response.json()
        df = pd.json_normalize(data)
        return df
    except Exception as e:
            st.error(f"Hiba: {e}")
            return None


#sqllote mentés előkészítés
def save_data_to_sqllite(df: pd.DataFrame, table_name: str):
    conn = sqlite3.connect('hw08.db')
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()

#sql tábla létrehozás df-el az adatoknak
def build_weather_df(city: str, df_raw: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{
        "city": city,
        "timestamp": dt.datetime.now().isoformat(),
        "temperature": df_raw["main.temp"][0],
        "humidity": df_raw["main.humidity"][0],
        "pressure": df_raw["main.pressure"][0],
        "wind_speed": df_raw["wind.speed"][0],
        "description": df_raw["weather"][0][0]["description"],
        "lat": df_raw["coord.lat"][0],
        "lon": df_raw["coord.lon"][0],
    }])

#kell egy log tábla is
def build_log_df(city: str) -> pd.DataFrame:
    return pd.DataFrame([{
        "timestamp": dt.datetime.now().isoformat(),
        "city": city,
        "user": "anonymous from IP:", #jo lenne az ip cím bele
        "source": "streamlit_app",
    }])


def main():
    st.title(f"Időjárás lekérdező alkalmazás")

    city = st.text_input("Kiválasztott város neve:", value=s.DEFAULT_CITY)
    


    if not city:
        st.warning("Kérem, adjon meg egy városnevet a kereséshez.")
        return
    
    df =get_streamlit_data(city)

    if df is None:
        st.warning("Nincs adat a megadott városhoz.")
        return
        
   
               
    st.markdown(f"{city} Aktuális dőjárása:")
            
    top_box1, top_box2 =st.columns([2, 2])  #box szélességek
    top_box1.metric("Hőmérséklet (°C)", f"{df['main.temp'][0]} °C")
    top_box2.metric("Páratartalom (%)", f"{df['main.humidity'][0]} %")
    box3, box4, box5 = st.columns([2, 2, 4])
    box3.metric("Szélsebesség (m/s)", f"{df['wind.speed'][0]} m/s")
    box4.metric("Légnyomás (hPa)", f"{df['main.pressure'][0]} hPa")
    box5.metric("Jelenlegi jellemző időjárás:", f"{df['weather'][0][0]['description']}")
            
    #box6.metric("long/lat:", f"{df['coord.lon'][0]}/{df['coord.lat'][0]}")
            
   #map nézet

    long = df['coord.lon'][0]
    lat = df['coord.lat'][0]
    map_data = pd.DataFrame({
        'lat': [lat],
        'lon': [long]
       })
    
    st.subheader("Térkép nézet")
    st.map(map_data, zoom=10)
        
    #forecast adatok plotly-al
    df_forecast = get_streamlit_forecastdata(city)
    st.markdown(f"### {city} 5 napos időjárás előrejelzés:")
    df_forecast_expanded = pd.json_normalize(df_forecast['list'][0])

    fig = px.line(df_forecast_expanded, x='dt_txt', y='main.temp', 
                labels={'dt_txt': 'Dátum és idő', 'main.temp': 'Hőmérséklet (°C)'}, 
                title=f"{city} Hőmérséklet előrejelzés a következő 5 napban")
    st.plotly_chart(fig)


    #lementjük a az adatokat és a logot is sqllite-ba
    weather_df = build_weather_df(city, df)
    log_df = build_log_df(city)

    save_data_to_sqllite(weather_df, "weather_data")
    save_data_to_sqllite(log_df, "request_log")

    st.success("Adatok sikeresen elmentve SQLite adatbázisba")


if __name__ == "__main__":
    main()
