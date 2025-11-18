import requests
import settings as s

url = "https://api.openweathermap.org/data/2.5/weather"

params = {"lat": s.BUDAPEST["lat"],
          "lon": s.BUDAPEST["lon"],
          "appid": s.OPENWEATHERMAP_API_KEY,
          "units": "metric"}

response = requests.get(url=url, params=params).json()

print(response)
print(type(response))

city = response["name"]
print(city)
temp = response["main"]["temp"]
print(temp)

for weather in response["weather"]:
    print(weather["description"])