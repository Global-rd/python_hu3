from pprint import pprint

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

# 1. Programozási nyelvek bekérése és hozzáadása a dictionary-hez
print("1. Programozási nyelvek hozzáadása")
#languages_input = input("Adj meg 4 programozási nyelvet vesszővel elválasztva (pl: Python,Java,JavaScript,C++): ")
languages_input = 'pit,jav,c,delphi'
skills_list = languages_input.split(",")
user_info["skills"] = skills_list
print(f"Skills hozzáadva: {user_info['skills']}")
pprint(user_info)
print()

# 2. Favourite_meals rendezése abc szerint
print("2. Favourite_meals rendezése")
user_info["favourite_meals"].sort()
pprint(user_info)
print()

# 3. Utolsó előtti elem kiírása
print("3. Favourite_meals utolsó előtti eleme")
print(f"Utolsó előtti elem: {user_info['favourite_meals'][-2]}")
print()

# 4. A "spaghetti" hozzáadása a listához
print("4. Spaghetti hozzáadása")
user_info["favourite_meals"].append("spaghetti")
print(f"Lista spaghetti után: {user_info['favourite_meals']}")
print()

# 5. Harmadik és negyedik elem hozzáadása újra
print("5. Harmadik és negyedik elem hozzáadása újra")
third_element = user_info["favourite_meals"][2]
fourth_element = user_info["favourite_meals"][3]
user_info["favourite_meals"].append(third_element)
user_info["favourite_meals"].append(fourth_element)
print(f"Lista duplikátumokkal: {user_info['favourite_meals']}")
print()

# 6. Duplikátumok törlése
print("6. Duplikátumok törlése")
# Lista átkonvertálása set-té, majd vissza listává
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(f"Duplikátumok törlése után: {user_info['favourite_meals']}")
print()

# 7. Első és utolsó elem felcserélése
print("7. Első és utolsó elem felcserélése")
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(f"Csere után: {user_info['favourite_meals']}")
print()

# 8. Új kontakt hozzáadása
print("8. Új kontakt hozzáadása")
user_info["phone_contacts"]["GáborM"] = "+36308787878"
pprint(user_info["phone_contacts"])
print()

# 9. Tim törlése (régi telefonszám)
print("9. Tim törlése a kontaktokból")
del user_info["phone_contacts"]["Tim"]
pprint(user_info["phone_contacts"])
print()

# 10. Új ember hozzáadása 2 telefonszámmal
print("10. Új ember 2 telefonszámmal")
user_info["phone_contacts"]["Peter"] = ["+36301234567", "+36701234567"]
pprint(user_info["phone_contacts"])
print()

# Extra 1: Skills lista utolsó 3 eleme fordított sorrendben
print("Extra 1: Skills utolsó 3 eleme fordított sorrendben")
last_three_reversed = user_info["skills"][-3:][::-1]
print(f"Utolsó 3 elem fordítva: {last_three_reversed}")
print()

# Extra 2: Tim2 átnevezése Tim-re
print("Extra 2: Tim2 átnevezése Tim-re")
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
pprint(user_info["phone_contacts"])
print()