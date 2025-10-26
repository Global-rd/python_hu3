"""Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát.
Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott
feltételek (város és albérlet ára) mellett be tudna e költözni az adott 
helyre."""

"""● Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban
kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD
havonta.
● Gyűlöli Washington-t, és semmi pénzért nem lakna ott
● Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit
megadna azért hogy ott lakhasson
● Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér
ellenében költözne oda.
"""

# ████████████████████████████████████████████████████████████████████████████

# lista, hogy ne lógjak ki a megengedett maximum soronkénti karakterszámból...
four_cities = ["New York", "San Fransisco", "Washington", "Chicago"]

# fő vonal ( végtelen ciklusba, hogy a tesztelésnél ne keljen indítgatni...)
while True:
    
    # bekérjük az adatokat
    city = input("Please give name of city: ")
    maximum_rent_cost = int(input("Please give maxumum cost of a rent ($): "))

    # kiértékelések
    if ((city == "New York" or city == "San Fransisco")
        and maximum_rent_cost < 4000):
        print(f"You can move into {city} for a rent of ${maximum_rent_cost}.")
    elif city == "Washington":
        print(f"You don't want to move {city}. Sure, go ahead...")
    elif city == "Chicago":
        print(f"Do it! You must move {city},\
            ${maximum_rent_cost} is a joke for it!")
    elif city not in four_cities and maximum_rent_cost < 3000:
        print(f"You can move {city} on ${maximum_rent_cost} cost.")
    else:
        print(f"You don't want to move {city}\
            for a rent of ${maximum_rent_cost}")
