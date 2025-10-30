import os

# Képernyő törlés.
os.system('cls' if os.name == 'nt' else 'clear')

# Kritériumok eltárolása egy dictionaryben.

flat_criteria = {"newyork": 4000,
                "sanfrancisco": 4000,
                "chicago": float('inf'),
                "washington": float('-inf')}

city_name = input("Name of the city? : ").lower().replace(" ","") #Szóközök eltávolítása és kisbetűsként való eltárolás.

flat_price = int(input("Flat price? : ").replace(" ","")) #Szóközök eltávolítása és integerként való eltárolás.

# A feladatban leírt kritériumok ellnőrzés.

if city_name == "newyork" and flat_price < flat_criteria[city_name]:
    print("I would love to rent this apartment.")

elif city_name == "sanfrancisco" and flat_price < flat_criteria[city_name]:
    print("I would love to rent this apartment.")

elif city_name == "chicago":
    print("I love Chicago! It is worth every cent to live here.")

elif city_name == "washington":
    print("I hate Washington! You could not pay me to live here!")

elif flat_price < 3000:
    print("I would love to rent this apartment.")
else:
    print("I would not like to rent this apartment. Maybe if it were a bit cheaper.")