import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) 

#.env-be van az url itt lenne az api kulcs is +.gitignore-ba is benne van a .env

try:
    OPENWEATHER_API_URL  = os.environ["OPENWEATHER_API_URL"] 
except KeyError as exc:
    raise RuntimeError(
    "OPENWEATHER_API_URL environment variable not set. Please set it in the .env file."
    ) from exc 

try:
    OPENWEATHER_API_URL_FORECAST  = os.environ["OPENWEATHER_API_URL_FORECAST"] 
except KeyError as exc:
    raise RuntimeError(
    "OPENWEATHER_API_URL_FORECAST environment variable not set. Please set it in the .env file."
    ) from exc 

#paraméterek

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
DEFAULT_CITY = os.getenv("DEFAULT_CITY")