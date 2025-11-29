import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime

# Oldal beállítások
st.set_page_config(
    page_title="Weather Map & Data Visualization App",
    layout="wide"
)

# API kulcs beolvasása a "secrets.toml"-ból.
# Feltételezzük hogy .streamlit/secrets.toml létezik, és van benne:
# [openweather]
# api_key = "YOUR_KEY"
API_KEY = st.secrets["openweather"]["api_key"]

# Adatbázis fájl ami a projekt mappájában fog létrejönni.
DB_NAME = "weather_logs.db"


# Adatbázis függvények:
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS search_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            timestamp TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def log_search(city: str, temperature: float, humidity: float, wind_speed: float):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO search_logs (city, temperature, humidity, wind_speed, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """,
        (city, temperature, humidity, wind_speed,
         datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # Eredetileg így csináltam: "datetime.now().isoformat()" csak megformáztam.
    )
    conn.commit()
    conn.close()


def load_last_logs(limit: int = 50) -> pd.DataFrame:

    conn = sqlite3.connect(DB_NAME)
    try:
        df = pd.read_sql_query(
            f"SELECT * FROM search_logs ORDER BY id DESC LIMIT {limit}",
            conn
        )
    except Exception:
        df = pd.DataFrame()
    finally:
        conn.close()
    return df


# API függvények:
<<<<<<< Updated upstream
=======
@st.cache_data(ttl=600)
>>>>>>> Stashed changes
def get_current_weather(city: str):

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Celsius
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        # Hibakezelés
        raise ValueError(
            f"Hiba az API hívásnál: {response.status_code} - {response.text}"
        )

    return response.json()


<<<<<<< Updated upstream
=======
@st.cache_data(ttl=600)
>>>>>>> Stashed changes
def get_forecast(city: str):

    # Előrejelzés lekérése: 5 nap / 3 órás felbontásban
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Metrikus rendszer -> Celsius
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise ValueError(
            f"Hiba az előrejelzés API hívásnál: {response.status_code} - {response.text}"
        )

    return response.json()


# Maga az App rész:
def main():
    # Adatbázis inicializálás (ha nincs, létrejön)
    init_db()

    st.markdown("Veszelovszky Endre")
    st.title("Weather Map & Data Visualization App")

    st.write("Add meg egy város nevét! (OpenWeather API)")

    # Városnév beviteli mező, alapértelmezett: Vámospércs (mert vámospércsi vagyok :D )
    city = st.text_input("Város neve", value="Vámospércs")

    if not city:
        st.info("Adj meg egy városnevet a fenti mezőben!")
        return

    if st.button("Időjárás lekérése"):
        try:
            data = get_current_weather(city)
        except Exception as e:
            st.error(
                f"Nem sikerült lekérni az aktuális időjárást. Részletek: {e}")
            return

        st.subheader("Aktuális időjárás")

        # Város neve (API szerinti)
        city_name = data.get("name", city)

        main_data = data.get("main", {})
        wind_data = data.get("wind", {})
        coord_data = data.get("coord", {})

        temp = main_data.get("temp", None)
        humidity = main_data.get("humidity", None)
        wind_speed = wind_data.get("speed", None)
        lat = coord_data.get("lat", None)
        lon = coord_data.get("lon", None)

        st.write(f"**Város:** {city_name}")

        # 3 KPI kártya
        col1, col2, col3 = st.columns(3)

        with col1:
            if temp is not None:
                st.metric("Hőmérséklet (°C)", f"{temp:.1f}")
            else:
                st.metric("Hőmérséklet (°C)", "N/A")

        with col2:
            if humidity is not None:
                st.metric("Páratartalom (%)", f"{humidity}")
            else:
                st.metric("Páratartalom (%)", "N/A")

        with col3:
            if wind_speed is not None:
                st.metric("Szélsebesség (m/s)", f"{wind_speed:.1f}")
            else:
                st.metric("Szélsebesség (m/s)", "N/A")

        # Adatbázis logolás
        if (temp is not None) and (humidity is not None) and (wind_speed is not None):
            try:
                log_search(city_name, float(temp), float(
                    humidity), float(wind_speed))
            except Exception as e:
                st.warning(
                    f"Nem sikerült elmenteni a lekérdezést az adatbázisba. Részletek: {e}")

        st.subheader("Térkép")

        if lat is not None and lon is not None:
            map_df = pd.DataFrame(
                {
                    "lat": [lat],
                    "lon": [lon],
                }
            )
            st.map(map_df, zoom=10)
        else:
            st.info(
                "Nem érkeztek koordináták az API válaszból, így nem lehet térképet mutatni.")

        # Grafikon:
        st.subheader("Előrejelzés – Hőmérséklet a következő napokban")

        try:
            forecast_data = get_forecast(city_name)
        except Exception as e:
            st.warning(f"Nem sikerült lekérni az előrejelzést. Részletek: {e}")
            return

        # forecast_data["list"] tartalmazza az időpontokat 3 órás bontásban
        records = []
        for item in forecast_data.get("list", []):
            dt_txt = item.get("dt_txt")       # pl. "2025-11-28 12:00:00"
            main_f = item.get("main", {})
            temp_f = main_f.get("temp", None)

            if dt_txt is not None and temp_f is not None:
                records.append(
                    {"datetime": dt_txt, "temperature": temp_f}
                )

        if not records:
            st.info("Az előrejelzésben nem található megjeleníthető adat.")
        else:
            forecast_df = pd.DataFrame(records)
            # datetime konverzió: string -> dátum-idő
            forecast_df["datetime"] = pd.to_datetime(forecast_df["datetime"])
            # időpont legyen index
            forecast_df = forecast_df.set_index("datetime")

            # ---- matplotlib-es vonaldiagram ----
            fig, ax = plt.subplots()
            ax.plot(forecast_df.index, forecast_df["temperature"])
            ax.set_xlabel("Idő")
            ax.set_ylabel("Hőmérséklet (°C)")
            ax.set_title("Előrejelzett hőmérséklet")
            fig.autofmt_xdate()

            st.pyplot(fig)

    # Log-ok megjelenítése:
    st.subheader("Keresési előzmények")

    with st.expander("Utolsó lekérdezések (SQLite adatbázis):"):
        logs_df = load_last_logs(limit=50)
        if logs_df.empty:
            st.info("Még nincs elmentett lekérdezés.")
        else:
            st.dataframe(logs_df)


if __name__ == "__main__":
    main()
