import os

# Képernyő törlés.
os.system('cls' if os.name == 'nt' else 'clear')

# Kritériumok eltárolása egy mátrixban.

flat_criteria = [
    ["newyork","sanfransisco",4000],
    ["chicago"],
    ["washington"],
    [3000]
]

city_name = input("Name of the city? : ").lower().replace(" ","") #Szóközök eltávolítása és kisbetűsként való eltárolás.

flat_price = int(input("Flat price? : ").replace(" ","")) #Szóközök eltávolítása és integerként való eltárolás.

# A feladatban leírt kritériumok ellnőrzés.

if (city_name == flat_criteria[0][0] or city_name == flat_criteria[0][1]) and flat_price < flat_criteria[0][2]:
    print("I would love to rent this apartment.")

elif (city_name == flat_criteria[1][0]):
    print("I love Chicago! It is worth every cent to live here.")

elif (city_name == flat_criteria[2][0]):
    print("I hate Washington! You could not pay me to live here!")

elif (flat_price < flat_criteria[3][0]):
    print("I would love to rent this apartment.")
else:
    print("I would not like to rent this apartment. Maybe if it were a bit cheaper.")