import streamlit as st
import requests
import pandas as pd

# időjárás lekérdezés API-val
# halványkék háttér
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6f2ff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(ttl=600)
def get_current_weather(city: str, api_key: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city.strip(), "appid": api_key.strip(), "units": "metric"}
    r = requests.get(url, params=params, timeout=10)
    if r.status_code != 200:
        return None
    return r.json()


def main():
    st.set_page_config(page_title="Weather App", layout="centered")

    api_key = st.secrets["OPENWEATHER_API_KEY"]

    st.title("🌦️ Robot Dreams Python - Weather App")

    city = st.text_input("Enter city name", value="Budapest")

    if not city:
        return

    data = get_current_weather(city, api_key)

    if data is None:
        st.warning("❌ City not found or API error.")
        return

    # adat kinyerés
    # időjárás
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    # koordináta-város

    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]

    st.subheader(f"Current Weather in {city}")

    col1, col2, col3 = st.columns(3)

    col1.metric("Temperature (°C)", f"{temp:.1f}")
    col2.metric("Humidity (%)", f"{humidity}")
    col3.metric("Wind Speed (m/s)", f"{wind_speed}")

    st.subheader("Weather Map")

    map_df = pd.DataFrame(
        {
            "lat": [lat],
            "lon": [lon],
        }
    )

    st.map(map_df)


if __name__ == "__main__":
    main()
