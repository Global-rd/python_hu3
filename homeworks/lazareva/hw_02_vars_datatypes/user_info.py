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
        "Mary": "36701234567",
        "Tim": "+36207654321",
        "Tim2": "+39304567321",
        "Jim": "+364005000"
    }
}

#1. 4 programozási nyelv hozzáadása a user_info dictionary-hez egy "skills" kulcs alatt
skills_in = input("Give me four programming languages separated by a comma: ")

print(skills_in)
print(type(skills_in))

user_info["skills"] = skills_in.split(",") #programozási nyelvek listává alakítása

pprint(user_info) #formázott kiírás

#2. Kedvenc ételek abc sorrendben
pprint(sorted(user_info["favourite_meals"]))

#3. Kedvenc ételek utolsó előtti elem kiíratása
print(user_info["favourite_meals"][-2])

#4. "spagetti" hozzáadása a kedvenc ételekhez
user_info["favourite_meals"].append("spagetti")

pprint(user_info)

#5. Kedvenc ételekhez hozzáadom a lista 3. és 4. elemét
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

print(user_info["favourite_meals"])

#6. Kedvenc ételeknél duplikáció törlése
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

print(user_info["favourite_meals"])

#7. Kedvenc ételeknél az első és az utolsó elem cseréje

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

print(user_info["favourite_meals"])

#8. Telefonkönyvbe új elem
user_info["phone_contacts"]["Edina"] = "+36123456789"

#9. Telefonkönyvből elem törlése (Tim)
del user_info["phone_contacts"]["Tim"]

#10. Telefonkönyvhöz új elem, ahol két telefonszám is van
user_info["phone_contacts"]["Angi"] = ["+36201234567", "+36301234567"]

pprint(user_info["phone_contacts"])

# teljes user_info kiírása
pprint(user_info)

#szorgalmi
#skills utolsó 3 eleme ellentétes sorrendben
print(user_info["skills"][-1:-4:-1])

#Tim2 átnevezése Tim-re a telefonkönyvben
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

pprint(user_info["phone_contacts"])
