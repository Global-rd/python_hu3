import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) 

#.env-be van az url itt lenne az api kulcs is +.gitignore-ba is benne van a .env

try:
    GECKO_API_URL = os.environ["GECKO_API_URL"] 
except KeyError as exc:
    raise RuntimeError(
    "GECKO_API_URL environment variable not set. Please set it in the .env file."
    ) from exc 

#paraméterek

GECKO_CURRENCY = os.environ.get("GECKO_CURRENCY", "usd")
GECKO_ORDER =os.environ.get("GECKO_ORDER", "market_cap_desc")
GECKO_PER_PAGE = int(os.environ.get("GECKO_PER_PAGE", "250"))