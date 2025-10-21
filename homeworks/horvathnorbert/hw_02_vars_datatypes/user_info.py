import os

# Képernyő törlés.

os.system('cls' if os.name == 'nt' else 'clear')

# A user_info dictionary létrehozása a szükséges adatokkal.

user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": [
        "pizza",
        "carbonara",
        "sushi"
    ],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000"
    }   
}

# A 4 kedvenc programozási nyelv bekérése. Az így létrehozott listát a user_info dictionaryhoz adjuk.

proglang_list = input("What are your 4 favourite programming language? (Seperated by a comma): ")
proglang_list = proglang_list.split(",")
user_info['skills'] = proglang_list

# A favourite_meals lista növekvő sorrendbe rendezése az abc szerint.

user_info["favourite_meals"].sort()

# A favourite_meals lista, valamint a lista utolsó előtti elemének képernyőre írása.

print(user_info["favourite_meals"])
print(user_info["favourite_meals"][-2])
print("----------------------------------------------------------------")

# A speghetti hozzáadása a favourite_meals listához.

user_info["favourite_meals"].append("spaghetti")

# A ffavourite_meals-hez hozzáadjuk az aktuális favourite_meals lista harmadik és negyedik elemét újra.

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# Az így létrejött duplikátumok törlése a favourite_meals set-té alakításával. Majd ismét listává alakítás.

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# A favourite_meals lista első és utolsó elemének felcserélése.

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

# A phone_contacts dictionary-hez egy név és egy telefonszám hozzáadása.

user_info["phone_contacts"]["Tivadar"] = "+3640506070"

# A Tim-ként elmentett telefonszám megszűnt ezért a Tim-et töröljuk a phone_contacts-ból.

del user_info["phone_contacts"]["Tim"]

# Egy új név felvétele a phone_contacts-ba akinek két telefonszáma van.

user_info["phone_contacts"]["Zebulon"] = ["+3670605040","+3630908070"]

# A skills lista, valamint a lista utolsó három elemének képernyőre írása.

print(user_info["skills"])
print(user_info["skills"][-3:][::-1])
print("----------------------------------------------------------------")

# Tim2 átnevezése Tim-re

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print(user_info["phone_contacts"])



      

