import requests
import json
from pathlib import Path
from definitions import write_json

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {"vs_currency": "HUF",
          "per_page": 250}

response = requests.get(url=url, params=params).json()

json_path = Path("homeworks") / "fejeszsolt" / "hw_07_extract_transform" / "coingecko.json" 


write_json(response,json_path)