# app.py
import requests
import streamlit as st
import pandas as pd
from datetime import datetime
import sqlite3

st.set_page_config(
    page_title="Weather Map & Data Visualization App",
    page_icon="🌦",
    layout="wide"
)

st.title("Robot Dreams Python - Weather Map & Data Visualization App")

# --- CITY INPUT ---
city = st.text_input("Enter city name", value="London")

# --- API KEY ---
api_key = st.secrets["openweather"]["api_key"]

# --- CACHE-ELT FÜGGVÉNYEK ---

@st.cache_data
def get_current_weather(city: str):
    """Jelenlegi időjárás lekérése OpenWeatherMap /weather endpoint-ról."""
    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )
    response = requests.get(url)
    if response.status_code != 200:
        # Hibás városnév vagy más hiba
        raise ValueError(f"API error: {response.status_code} - {response.text}")
    return response.json()


@st.cache_data
def get_forecast(city: str):
    """Előrejelzés lekérése (extra) /forecast endpoint-ról."""
    url = (
        f"http://api.openweathermap.org/data/2.5/forecast"
        f"?q={city}&appid={api_key}&units=metric"
    )
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"API error: {response.status_code} - {response.text}")
    return response.json()


# --- SQLITE (EXTRA) - adatbázis init ---
def init_db():
    conn = sqlite3.connect("weather_searches.db")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            created_at TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def log_search(city: str, temp: float, hum: int, wind: float):
    conn = sqlite3.connect("weather_searches.db")
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO searches (city, temperature, humidity, wind_speed, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (city, temp, hum, wind, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


init_db()

# --- MAIN LOGIC ---

if city:
    try:
        data = get_current_weather(city)

        # Aktuális adatok kinyerése
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]  

        # Városnév dinamikus kiírása
        st.subheader(f"Current Weather in {city}")

        # KPI-ok 3 oszlopban
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Temperature (°C)", f"{temp:.2f}°C")
        with col2:
            st.metric("Humidity (%)", f"{humidity}%")
        with col3:
            st.metric("Wind Speed (m/s)", f"{wind_speed:.2f} m/s")

        # Loggolás SQLite adatbázisba (extra feladat)
        log_search(city, temp, humidity, wind_speed)

        # Térképhez DataFrame-lat/lon
        st.subheader("Weather Map")
        map_df = pd.DataFrame(
            {"lat": [lat], "lon": [lon]}
        )
        st.map(map_df, zoom=10)

        # --- EXTRA: ELŐREJELZÉS CHART ---
        st.subheader("Temperature Trends (Next 5 Days)")
        forecast_data = get_forecast(city)

        # A /forecast válaszból időpont + hőmérséklet kinyerése
        times = []
        temps = []
        for item in forecast_data["list"]:
            times.append(item["dt_txt"])
            temps.append(item["main"]["temp"])

        forecast_df = pd.DataFrame(
            {"datetime": pd.to_datetime(times), "temperature": temps}
        ).set_index("datetime")

        st.line_chart(forecast_df["temperature"])

    except ValueError as e:
        st.warning(
            "Sikertelen API hívás. "
            "Ellenőrizd, hogy helyes városnevet adtál-e meg!"
        )
        st.text(str(e))
    except Exception as e:
        st.error("Váratlan hiba történt.")
        st.text(str(e))
else:
    st.info("Adj meg egy létező városnevet az induláshoz.")
