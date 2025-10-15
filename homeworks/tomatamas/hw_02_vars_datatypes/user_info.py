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

# programmozási nyelvek bekérése
prog_languages = input("Name four programming languages separated with comma: ").split(",")
for i in range(len(prog_languages)):
    prog_languages[i] = prog_languages[i].strip()
user_info["skills"] = prog_languages

# favorite meals rendezése
user_info["favourite_meals"].sort()

# favorite meals lista utolsó előtti elem printelése
print(f"Favorite meals lista utolsó előtti eleme: {user_info['favourite_meals'][-2]}")

# spaghetti hozzáadása favorite meals list-hez
user_info["favourite_meals"].append("spaghetti")

# favorite meals lista 3. és 4. elemeinek hozzáadása
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# favorite meals duplikátumok tisztítása (és rendezése)
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
user_info["favourite_meals"].sort()

# favorite meals első és utolsó elem felcserélése
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

# új phone contact hozzáadása
user_info["phone_contacts"]["Jamie"] = "+36308899658"

# Tim kontakt törlése
user_info["phone_contacts"].pop("Tim")

# Új kontakt hozzáadása több telefonszámmal
user_info["phone_contacts"]["Bob"] = ["+36308826698","+36205996585"]

# skills lista utolsó 3 elemének kiíratása ellentétes sorrendben
print(f"Skills lista utolsó 3 eleme fordított sorrendben: {user_info['skills'][-1:-4:-1]}")

# Tim2 átnevezése Tim-re
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

#print(user_info)
