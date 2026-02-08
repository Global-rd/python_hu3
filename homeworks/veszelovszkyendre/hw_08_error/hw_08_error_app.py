import streamlit as st
import requests
import pandas as pd

# weather_api_app v1.0
st.set_page_config(
    page_title="Weather Map & Data Visualization App",
    layout="wide"
)

API_KEY = st.secrets["openweather"]["api_key"]


def get_current_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise ValueError(
            f"Hiba az API hívásnál: {response.status_code} - {response.text}"
        )

    return response.json()


def get_forecast(city: str):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise ValueError(
            f"Hiba az előrejelzés API hívásnál: {response.status_code} - {response.text}"
        )

    return response.json()


def main():
    st.markdown("Veszelovszky Endre")
    st.title("Weather Map & Data Visualization App")

    st.write("Add meg egy város nevét! (OpenWeather API)")

    city = st.text_input("Város neve", value="Vámospércs")

    if not city:
        st.info("Adj meg egy városnevet a fenti mezőben!")
        return

    if st.button("Időjárás lekérése"):

        try:
            data = get_current_weather(city)
        except Exception as e:
            st.error(
                f"Nem sikerült lekérni az aktuális időjárást. Részletek: {e}")
            return

        st.subheader("Aktuális időjárás")

        city_name = data.get("name", city)

        main_data = data.get("main", {})
        wind_data = data.get("wind", {})
        coord_data = data.get("coord", {})

        temp = main_data.get("temp", None)
        humidity = main_data.get("humidity", None)
        wind_speed = wind_data.get("speed", None)
        lat = coord_data.get("lat", None)
        lon = coord_data.get("lon", None)

        st.write(f"**Város:** {city_name}")

        col1, col2, col3 = st.columns(3)

        with col1:
            if temp is not None:
                st.metric("Hőmérséklet (°C)", f"{temp:.1f}")
            else:
                st.metric("Hőmérséklet (°C)", "N/A")

        with col2:
            if humidity is not None:
                st.metric("Páratartalom (%)", f"{humidity}")
            else:
                st.metric("Páratartalom (%)", "N/A")

        with col3:
            if wind_speed is not None:
                st.metric("Szélsebesség (m/s)", f"{wind_speed:.1f}")
            else:
                st.metric("Szélsebesség (m/s)", "N/A")

        st.subheader("Térkép")

        if lat is not None and lon is not None:
            map_df = pd.DataFrame(
                {
                    "lat": [lat],
                    "lon": [lon],
                }
            )
            st.map(map_df, zoom=10)
        else:
            st.info(
                "Nem érkeztek koordináták az API válaszból, így nem tudok térképet mutatni.")

        st.subheader("Előrejelzés – Hőmérséklet a következő napokban")

        try:
            forecast_data = get_forecast(city_name)
        except Exception as e:
            st.warning(f"Nem sikerült lekérni az előrejelzést. Részletek: {e}")
            return

        records = []
        for item in forecast_data.get("list", []):
            dt_txt = item.get("dt_txt")
            main_f = item.get("main", {})
            temp_f = main_f.get("temp", None)

            if dt_txt is not None and temp_f is not None:
                records.append(
                    {"datetime": dt_txt, "temperature": temp_f}
                )

        if not records:
            st.info("Az előrejelzésben nem találtam megjeleníthető adatot.")
        else:
            forecast_df = pd.DataFrame(records)
            forecast_df["datetime"] = pd.to_datetime(forecast_df["datetime"])
            forecast_df = forecast_df.set_index("datetime")

            st.line_chart(forecast_df["temperature"], height=300)


if __name__ == "__main__":
    main()
