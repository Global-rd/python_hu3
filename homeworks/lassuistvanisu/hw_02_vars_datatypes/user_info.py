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

print("Feladat 1.")
#ADATBEKÉRŐ
get_skills = input("Give me three programming language, separate by a coma: ")

#LISTÁBA TESZ
"""skills_list = get_skills.split(",")
user_info["skills"] = get_skills.split(",")
"""
#LÉTREHOZ EGY SKILLS KULCSOT ÉS HOZZÁADJA A BEKÉRT ADATOKAT LISTÁBA
user_info["skills"] = get_skills.split(",")
print(user_info["skills"])

print("Feladat 2.")
#"favourite_meals" LISTA ABC NÖVEKVŐBE RENDEZÉS
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"]) 

print("Feladat 3.")
#KIPRINTELNI A "favourite_meals" UTOLSÓ ELEMÉT
penultimate_meal = user_info["favourite_meals"][-2]
print(f"Utolsó előtti elem: {penultimate_meal}")


print("Feladat 4.")
#SPAGETTI HOZZÁADÁSA A KEDVENC KAJÁKHOZ
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"][-1:])

print("Feladat 5.")
#3. és 4. ELEMEK ISMÉTELT HOZZÁADÁS
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

"""third = user_info["favourite_meals"][2]
fourth = user_info["favourite_meals"][3]
user_info["favourite_meals"].extend([third, fourth])
"""
print(user_info["favourite_meals"])

print("Feladat 6.")
#DUPLIKÁTUM TÖRLÉSE
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
print(user_info["favourite_meals"])

print("Feladat 7.")
#ELSŐ ÉS UTOLSÓ ELEM FELCSERÉLÉS A KAJÁBAN
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = (
    user_info["favourite_meals"][-1],
    user_info["favourite_meals"][0]
)
print(user_info["favourite_meals"])

print("Feladat 8.")
#ÚJ KONTAKT
user_info["phone_contacts"]["Kate"] = "+36301234567"
print(user_info["phone_contacts"])

print("Feladat 9.")
#TIM'TÖRLÉSE AZ INAKTÍV SZÁMMAL
del user_info["phone_contacts"]["Tim"]
print(user_info["phone_contacts"])

print("Feladat 10.")
#ÚJ EMBER HOZZÁADÁS AHOL A SZÁMOK LISTÁBAN VANNAK
user_info["phone_contacts"]["Alex"] = ["+36701112222", "+36703334455"]
print(user_info["phone_contacts"])


#EXTRA FELADATOK
#SKILLS LISTA UTOLSÓ 3 ELEMÉNEK KIÍRÁSA FORDÍTOTT SORRENDBEN
skills_reverse = user_info["skills"][-3:][::-1]
print(f"Skills utolsó 3 eleme fordított sorrendben:{skills_reverse}" )

#"TIM 2" ÁTNEVEZÉSE "TIM"
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

