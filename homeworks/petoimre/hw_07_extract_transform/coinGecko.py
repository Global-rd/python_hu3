import requests
import settings as s
import pandas as pd


# basic_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false"
basic_url = "https://api.coingecko.com/api/v3/coins/markets"

api_params = {"vs_currency": s.CURRENCY,
              "order": s.ORDER,
              "per_page": s.PER_PAGE,
              "page": s.PAGE,
              "sparkline": s.SPARKLINE}

response = requests.get(url=basic_url, params=api_params).json()





df = pd.DataFrame(response)
print(df)
print(df.info())                                   # 1./

sum_market_cap = df["market_cap"].sum()            # 2./
print(sum_market_cap)

top50_df = df.nlargest(50, "current_price")        # 3./
print(top50_df)

desc_by_pcp24h = top50_df.sort_values("price_change_percentage_24h", ascending=False)    # 4./
print(desc_by_pcp24h)

def determine_change_direction(row):
        if row["price_change_percentage_24h"] > 0:
            return "+"
        elif row["price_change_percentage_24h"] < 0:
            return "-"
        else:
            return "0"
        

top50_df["change_direction"] = top50_df.apply(determine_change_direction, axis=1)

"""
top50_df["change_direction"] = "0"            
top50_df.loc[df["price_change_percentage_24h"] > 0, "change_direction"] = "+"           # 5./
top50_df.loc[df["price_change_percentage_24h"] < 0, "change_direction"] = "-"

print(top50_df)


"""

