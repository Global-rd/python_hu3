user_info = {
    "name": "Mike",
    "age": 25,
    "favorite_meals": [
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
# 1. Bekérek 4 programizási nyelvet
languages = input("Adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül: ")
# Szöveg listává alakítom
skills_list = languages.split(",")
# Hozzáadom a dictionary-hez
user_info["skills"] = skills_list
# 2. A favourite_meals elemeit ABC sorrendbe rendezem
user_info["favorite_meals"].sort()
# 3. Printelem az utolsó előtti ételt
print("Utolsó előtti kedvenc étel:", user_info["favorite_meals"][-2])
# 4. Hozzáadom a spagettit a listához
user_info["favorite_meals"].append("spaghetti")
# 5. A favourite_meals-hez hozzáadom az aktuális favourite_meals lista harmadik és negyedik elemét
user_info["favorite_meals"].extend(user_info["favorite_meals"][2:4])
# 6. Törlöm a duplikációt
user_info["favorite_meals"] = list(set(user_info["favorite_meals"]))
# 7. Felcserélem az első, és az utolsó elemet
meals = user_info["favorite_meals"]
meals[0], meals[-1] = meals[-1], meals[0]
user_info["favorite_meals"] = meals
# 8. A “phone_contacts” dictionary-hez hozzáadok egy új elemet, Alexet
user_info["phone_contacts"]["Alex"] = "+36709998877"
# 9. Kitörlöm a "Tim" key mögött lévő telefonszámot, mert már nem él.
del user_info["phone_contacts"]["Tim"]
#10. Hozzáadok egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van
user_info["phone_contacts"]["Ricsi"] = ["+36701478525", "+36202255887"]