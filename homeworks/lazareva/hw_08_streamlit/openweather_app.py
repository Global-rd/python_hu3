import streamlit as st
import plotly.express as px
import requests
import pandas as pd


API_KEY = st.secrets["open_weather"]["api_key"]
BASE_URL = "https://api.openweathermap.org/data/2.5"

#cashe_data: az adatokat 3 óráig cache-eli, nem kell újra lekérdezni (mp-ben)
@st.cache_data(ttl=10800)
def get_current_weather(city):

    url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric&lang=en"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json() #az adatokat dictionary-ként adja vissza
    else:
        st.error(f"Failed to fetch data: {response.status_code} - {response.text}")

@st.cache_data(ttl=10800)
def get_forecast(city):

    url = f"{BASE_URL}/forecast?q={city}&appid={API_KEY}&units=metric&lang=en"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json() #az adatokat dictionary-ként adja vissza
    else:
        st.error(f"Failed to fetch data: {response.status_code} - {response.text}")


def main():

    st.title(f"Robot Dreams Python - Weather")
    st.header(f"Map & Data Visualization App")

    city_input = st.text_input("Enter city name")
    
    if city_input:

        current_weather = get_current_weather(city_input)
        forecast_data = get_forecast(city_input)

        if current_weather:

            # 1. Current Weather
            
            city = current_weather['name']
            st.header(f"Current Weather in {city}")

            c1, c2, c3 = st.columns(3)

            temp = current_weather['main']['temp']
            humidity = current_weather['main']['humidity']
            wind_speed = current_weather['wind']['speed']

            c1.metric("Temperature (°C)", f"{temp}°C")
            c2.metric("Humidity (%)", f"{humidity}%")
            c3.metric("Wind Speed (m/s)", f"{wind_speed} m/s")

            # 2. Weather Map

            st.subheader("Weather Map")

            lat = current_weather['coord']['lat']
            lon = current_weather['coord']['lon']

            st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))

        else:
            st.error(f"Failed to fetch weather data.")


        # 3.Temperature Trend (Forecast)

        if forecast_data:

            forecast_data_df = pd.DataFrame(forecast_data["list"])   #dataframe formátum

            forecast_data2_df = forecast_data_df[["dt_txt", "main"]] # key, időpont és az egész main blokk

            min_dt = forecast_data2_df["dt_txt"].min()
            max_dt = forecast_data2_df["dt_txt"].max()

            forecast_data2_df.set_index("dt_txt", inplace=True) # index
            forecast_data2_df = forecast_data2_df.sort_index()  # rendezés

            st.subheader("Temperature Trends (Next 5 Days)")
 
            fig_temperature = px.line(
                forecast_data2_df,
                x=forecast_data2_df.index,
	            y=forecast_data2_df["main"].apply(lambda x: x["temp"]),       
                title=f"{city} temperature trends",
                subtitle=f"{min_dt} - {max_dt}",
	            )
            st.plotly_chart(fig_temperature)

        else:
            st.error(f"No forecast data available")

if __name__ == "__main__":
    main()

