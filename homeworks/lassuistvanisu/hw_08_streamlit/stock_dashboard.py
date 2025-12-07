import streamlit as st
import plotly.express as px
import requests
import pandas as pd
import sqlite3
import os
from datetime import datetime


# ============ DATABASE INICIALIZATION ============

DATABASE_FILE = "weather_search_log.db"

def init_database():
    
    #Inicializálja az SQLite adatbázist és létrehozza a szükséges táblát.
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Tábla létrehozása, ha nem létezik
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_name TEXT NOT NULL,
            temperature REAL,
            humidity INTEGER,
            wind_speed REAL,
            search_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()


def log_search(city_name, temperature, humidity, wind_speed):
    
    #Naplózza a keresést az SQLite adatbázisba.
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    current_time = datetime.now()
    
    cursor.execute('''
        INSERT INTO weather_log (city_name, temperature, humidity, wind_speed, search_time)
        VALUES (?, ?, ?, ?, ?)
    ''', (city_name, temperature, humidity, wind_speed, current_time))
    
    conn.commit()
    conn.close()
    
    print(f"Logged: {city_name} | Temperature: {temperature}°C | Humidity: {humidity}% | Wind seed: {wind_speed} m/s | Time: {current_time}")


def get_search_history(limit=10):
    # Lekérdezi az utolsó N keresést az adatbázisból.
    
    conn = sqlite3.connect(DATABASE_FILE)
    query = f'''
        SELECT city_name, temperature, humidity, wind_speed, search_time
        FROM weather_log
        ORDER BY search_time DESC
        LIMIT {limit}
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    return df

# ============ WEATHER API ============
#URL Create
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

API_KEY=st.secrets["openweathermap"]["api_key"]
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

@st.cache_data(ttl=900)
def fetch_stock_data(city_name):
    print(f"Fetch data {city_name}")
    
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    print(url)
    response =requests.get(url)

    if response.status_code == 200:
        print(response.text)
        return response.json()
    else:
        st.error(f"Faild to fetch data: {response.status_code} - {response.text}")
        return None

# Datafrane Craete
def process_data(data):

    if  "coord" in data and "main" in data and "wind" in data:
        df = pd.DataFrame([ {**data['coord'],**data['main'], **data['wind']} ])
        df = df.drop(columns=["feels_like", "temp_min", "temp_max", "sea_level", "grnd_level"])
        
        numeric_float_columns = ["lon", "lat","temp", "speed"]
        numeric_int_columns = ["pressure", "humidity", "deg"] 
        
        df[numeric_float_columns] = df[numeric_float_columns].astype(float)
        df[numeric_int_columns] = df[numeric_int_columns].astype(int)
        print(df)
    
        first_row = df.iloc[0]
        temperature = first_row['temp']
        humidity = first_row['humidity']
        wind_speed = first_row['speed']
        
        return df, temperature, humidity, wind_speed
    
    else:
        st.error("No data available")
        return None, None, None, None
    
#Dashboard Create
def main():
    st.title("Robot Dreams Python - Weather Map & Data Visualization App")
    
    init_database()
    data = None

    stock_city_name = st.text_input(
        "Enter City Name: ", "Budapest"
    )
    if st.button("Search Weather"):
        data = fetch_stock_data(stock_city_name)
        
    if data:
        df, temperature, humidity, wind_speed = process_data(data)
        st.header(f"Current Weather in {stock_city_name}")

        if df is not None:
            
            # NAPLÓZÁS - Az adatok mentése az adatbázisba
            log_search(stock_city_name, temperature, humidity, wind_speed)
            
            temp_kpi, humid_kpi, wind_kpi = st.columns(3)

            # TEMP KPI
            with temp_kpi:
                st.metric(label="Tempature (°C)", value=f"{df['temp'].values[0]} °C")
            # HUMINIDY KPI
            with humid_kpi:
                st.metric(label="Humidity (%)", value=f"{df['humidity'].values[0]} %")
            # WIND KPI
            with wind_kpi:
                st.metric(label="Wind Speed (m/s)", value=f"{df['speed'].values[0]} m/s")

            #MAPS
            st.subheader("Weather Map")
            st.map(df[['lat', 'lon']])

    else:
        st.error("No data! Please enter the city name and click the 'Search' button!")

 # ============ SEARCH HISTORY  ============
    
    st.divider()
    st.subheader("Search History")
    
    # History lekérdezése
    history_df = get_search_history(limit=20)
    
    if not history_df.empty:
        # Oszlopok átnevezése
        history_df.columns = ['City', 'Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)', 'Search Time']
        
        # Formázás
        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )
        
        # Statisztikák
        st.subheader("Statistics")
        total_searc_kpi, avg_temp_kpi, avg_humidity_kpi = st.columns(3)
        
        with total_searc_kpi:
            st.metric("Total Searches", len(history_df))
        
        with avg_temp_kpi:
            avg_temp = history_df['Temperature (°C)'].mean()
            st.metric("Average Temperature", f"{avg_temp:.2f}°C")
        
        with avg_humidity_kpi:
            avg_humidity = history_df['Humidity (%)'].mean()
            st.metric("Average Humidity", f"{avg_humidity:.1f}%")
        
        # CSV export
        if st.button("Download Search History as CSV"):
            csv = history_df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"weather_search_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
    else:
        st.info("No search history yet.")
    
    #Database dates
    st.divider()
    if os.path.exists(DATABASE_FILE):
        db_size = os.path.getsize(DATABASE_FILE) / 1024  # KB-ban
        st.caption(f" Database size: {db_size:.2f} KB | File: {DATABASE_FILE}")



if __name__=="__main__":
    main()

