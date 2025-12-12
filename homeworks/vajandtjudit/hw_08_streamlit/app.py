import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# ------------------------
#      API FUNCTIONS
# ------------------------

@st.cache_data(ttl=600)
def get_current_weather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "hu"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None
    return response.json()


@st.cache_data(ttl=600)
def get_forecast(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "hu"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None
    return response.json()


# ------------------------
#        UI START
# ------------------------

st.title("Időjárás lekérdezés")

city = st.text_input("Írd be a város nevét:")

if city:
    api_key = st.secrets["OPENWEATHER"]["API_KEY"]
    
    # Current weather lekérése
    data = get_current_weather(city, api_key)

    if data:
        st.subheader(f"Aktuális időjárás: **{city}**")
        st.write(f"Hőmérséklet: {data['main']['temp']} °C")
        st.write(f"Szél: {data['wind']['speed']} m/s")
        st.write(f"Leírás: {data['weather'][0]['description']}")

        # ------------------------
        #          KPI-ok
        # ------------------------
        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Hőmérséklet (°C)", f"{data['main']['temp']} °C")
        col2.metric("Páratartalom (%)", f"{data['main']['humidity']} %")
        col3.metric("Szélsebesség (m/s)", f"{data['wind']['speed']} m/s")
        col4.metric("Felhőzet (%)", f"{data['clouds']['all']} %")

        # ------------------------
        #       Forecast rész
        # ------------------------
        st.markdown("---")
        forecast = get_forecast(city, api_key)

        if forecast:
            st.subheader("Időjárás előrejelzés (5 nap)")

            # DataFrame építése
            df = pd.DataFrame({
                "Dátum": [item["dt_txt"] for item in forecast["list"]],
                "Hőmérséklet": [item["main"]["temp"] for item in forecast["list"]],
                "Páratartalom": [item["main"]["humidity"] for item in forecast["list"]],
                "Szél": [item["wind"]["speed"] for item in forecast["list"]],
                "Felhőzet": [item["clouds"]["all"] for item in forecast["list"]],
            })

            df["Dátum"] = pd.to_datetime(df["Dátum"])
            df.set_index("Dátum", inplace=True)

            # Line chart (hőmérséklet)
            fig = px.line(
                df,
                x=df.index,
                y="Hőmérséklet",
                title=f"Hőmérséklet előrejelzés - {city}",
                labels={"value": "°C", "Dátum": "Időpont"}
            )
            st.plotly_chart(fig)

    else:
        st.error("Nem sikerült lekérni az időjárást. Ellenőrizd a város nevét vagy az API kulcsot.")
