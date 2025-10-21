user_info = {
"name": "Mike",
"age": 25,
"favourite_meals": ["pizza","carbonara","sushi"],
"phone_contacts": {"Mary": "+36701234567",
"Tim": "+36207654321",
"Tim2": "+36304567321",
"Jim": "+364005000"}
}

#print(user_info)

# 1. feladat 
prog_language = input("Kérek 4 programozási nyelvet vesszővel elválasztva!")
user_info["skills"] = prog_language.split(",") # Hozzáadom a megadott listát

# 2. feladat
user_info["favourite_meals"].sort() # Rendezem az adatokat

# 3. feladat
print(user_info["favourite_meals"][-1]) # Listázom a lista utolsó elemét

# 4. feladat
user_info["favourite_meals"].append("spaghetti") # Hozzáadom a "Spaghetti"-t
#print(user_info["favourite_meals"])

# 5. feladat
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4]) # Hozzáadom egy lista 3., 4. elemét értékként
#print(user_info["favourite_meals"])

# 6. feladat
user_info["favourite_meals"]=list(set(user_info["favourite_meals"])) # Törlöm a duplikációkat és visszaalakítom listává
#print(user_info["favourite_meals"])

# 7. feladat
user_info["favourite_meals"].sort() # Rendezem a listát újra
"""
first = user_info["favourite_meals"][0] # Eltárolom a jelenlegi első elemet
last = user_info["favourite_meals"][-1] # Eltárolom a jelenlegi utolsó elemet
user_info["favourite_meals"][0]=last # Első elemnek megadom az eltárolt utolsó elemet
user_info["favourite_meals"][-1]=first # Utolsó elemnek megadom az eltárolt első elemet
"""
user_info["favourite_meals"][0],user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1],user_info["favourite_meals"][0]
#print(user_info["favourite_meals"])

# 8. feladat
user_info["phone_contacts"].update({"Jack":"+36301122334"}) # Hozzáadom "Jack"-et és telefonszámát
#print(user_info["phone_contacts"])

# 9. feladat
user_info["phone_contacts"].pop("Tim") # Törlöm "Tim"-et
#print(user_info["phone_contacts"])

# 10. feladat
user_info["phone_contacts"].update({"Lara":["+36203334444","+36305556666"]}) # Hozzáadom "Lara"-t és az ő 2 telefonszámát
print(user_info)
