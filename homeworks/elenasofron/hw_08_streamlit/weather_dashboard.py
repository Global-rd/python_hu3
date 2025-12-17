import streamlit as st
import requests
import pandas as pd

#api_key_weather = ["b2c2a2a969cb237ff0df24a3eb6b374f"]

API_KEY = st.secrets["openweather"]["api_key_weather"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#print(st.secrets["openweather"]["api_key_weather"])

#@st.cache_data(ttl=600)

def get_current_weather(city):
    url = f"{BASE_URL}/?q={city}&appid={API_KEY}&units=metric&lang=en"
    response = requests.get(url)

    if response.status_code != 200:
        return None
    return response.json()


st.title("WEATHER DASHBOARD")

city = st.text_input("Write a city:")

if city:
    current_weather = get_current_weather(city)
    
    if current_weather:
        city = current_weather['name']
        st.header(f"Current Weather in {city}")

        c1, c2, c3 = st.columns(3)

        temp = current_weather['main']['temp']
        humidity = current_weather['main']['humidity']
        wind_speed = current_weather['wind']['speed']

        c1.metric("Temperature (°C)", f"{temp}°C")
        c2.metric("Humidity (%)", f"{humidity}%")
        c3.metric("Wind Speed (m/s)", f"{wind_speed} m/s")

    else:
        st.error("ERROR")
