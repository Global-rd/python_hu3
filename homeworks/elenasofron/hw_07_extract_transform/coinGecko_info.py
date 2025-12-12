import requests
import pandas as pd

def get_top_250_cryptos():

    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",  
        "order": "market_cap_desc",  
        "per_page": 250,  
    }

    try:  
        with requests.get(url, params=params, timeout=10) as response:
            if response.status_code == 200:  
                return response.json() 
            else:  
                print(
                    f"ERROR: {response.status_code}"
                )  
                return None

    except (
        requests.RequestException
    ) as e: 
        print(f"ERROR: {e}")  
        return None
    
#print(get_top_250_cryptos())
