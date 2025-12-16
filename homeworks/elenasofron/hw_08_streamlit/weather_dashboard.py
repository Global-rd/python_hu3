import streamlit as st
import requests
import pandas as pd
import plotly.express as px

#api_key_weather = ["b2c2a2a969cb237ff0df24a3eb6b374f"]

print(st.secrets["openweather"]["api_key_weather"])



'''
@st.cache_data(ttl=600)

def get_current_weather(city, api_key_weather):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key_weather,
        "units": "metric",
        "lang": "hu"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None
    return response.json()

st.title("WEATHER DASHBOARD")

city = st.text_input("Write a city:")

if city:
    api_key_weather = "b2c2a2a969cb237ff0df24a3eb6b374f"
    
    # Current weather
    data = get_current_weather(city, api_key_weather)

    if data:
        st.subheader(f"Current city: **{city}**")
        st.write(f"Current temperature: {data['main']['temp']} °C")

        col.metric("Temperature (°C)", f"{data['main']['temp']} °C")

    else:
        st.error("ERROR")

'''