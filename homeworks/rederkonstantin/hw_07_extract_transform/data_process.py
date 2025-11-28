# Csak, hogy szép is legyen....

# imports  Behívjuk a függvényt az adat lekéréshez.

from crypto_info import get_top_250_cryptos
import pandas as pd  # Meg a jó öreg PANDAS-t is.


df_main = pd.DataFrame(
    get_top_250_cryptos()
)  # Mivel már tudni lehet a feladat leírásból, hogy több adatkeret lesz, nem sima df.

print(df_main.isna().sum())  # Kinyomtatjuk az üres cellák mennyiségét oszloponként.

total_maket_cap = df_main["market_cap"].sum()  # kiszámítjuk a 'market_cap' összegét.

print("-------------------------------------------------")
print(
    f"Sum of macket_cap is {total_maket_cap:.0f} USD."
)  # Majd ki is írjuk a consol-ra.
print("-------------------------------------------------")

top50_df_by_current_price = df_main.sort_values(
    "current_price", ascending=False
)[  # sorba rendezünk csökkenő sorrendbe,
    0:50  # ebből vesszük az első 50 sort,
].reset_index()  # indexet rendezünk,
print(top50_df_by_current_price)  # kiírjuk az eredményt a consol-ra.
print("-------------------------------------------------")

top50_df_by_current_price = top50_df_by_current_price.sort_values(
    "price_change_percentage_24h",
    ascending=False,  # újra rendezzük az adattáblát szintén csökkenő sorrendbe,
).reset_index()  # indexet rendezünk,


print(top50_df_by_current_price)  # Kiírjuk az eredményt a consol-ra.
print("-------------------------------------------------")
print(
    top50_df_by_current_price["price_change_percentage_24h"]
)  # Itt csak magamat ellenőrzöm, vagyis a kódot.

top50_df_by_current_price["change_direction"] = "NaN"  # létrehozom az új oszlopot.


def categorize_by_price_change_percentage_24h(row):  # függvény az apply-hez.
    """
    Categorizes lines according to value of price_change_percentage_24h.
    This function is for aply method.
    "+" if value > 0
    "-" if value < 0
    "0" if value = 0
    Print error if value is not a number.
    :param row: row of dataframe.
    """

    if row["price_change_percentage_24h"] > 0:  # Ha az érték nagyobb mint 0,
        return "+"  # akkor "+",
    elif row["price_change_percentage_24h"] < 0:  # ha az érték kisebb mint 0,
        return "-"  # akkor "-",
    elif row["price_change_percentage_24h"] == 0:  # ha 0,
        return "0"  # akkor "0"(str),
    else:  # amúgy meg
        print("Something wrong happened.... :)")  # hibát írunk a consol-ra.


# A megcímzett oszlopot írjuk felül a fenti függvénnyel az apply metódussal.
top50_df_by_current_price["change_direction"] = top50_df_by_current_price.apply(
    categorize_by_price_change_percentage_24h, axis=1
)

# Meg még ellenőrzök is párat.
print(top50_df_by_current_price["change_direction"])
print(top50_df_by_current_price["price_change_percentage_24h"])
