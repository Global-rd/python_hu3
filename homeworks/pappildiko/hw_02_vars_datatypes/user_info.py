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


'''1. Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül. 
Konvertáld a kapott stringet egy listává, és add hozzá a fenti dictionary-hez “skills” néven.'''
prog_languages = input("Give me 4 programming languages separated by a comma, without spaces: ")
# spaces are cut off only at the beginning of the first word and at the end of the last word
prog_languages_list = prog_languages.strip().split(",") 
user_info["skills"]= prog_languages_list


'''2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.'''
sorted(user_info["favourite_meals"])


'''3. Printeld ki a favourite_meals lista utolsó előtti elemét'''
print(user_info["favourite_meals"])
print(user_info["favourite_meals"][-2])



'''4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.'''
user_info["favourite_meals"].append("spaghetti")


'''5. Add hozzá a favourite_meals-hez az aktuális favourite_meals lista harmadik és negyedik elemét (nem az index-ét) újra.'''
user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])


'''6. Ezután töröld az így keletkezett duplikátumokat!'''
user_info["favourite_meals"].remove("sushi")
user_info["favourite_meals"].remove("spaghetti")


'''7. Cseréld fel a favourite_meals lista első és utolsó elemét!'''
user_info["favourite_meals"][0],user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1],user_info["favourite_meals"][0]


'''8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.'''
user_info["phone_contacts"]["Vera"] = "+36544444444"


'''9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. 
Töröld ki a telefonkönyvből!'''
del user_info["phone_contacts"]["Tim"]


'''10. Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!'''
user_info["phone_contacts"]["Aron"] = "+3654443333"
user_info["phone_contacts"]["Aron2"] = "+3654442222"


'''Extra 1: Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!''' 
print(user_info["skills"])
reversed_skills = sorted(user_info["skills"], reverse=True)
print(reversed_skills[:3])


'''Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!'''
user_info["phone_contacts"]['Tim'] = user_info["phone_contacts"]['Tim2']
del user_info["phone_contacts"]['Tim2']
