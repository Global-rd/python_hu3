import streamlit as st
import plotly.express as px
import datetime
import requests
import pandas as pd
from datetime import datetime, timedelta

API_KEY = st.secrets["openweathermap"]["api_key"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
BASE_URL_EXTRA = "https://api.openweathermap.org/data/2.5/forecast"
UNITS = "metric"

most = datetime.now()
nap_vege = datetime(most.year, most.month, most.day) + timedelta(days=1)
hatra = (nap_vege - most).total_seconds()


@st.cache_data(ttl=hatra)
def fetch_weather_forecast(city):
    print(f"Fetch forecast data for {city}")

    url = f"{BASE_URL_EXTRA}?q={city}&appid={API_KEY}&units={UNITS}"
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
        return response.json()
    else:
        st.error(f"Error: {response.json()['message']}")


@st.cache_data(ttl=1800)
def fetch_current_weather(city):
    print(f"Fetch data for {city}")

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units={UNITS}"
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.json()['message']}")


def process_weather_data(data):
    if "main" in data:
        df = pd.DataFrame([data])

        return df
    else:
        st.error("No data available")
        return None


def process_forecast_data(forecast):
    if "list" in forecast:
        # df = pd.json_normalize(forecast["list"])
        df = pd.DataFrame(
            [
                {"dt": forecast["dt"], "main.temp": forecast["main"]["temp"]}
                for forecast in forecast["list"]
            ]
        )
        df["timestamp"] = pd.to_datetime(df["dt"], unit="s")
        df.set_index("timestamp", inplace=True)
        df = df[["main.temp"]]
        df = df.rename(columns={"main.temp": "Temperature"})
        df.sort_index()
        return df

    else:
        st.error("No forecast data available")
        return None


def main():

    st.title("Current Weather Dashboard")
    city = st.text_input(
        "Enter City Name: (e.g.: Budapest, London, New York)", "Budapest"
    )

    st.subheader(f"Current Weather in {city}")
    data = fetch_current_weather(city)
    forecast = fetch_weather_forecast(city)

    # print(data)

    if data:
        df = process_weather_data(data)
        if df is not None:

            kpi1, kpi2, kpi3 = st.columns(3)
            with kpi1:
                st.metric(label="Temperature (°C)", value=f"{df['main'][0]['temp']} °C")
            with kpi2:
                st.metric(label="Humidity (%)", value=f"{df['main'][0]['humidity']} %")
            with kpi3:
                st.metric(
                    label="Wind Speed (m/s)", value=f"{df['wind'][0]['speed']} m/s"
                )

        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        st.map(
            pd.DataFrame({"lat": [lat], "lon": [lon]}), zoom=10, height=400, size=200
        )
    else:
        st.error("No data available")

    if forecast:
        df_forecast = process_forecast_data(forecast)
        print(df_forecast)
        if df_forecast is not None:
            st.subheader(f"5-Day Weather Forecast for {city}")
            fig = px.line(
                df_forecast,
                x=df_forecast.index,
                y=["Temperature"],
                title="Temperature Trend Next 5 days",
                # labels={"timestamp": "Date", "Temperature": "Temperature (°C)"},
            )
            st.plotly_chart(fig)
    else:
        st.error("No data available")


if __name__ == "__main__":
    main()
