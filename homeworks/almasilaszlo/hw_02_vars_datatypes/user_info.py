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
#print(user_info)
#1. Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül. Konvertáld a kapott stringet egy listává, és add hozzá a fenti dictionary-hez “skills” néven.
dev_lan = input("Provde me 4 different programmaing languages seperated by a comma: ")
dev_lan = dev_lan.split(",")
#print(dev_lan)
#print(type(dev_lan))
user_info["skills"]=dev_lan

#2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
user_info["favourite_meals"].sort()

#3. Printeld ki a favourite_meals lista utolsó előtti elemét
print(user_info["favourite_meals"][-2])

#4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
user_info["favourite_meals"].append("spaghetti")

#5.Add hozzá a favourite_meals-hez az aktuális favourite_meals lista harmadik és negyedik elemét (nem az index-ét) újra.
food_to_add= user_info["favourite_meals"][2:4]
user_info["favourite_meals"].extend(food_to_add)
#print(user_info)

#6. Ezután töröld az így keletkezett duplikátumokat!
user_info["favourite_meals"]=list(set(user_info["favourite_meals"]))
#print(user_info)

#7.
user_info["favourite_meals"][0],user_info["favourite_meals"][-1]=user_info["favourite_meals"][-1],user_info["favourite_meals"][0]
#print(user_info)

#8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.
user_info["phone_contacts"]["Belaba: "]="+3690666666"

#9.Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!
del user_info["phone_contacts"]["Tim"]

#10. Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!
user_info["phone_contacts"]["Donald: "]=["+3690666666", "+36907777777"]
print(user_info)

#EXTRA 1.
""" KÉRDÉS: Ez "Nonetype-ot eredményez, de pontosan miért?? Lehet átsiklottam fölötte, de azt hittem így működik, de e miatt meg sem tudja fordítani."
print(user_info["skills"][-3:].sort(reverse=True))
print(type(user_info["skills"][-3:]))
Másik megoldás alább:
"""
print(user_info["skills"][-3:][::-1])

#EXTRA 2. Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print(user_info)