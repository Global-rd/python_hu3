import streamlit as st
import requests
import pandas as pd

# OpenWeatherMap API alapbeállítások
API_KEY = st.secrets["open_weather"]["api_key"]
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"


@st.cache_data(ttl=3600)
def get_current_weather(city_name: str, api_key: str) -> dict | None:
    """
    Időjárási adatok lekérése egy adott városra.
    Cache-elve van, hogy ne hívjuk feleslegesen az API-t.
    """
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
        "lang": "hu",
    }

    try:
        response = requests.get(WEATHER_URL, params=params, timeout=5)
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    return response.json()


def main():
    st.title("Időjárás – város alapú lekérdezés")

    # Városnév bekérése
    city_input = st.text_input("Add meg a település nevét:", value="London")

    if not city_input:
        st.info("Kérlek, adj meg egy városnevet a lekérdezéshez.")
        return

    weather_payload = get_current_weather(city_input, API_KEY)

    if not weather_payload:
        st.warning("Nem sikerült lekérdezni az időjárási adatokat. "
                   "Ellenőrizd a város nevét, vagy próbáld újra később.")
        return

    # Dinamikus cím az aktuális várossal
    st.subheader(f"Aktuális időjárás: {city_input}")

    # Fő mutatók (KPI-k)
    col_temp, col_hum, col_wind = st.columns(3)

    with col_temp:
        st.caption("Hőmérséklet (°C)")
        st.subheader(f"{weather_payload['main']['temp']:.1f}")

    with col_hum:
        st.caption("Relatív páratartalom (%)")
        st.subheader(f"{weather_payload['main']['humidity']}")

    with col_wind:
        st.caption("Szélsebesség (m/s)")
        st.subheader(f"{weather_payload['wind']['speed']}")

    # Térkép az adott város koordinátáival
    st.subheader("Térképes megjelenítés")
    coord_frame = pd.DataFrame(
        [
            {
                "lat": weather_payload["coord"]["lat"],
                "lon": weather_payload["coord"]["lon"],
            }
        ]
    )
    st.map(coord_frame, zoom=10)


if __name__ == "__main__":
    main()
