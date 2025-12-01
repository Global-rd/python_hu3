import streamlit as st
import requests
import pandas as pd
import sqlite3
from datetime import datetime

st.set_page_config(page_title="Weather Dashboard", layout="wide")

# ----------------------------- DATABASE SETUP ----------------------------- #
def init_db():
    conn = sqlite3.connect("weather_logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            city TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            datetime TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_search(city, temp, humidity, wind):
    conn = sqlite3.connect("weather_logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO logs (city, temperature, humidity, wind_speed, datetime)
        VALUES (?, ?, ?, ?, ?)
    """, (city, temp, humidity, wind, datetime.now().isoformat()))
    conn.commit()
    conn.close()


init_db()

# ----------------------------- API ACCESS ----------------------------- #
API_KEY = st.secrets["openweather"]["api_key"]

@st.cache_data(show_spinner=False)
def get_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    return requests.get(url).json()

@st.cache_data(show_spinner=False)
def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    return requests.get(url).json()

# ----------------------------- SIDEBAR INPUT ----------------------------- #
st.sidebar.title("🌍 Weather App")
city = st.sidebar.text_input("City name:", "Budapest")

st.title("🌦️ Weather Dashboard")

if st.sidebar.button("Get Weather"):
    if not city:
        st.warning("Please enter a valid city name.")
        st.stop()

    data = get_current_weather(city)

    if "cod" in data and data["cod"] != 200:
        st.warning(f"Error: {data.get('message', '')}")
        st.stop()

    # ----------------------------- CURRENT WEATHER ----------------------------- #
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]

    st.subheader(f"🌡️ Current Weather — {city}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature (°C)", f"{temp}°C")
    col2.metric("Humidity (%)", f"{humidity}%")
    col3.metric("Wind Speed (m/s)", f"{wind_speed}")

    # Log to database
    log_search(city, temp, humidity, wind_speed)

    # ----------------------------- MAP ----------------------------- #
    st.subheader("📍 Location on Map")
    map_df = pd.DataFrame({"lat": [lat], "lon": [lon]})
    st.map(map_df)

    # ----------------------------- FORECAST (EXTRA) ----------------------------- #
    forecast_data = get_forecast(city)

    if "cod" in forecast_data and forecast_data["cod"] != "200":
        st.warning("Forecast data unavailable.")
    else:
        df_forecast = pd.DataFrame(forecast_data["list"])

        df_forecast["datetime"] = pd.to_datetime(df_forecast["dt"], unit="s")
        df_forecast["temp"] = df_forecast["main"].apply(lambda x: x["temp"])

        st.subheader("📅 Forecast (5 days, 3-hour intervals)")
        st.line_chart(df_forecast.set_index("datetime")["temp"], height=250)

        # Optional: humidity chart
        st.subheader("💧 Humidity Forecast")
        df_forecast["humidity"] = df_forecast["main"].apply(lambda x: x["humidity"])
        st.line_chart(df_forecast.set_index("datetime")["humidity"], height=250)




 