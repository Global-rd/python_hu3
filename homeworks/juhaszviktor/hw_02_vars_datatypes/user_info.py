import pprint

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

dev_lang = input("Írj 4 programozási nyelvet vesszővel elválasztva: ")
dev_lang_list = dev_lang.split(",")
# Szóközök eltávolítása az elemek elejéről
dev_lang_list = [lang.strip() for lang in dev_lang_list]
#print(dev_lang_list)

#pprint.pprint(user_info)
user_info["skills"] = dev_lang_list
#pprint.pprint(user_info)

#print(user_info["favourite_meals"][-2])
user_info["favourite_meals"].append("spaghetti")
#pprint.pprint(user_info)

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
#pprint.pprint(user_info)

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
#pprint.pprint(user_info)

#első és utolsó felcserélése
meals = user_info["favourite_meals"]
meals[0], meals[-1] = meals[-1], meals[0]
#pprint.pprint(user_info)

user_info["phone_contacts"]["Viktor"]="+36204498843"

del user_info["phone_contacts"]["Tim2"]

user_info["phone_contacts"]["Új emner"]=["+36201234567","+36301234567"]
pprint.pprint(user_info)
