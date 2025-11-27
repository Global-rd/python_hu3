import requests
import settings as s


# basic_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false"
basic_url = "https://api.coingecko.com/api/v3/coins/markets"

api_params = {"vs_currency": s.CURRENCY,
              "order": s.ORDER,
              "per_page": s.PER_PAGE,
              "page": s.PAGE,
              "sparkline": s.SPARKLINE}

response = requests.get(url=basic_url, params=api_params).json()



#print(response.status_code)
#print(response.content)
#print(response.text)
#print(type(response.text))
print(response)                        # json esetén
print(type(response))



