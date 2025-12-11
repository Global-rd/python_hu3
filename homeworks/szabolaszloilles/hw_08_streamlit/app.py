import streamlit as st
import requests
import pandas as pd


API_KEY = st.secrets["OPENWEATHER_API_KEY"]

@st.cache_data
def get_current_weather(city):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def main():
    st.set_page_config(page_title="Weather App")

    st.title("Weather Map & Visualization")

   
    city = st.text_input("Enter city name", "London")

    if city:
        
        weather_data = get_current_weather(city)

        if weather_data:
            
            temp = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            
           
            lat = weather_data['coord']['lat']
            lon = weather_data['coord']['lon']

            
            st.subheader(f"Current Weather in {city}")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Temperature (°C)", value=f"{temp}°C")
            with col2:
                st.metric(label="Humidity (%)", value=f"{humidity}%")
            with col3:
                st.metric(label="Wind Speed (m/s)", value=f"{wind_speed} m/s")

            
            st.subheader("Weather Map")
           
            map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
            st.map(map_data)

        else:
            st.warning("City not found! Please check the spelling.")

if __name__ == "__main__":
    main()