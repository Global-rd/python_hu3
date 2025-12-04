import streamlit as st
import plotly.express as px
import datetime as dt
import requests
import pandas as pd

API_KEY =st.secrets["open_weather"]["api_key"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
BASE_URL_FORECAST = "http://api.openweathermap.org/data/2.5/forecast"

@st.cache_data(ttl=86400)
def fetch_weather_data(city: str, api_key: str) -> dict:  
    today = dt.date.today()
    start_date = today - dt.timedelta(days=7)  
    params = {
        "q": city,
        "appid": api_key,   
        "units": "metric",
        "lang": "hu"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        st.error("Hiba történt az időjárási adatok lekérése során.")
        return {}   
    return response.json()  

@st.cache_data(ttl=86400)
def fetch_forecast_data(city: str, api_key: str) -> dict:  
    params = {
        "q": city,
        "appid": api_key,   
        "units": "metric",
        "cnt": 40,
        "lang": "hu"
    }
    response = requests.get(BASE_URL_FORECAST, params=params)
    if response.status_code != 200:
        st.error("Hiba történt az előrejelzési adatok lekérése során.")
        return {}   
    return response.json()

def main():
    st.title("Időjárás alkalmazás")

    city = st.text_input("Város neve:", "London")    
    if city:
        weather_data = fetch_weather_data(city, API_KEY)         
        if weather_data:
            st.subheader(f"Időjárás {city} városában")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.write("Hőmérséklet")
                st.subheader( f"{weather_data['main']['temp']} °C")
            
            with col2:
                st.write("Páratartalom")
                st.subheader(f"{weather_data['main']['humidity']} %")
            
            with col3:
                st.write("Szélsebesség")
                st.subheader(f"{weather_data['wind']['speed']} km/h")

            df = pd.DataFrame(
                {"lat": [weather_data['coord']['lat']], "lon": [weather_data['coord']['lon']]}  
            )
            st.map(data=df,zoom=12) #latitude=weather_data['coord']['lat'], longitude=weather_data['coord']['lon'], 
        
        forecast_data = fetch_forecast_data(city, API_KEY)
        if forecast_data:
            st.subheader(f"Előrejelzés {city} városára")
           
            fig = px.line(
                x=[forecast_data['list'][i]['dt_txt'] for i in range(40)],
                y=[forecast_data['list'][i]['main']['temp'] for i in range(40)],
                labels={"x": "Jellemzők", "y": "Érték"},
                title="5 napos hőmérsékelt előrejelzés [°C]"
            )
            st.plotly_chart(fig)

if __name__ == "__main__":
    main()