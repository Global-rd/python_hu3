import requests
import streamlit as st
import pandas as pd
import plotly.express as px

api_key=st.secrets["weather"]["api_key"]
base_url = f'https://api.openweathermap.org/data/2.5/weather'

@st.cache_data(ttl=86400)
def fetch_current_weather(city):
    print(f"Fetch data for {city}")
    url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("City not found.{response.status_code},{response.text}")
    return None

def process_weather_data(data):
    if "main" in data:
        df = pd.DataFrame([data])

        return df
    else:
        st.error("No data available")
        return None

def main():
    st.title("Weather App")
    st.sidebar.header("Configuration")
    city = st.sidebar.text_input("Enter city name:e.g.:London,Warsaw,New York")
    if city:
        data = fetch_current_weather(city)
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
            st.subheader(f"Weather Details for {city}")
            lat = df['coord'][0]['lat']
            lon = df['coord'][0]['lon']
            st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}), zoom=10)

if __name__ == "__main__":
    main()

