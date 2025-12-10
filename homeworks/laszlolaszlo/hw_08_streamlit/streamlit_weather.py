"""
Hozd létre a következő streamlit appot: A mintán látható KPI-ok/key metric-ek és a
chart-ok mindenképp legyenek jelen az app-odban, az elrendezés és a design
(színkombinációk, tabok, oszlopok stb) a te döntésed.

A következőkre lesz szükséged:
OpenWeatherMap API key:
https://home.openweathermap.org/users/sign_in regisztrálj, és hozz
létre egy saját API key-t (https://home.openweathermap.org/api_keys)
amit a .streamlit mappában a secrets.toml-ben tárolsz, ahogy az órán
tanultuk.

Egy cache-elt function-re a jelenlegi időjárás lekéréséhez.
Dokumentáció: https://openweathermap.org/current

Egy másik cache-elt function-re az előrejelzésekhez (extra feladat
része, nem kötelező). Dokumentáció:
https://openweathermap.org/forecast5

Tipp: mind a két endpoint-hoz használhatsz egy “q” paramétert, nem kell a
lat és lon paramétereket megadnod. Példák:
url =
f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={
api_key}&units=metric'
url =
f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=
{api_key}&units=metric'
Így az url-be bekerülhet a felhasználó által megadott város.

Működési elv: A felhasználónak képesnek kell lennie megadni egy létező
város nevét. Az, hogy hol kéred be az inputot, rád van bízva (pl egy
sidebaron, vagy ahogy a screenshoton látod). Ha az API hívás hibát dob,
tudasd egy warning használatával a hibát. Minden városnévvel kapcsolatos
text az oldalon dinamikusan változzon. A
https://openweathermap.org/current endpoint-ról húzd le az órán tanult
módon a megadott település jelenlegi hőmérsékletét, páratartalmát és a szél
sebességét. Jelenítsd meg KPI-okként/key metric-enként ezeket az adatokat.
A /current response tartalmazni fogja a lat és lon paramétereket, ezeket
felhasználva jeleníts meg egy térképet az st.map() segítségével (ennek
önállóan utána kell járnod).

Deployold az app-ot a Community Cloud–ra, és a PR-odnak legyen része a
link. A deployment-hez létre kell hoznod egy saját public repository-t, mivel
csak admin joggal rendelkező felhasználó deployolhat. Ettől függetlenül a
robot_dreams repo-ba PR-ként be kell adni a házi kódját a megszokott
módon.

Extra:
1.Készíts egy előrejelzést a /forecast-ból szerzett adatokból a mintán látható
módon.

2.Logolj minden keresést (városnév, temperature, humidity, wind speed, és a
jelenlegi idő (datetime.now()) egy sqlite adatbázisba. Ehhez hozd létre az
adatbázist és egy táblát a fent említett 5 oszloppal (használd az órán tanult
metódusokat a betöltéshez)
"""

import streamlit as st
import plotly.express as px
import datetime
import requests
from pathlib import Path
import pandas as pd

API_KEY = st.secrets["openweathermap"]["api_key"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

st.set_page_config(page_title="Weather Dashboard", layout="wide")


@st.cache_data(ttl=3600)
def fetch_weather_data(city_name: str, api_key: str = API_KEY) -> dict | None:
    """
    Fetch current weather data for a given city.
    """
    print(f"Fetch weather data for {city_name} with {API_KEY}")

    url = f"{BASE_URL}?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP errors
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error fetching data: {response.status_code}")
            return None
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None


@st.cache_data(ttl=86400)
def fetch_forecast_data(city_name: str, api_key: str = API_KEY) -> dict | None:
    """
    Fetch 5-day weather forecast data for a given city.
    """
    FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"
    url = f"{FORECAST_URL}?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP errors
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error fetching forecast data: {response.status_code}")
            return None
    except requests.RequestException as e:
        st.error(f"Error fetching forecast data: {e}")
        return None


def log_search(city_name: str, temperature: float, humidity: int, wind_speed: float):
    """Log search data to a SQLite database stored at the repo root."""
    import sqlite3

    db_path = Path(__file__).resolve().parent / "weather_searches_laszlolaszlo.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS searches (
                    id INTEGER PRIMARY KEY,
                    city_name TEXT,
                    temperature REAL,
                    humidity INTEGER,
                    wind_speed REAL,
                    search_time TEXT
                )
                """
            )

            search_time = datetime.datetime.now().isoformat()
            cursor.execute(
                """
                INSERT INTO searches (city_name, temperature, humidity, wind_speed, search_time)
                VALUES (?, ?, ?, ?, ?)
                """,
                (city_name, temperature, humidity, wind_speed, search_time),
            )
            conn.commit()
    except Exception as e:
        st.error(f"Error logging search: {e}")


def main():
    st.title("Weather Dashboard")
    st.sidebar.header("Configuration")

    city_name: str = st.sidebar.text_input("Enter City Name:", "Salomvár")

    weather_data: dict | None = fetch_weather_data(city_name=city_name)
    if weather_data:
        st.subheader(f"Current Weather in {city_name}")
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Temperature", value=f"{temp} °C")
        col2.metric(label="Humidity", value=f"{humidity} %")
        col3.metric(label="Wind Speed", value=f"{wind_speed} m/s")

        st.subheader("Weather Map")
        lat = weather_data["coord"]["lat"]
        lon = weather_data["coord"]["lon"]
        map_data = pd.DataFrame({"lat": [lat], "lon": [lon]})
        st.map(map_data)

        log_search(city_name, temp, humidity, wind_speed)
    else:
        st.error("Could not fetch weather data.")
        return

    forecast_data: dict | None = fetch_forecast_data(city_name=city_name)
    if forecast_data:
        st.subheader(f"5-Day Forecast for {city_name}")
        forecast_list = forecast_data["list"]
        dates = [entry["dt_txt"] for entry in forecast_list]
        temps = [entry["main"]["temp"] for entry in forecast_list]
        humidities = [entry["main"]["humidity"] for entry in forecast_list]
        wind_speeds = [entry["wind"]["speed"] for entry in forecast_list]

        df_forecast = pd.DataFrame(
            {
                "Date": dates,
                "Temperature": temps,
                "Humidity": humidities,
                "Wind Speed": wind_speeds,
            }
        )

        fig_temp = px.line(
            df_forecast, x="Date", y="Temperature", title="Temperature Forecast"
        )

        fig_humidity = px.bar(
            df_forecast,
            x="Date",
            y="Humidity",
            title="Humidity Forecast",
            color="Humidity",
        )

        fig_wind = px.bar(
            df_forecast,
            x="Date",
            y="Wind Speed",
            title="Wind Speed Forecast",
            color="Wind Speed",
        )

        st.plotly_chart(fig_temp)
        st.plotly_chart(fig_humidity)
        st.plotly_chart(fig_wind)

    else:
        st.error("Could not fetch forecast data.")


if __name__ == "__main__":
    main()
