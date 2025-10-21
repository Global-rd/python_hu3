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

skills = input("Addj meg négy programozási nyelvet, vesszóvel válaszd el őket egymástól: ").strip()     # információ bekérése.
list_of_skills = list(skills.split(","))                                                                # lista készítése vesszó mentén.
user_info["skills"] = list_of_skills                                                                    # a lista beépítése a user_info-ba skills kulcs alá.

user_info["favourite_meals"].sort()                                         # A avourite_meals lista abc rendezése.

user_info["favourite_meals"].append("spaghetti")                            # A avourite_meals lista bővítése spaghetti-vel.

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])      # A favourite_meals lista utolsó két elemének másolása.

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))      # A favourite_meals lista duplikációinak megszűntetése.

""" Első megoldás:
first_food = user_info["favourite_meals"][0]                                # Az első elem a listából változóba másolva.
last_food = user_info["favourite_meals"][-1]                                # Az utolsó elem a listából változóba mentve.
user_info["favourite_meals"][0] = last_food                                 # Az utolsó elem az első helyre másolva.
user_info["favourite_meals"][-1] = first_food                               # Az első elem az utolsó helyre másolva.
"""

# Javasolt, jobb megoldás:
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = (
    user_info["favourite_meals"][-1],
    user_info["favourite_meals"][0],
)

user_info["phone_contacts"]["Jony"] = "+3672555776"                         # A telefonlista bővítve Jony-val.

del user_info["phone_contacts"]["Tim"]                                      # Tim kulcs és a hozzá tartozó érték törlése.

user_info["phone_contacts"]["Koni"] = ["+3680555555", "+3620777555"]        # Koni hozzáadva két tel számmal, ezek listában, hogy lehessen visszakeresni.

""" Első megoldás:
print(sorted(user_info["skills"][-3:], reverse=True))                       # A skills lista utolsó három elemét fordítva kiírja. ( ezt már nyomozni kellett...)
"""

# Javaslot, jobb megoldás: 
print(user_info["skills"][-3:][::-1])
# itt az [-3:] egy kiválasztás, a [::-1] pedig az egyesével való visszafelé való "lépkedés".

""" Első megoldás:
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]    # Lemásolom Tim2-őt Tim-néven.
del user_info["phone_contacts"]["Tim2"]                                     #Törlöm Tim2-őt. ( csórókám :) )
"""

# Javasolt, jobb megoldás:
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

pprint(user_info)