from pprint import pprint
# Data structure
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

# 1. adatbekérés
# --------------
languages = input("Adj meg 4 programozási nyelvet, vesszővel elválasztva! ")
lang_list = languages.split(",")
user_info['skills'] = lang_list

print(user_info)
print ("----------")

# 2. rendezés ABC szerint növekvő sorrendbe
# --------------
# print(user_info["favourite_meals"].sort()) -- Ezt próbáltam, de nem működött és nem értem, hogy miért?

user_info["favourite_meals"].sort() # Erről nem találtam az órai videóban utalást. Google segített.
print(user_info["favourite_meals"])

# 3. a lista utolsó előtti eleme
# --------------
print ("----------")
print(f"A teljes lista: {user_info["favourite_meals"]}")
print(f"A favorite_meals utolsó lista utolsó előtti eleme: {user_info["favourite_meals"][-2]}")

# 4. hozzáadunk egy kis spagettit :)      
# --------------
print ("----------")
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])

# 5. újabb elemek hozzáadása
# --------------
print ("----------")
add_to_list = user_info["favourite_meals"][2:4]
user_info["favourite_meals"].extend(add_to_list)

print(user_info["favourite_meals"])

# 6. duplázott elemek törlése
# --------------
print ("----------")
print(list(set(user_info["favourite_meals"])))

# 7. elemek felcserélése
# --------------
print ("----------")
first = user_info["favourite_meals"][0]
last = user_info["favourite_meals"][-1]

user_info["favourite_meals"][0] = last
user_info["favourite_meals"][-1] = first

print(user_info["favourite_meals"])


# 8. Új elem hozzáadása
# --------------
print ("----------")
user_info["phone_contacts"]["Attila"] = "+36209162401"

# 9. Elem törlése

del user_info["phone_contacts"]["Tim"]

# 10. Új kontakt, két telefonszámmal

user_info["phone_contacts"]["Peter"] = ["+36209162401","+36201234567"]


