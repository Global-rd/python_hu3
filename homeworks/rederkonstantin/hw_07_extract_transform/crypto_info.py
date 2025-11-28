import requests
import pandas as pd


def get_top_250_cryptos():
    """
    Request to suck top 250 crypto ordered by market value.
    Output: .json
    """

    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",  # USD-ben legyen a valuta
        "order": "market_cap_desc",  # Rendezzük piaci kapitalizáció szerint csökkenő sorrendbe, bármit is jelentsen. :)
        "per_page": 250,  # 250 elem egy oldalon (max ennyi lehet egyszerre, fura, hogy ha nagyobb értéket adok meg, 100 lesz belőle.)
    }

    try:  # Megpróbáljuk...
        with requests.get(url, params=params, timeout=10) as response:
            if response.status_code == 200:  # ha normál válasz jött, akkor
                return response.json()  # visszaadjuk a kapott infót json-ban.
            else:  # ha nem kapunk normális választ,
                print(
                    f"Hiba történt: {response.status_code}"
                )  # kiírjuk a válasz kódját.
                return None

    except (
        requests.RequestException
    ) as e:  # ha netán a kéréssel van a baj, nem a kérés tartalmával, akkor
        print(f"Hiba a kérés során: {e}")  # kiírjuk a kéréssel kapcsolatos problémát.
        return None
