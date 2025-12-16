import requests
import settings as s
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import db_connector as dbc
import datetime as dt

API_KEY = st.secrets["massive"]["api_key_owm"]

base_url_weather = "https://api.openweathermap.org/data/2.5/weather"
base_url_forecast = "http://api.openweathermap.org/data/2.5/forecast"


@st.cache_data(ttl=86400)  # Nehogy kicsússzunk a kérési leheőségekből....
def current_weather_info(city):
    """
    Docstring for current_weather_info
    Ask current weather information about requested city.

    :param city: Name of city.
    """
    url = f"{base_url_weather}?q={city}&appid={API_KEY}&units=metric"
    print(url)  # összerakjuk az url-t a jelenlegi értékekhez

    response = requests.get(url)  # le is kérjük az adatokat

    if response.status_code == 200:  # Megnézzük, hogy jött-e válasz.
        print(response.text)  # Kiírjuk. ( benn hagytam, bár zavar kicsit)
        return response.json()  # visszaadjuk az eredményt a hívónak json-ban.
    else:
        st.error(
            f"Failed to fetch data: {response.status_code} - {response.text}"
        )  # Ha netán nem jó valami....


def forecast_weather_info(city):
    """
    Docstring for forecast_weather_info
    Ask forecast about this city for next 5 days.
    :param city: Name of city.
    """
    url = f"{base_url_forecast}?q={city}&appid={API_KEY}&units=metric"
    print(url)  # összerakjuk az url-t, most az 5 napos forecast-ra.

    response = requests.get(
        url
    )  # Meg is kérjük a szervert, hogy adja meg a kért infókat.

    if response.status_code == 200:  # Mengézzük, hogy jött-e válasz.
        return_file = response.json()  # Visszaadjuk Json-ban.
        return (
            return_file  # dict, itt valamit ellenőriztem, benne hagyom, így is lehet.
        )

    else:
        st.error(
            f"Failed to fetch data: {response.status_code} - {response.text}"
        )  # Ha netán gond lenne...


def process_data(data):
    """
    Docstring for process_data
    Process data from json. Give back temperature, humidity, wind speed to show.

    :param data: Json format from webpage dicetly.
    """
    if "main" in data:  # ha van main az adatok között, valószínűleg van adat.

        df1 = pd.DataFrame(
            [data["main"]]
        )  # kiszedjük a main részt az adathalmazból, abban van a temp, humidity, windspeed.
        df2 = pd.DataFrame([data["wind"]])  # kiszedjük a wind infót is.

        current_temp = df1["temp"].iloc[0]  # kiszedjük magukat az értékeket.
        current_humidity = df1["humidity"].iloc[0]
        current_wind_speed = df2["speed"].iloc[0]

        df_coord = pd.DataFrame(
            [data["coord"]]
        )  # kiszedem a koordinátákat is a későbbi térképes megjelenítéshez

        return (
            current_temp,
            current_humidity,
            current_wind_speed,
            df_coord,
        )  # Visszaadom az összes adatot a kérőnek...

    else:
        st.error(
            "Gáz van babám..."
        )  # Ha netán nem jön adat, lássam, hogy nem jött adat. :)
        None


def process_data_forecast(data):  # input: dict
    """
    From list ( openweathermap 5 days forcast ) generates datetime and temp frame with datetime index.

    """
    if "list" in data:  # ha van lista a json-ból nyert adatban,

        list_of_data = data["list"]  # list                 # ki is nyerjük a listát
        df = pd.DataFrame(list_of_data)  # csinálunk egy pandas DF-et.
        df["dt"] = pd.to_datetime(
            df["dt"], unit="s"
        )  # a 70-estől a sec-eket datetime-osítjuk

        df = df[["dt", "main"]]  # kitörlöm a felesleges olszlopokat
        df["temp"] = df["main"].apply(
            lambda x: x["temp"]
        )  # a main dic-t-ből ki kell kaparni a temp értékeket soronként
        df = df[
            ["dt", "temp"]
        ]  # Megint DF takarítás. Lehet, hogy ismétlés, de így adta
        df.set_index(
            "dt", inplace=True
        )  # dt adatot indexbe, mert a streamlit így szereti
        return df  # majd jól visszaadom a df-et, akármi is legyen az, majd mindjárt kiderül


def main():  # A fővágány, itt áll össze minden.
    st.title(
        "Robot Dreams Python - Weather Map & Data Visualization Apр"
    )  # kiírjuk, amit kell...
    st.markdown("Location:")
    city_name = st.text_input("Enter city name:", "Budapest")
    st.subheader(
        f"Current weather in {city_name}:"
    )  # Itt azt is, hogy mi a város, ami érdekel minket.
    st.subheader("")  # Kis formázás

    data = current_weather_info(
        city_name
    )  # Itt hívjuk meg az API lekérdezést, vagy hogy is hívják...
    temp, humidity, wind_speed, df_coord = process_data(
        data
    )  # Aztán meghívjuk az adatkinyerés függvényt is.
    if (
        temp and humidity and wind_speed and df_coord is not None
    ):  # Ellenőrzés, nehogy valami hiányozzon.

        text1, text2, text3 = st.columns(
            3
        )  # Három oszlopba rendezzük a három fő adatot.

        with text1:  # 1. felirat
            st.markdown("Temperature (°C)")
        with text2:  # 2. felirat
            st.markdown("Humidity (%)")
        with text3:  # 3. felirat
            st.markdown("Wind Speed (m/s)")

        temperature_v, humidity_v, wind_speed_v = st.columns(3)

        with temperature_v:  # 1. adat
            st.header(f"{temp} °C")

        with humidity_v:  # 2. adat
            st.header(f"{humidity} %")

        with wind_speed_v:  # 3. adat
            st.header(f"{wind_speed} m/s")

    st.subheader("Weather Map")  # Még egy kis felirat
    st.map(df_coord)

    data2 = forecast_weather_info(city_name)  # API lekérés....

    list_of_forecast = process_data_forecast(data2)  # Adat feldolgozás az eredményre.

    # forecast grafikon

    st.subheader("5 days forecast. [TEMP in °C]")  # Fejléc
    fig_forecast = px.line(  # Jó kis grafikonösszerakóadat.
        list_of_forecast,
        x=list_of_forecast.index,
        y="temp",
        title=f"{city_name} temperature trends. (next 5 days)",
    )
    st.plotly_chart(
        fig_forecast
    )  # Jó kis grafikon. Bár az AM/PM formázást nem csináltam meg...

    now = dt.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )  # Adatbázis beíráshoz megkérdezem a most-ot, mint Chuck Norris.

    with dbc.SqliteDB(
        "homeworks/rederkonstantin/hw_08_streamlit/weather_log"
    ) as db:  # Be is írom a létrehozott db-be.
        db.write_single_record(
            "logs",
            {
                "date": now,
                "city": city_name,
                "temp": temp,
                "humidity": int(
                    humidity
                ),  # valamiért nagyon furcsa adatok kerültek beírásra, formázás után rendben van a beírás.
                "wind_speed": wind_speed,
            },
        )


if __name__ == main():
    main()

# streamlit run homeworks/rederkonstantin/hw_08_streamlit/owm.py
