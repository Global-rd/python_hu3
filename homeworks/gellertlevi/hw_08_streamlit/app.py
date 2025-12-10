import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Weather Dashboard",   
    layout="wide",                    
    initial_sidebar_state="expanded"  
)




api_key = st.secrets["openweathermap"]["api_key"]  


@st.cache_data(ttl=600)  
def get_current_weather(city: str):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    
    response = requests.get(url)
    
    
    if response.status_code == 200:
        return response.json()  
    else:
        st.error(f"Error by creating wheather report: {response.status_code}")  
        return None  


st.sidebar.header("Select city")  
city = st.sidebar.text_input("Type the name of the city:", value="Budapest")  


if city: 
    data = get_current_weather(city)  
    if data:  
        
        
       
        temp = data['main']['temp']                    
        feels_like = data['main']['feels_like']       
        humidity = data['main']['humidity']           
        wind_speed = data['wind']['speed']            
        weather_desc = data['weather'][0]['description'].capitalize()  

        
        col1, col2, col3, col4 = st.columns(4)  
        col1.metric("Temperature(°C)", f"{temp}")           
        col2.metric("Temperature felt (°C)", f"{feels_like}") 
        col3.metric("Humidity (%)", f"{humidity}")       
        col4.metric("Wind (m/s)", f"{wind_speed}")   

        
        st.markdown(f"**Wheather report:** {weather_desc}")

       
        
        df = pd.DataFrame({
            "Properties": ["Temperature", "Felt", "Humidity", "Wind"],
            "Value": [temp, feels_like, humidity, wind_speed]
        })

        
        fig = px.bar(
            df,
            x="Properties",
            y="Value",
            color="Value",                        
            color_continuous_scale="Viridis",      
            title=f"{city} wheather data"      
        )

       
        st.plotly_chart(fig, use_container_width=True)


