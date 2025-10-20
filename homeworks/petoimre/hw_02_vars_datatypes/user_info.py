
from pprint import pprint

user_info = {
"name"           : "Mike",
"age"            : 25,
"favourite_meals": ["pizza","carbonara","sushi"],
"phone_contacts" : {"Mary": "+36701234567",
                     "Tim": "+36207654321",
                    "Tim2": "+36304567321",
                     "Jim": "+364005000"}
}

user_input =  input("Type in four prgraming language. Use comma to separate them: ")  # Bekéri a szavakat
user_input = user_input.split(",")                                                   # list lesz belőle
# print(type(user_input))                                                            # check
# print(user_input)                                                                  # chk
user_info ["skills"] = user_input                                                    # hozzáteszi a list-et dict-hez
# print(user_info)                                                                   # chk
user_info["favourite_meals"] = sorted(user_info["favourite_meals"])                  # abc sorrenbe teszi
# print(user_info)                                                                   # chk 
print(user_info["favourite_meals"][-2:-1])                                           # print az utólsó előtti elemet
user_info["favourite_meals"].append("spaghetti")                                     # hozzáadja a 'spagetti'-t
# print(user_info)                                                                   # chk
user_info["favourite_meals"] = sorted(user_info["favourite_meals"])                  # legyen újra abc-ben
# print(user_info)                                                                   # chk
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])               # hozzáteszi a saját harmadik és negyedik elemét
# print(user_info)                                                                   # chk
favourite_meals_set = set(user_info["favourite_meals"])                              # set-ként betéve a változóba
# print(favourite_meals_set)                                                         # chk eltűnt a duplikáció
user_info["favourite_meals"] = list(favourite_meals_set)                             # list-ként visszatéve a dict-be
# print(user_info)                                                                   # chk
user_info["favourite_meals"] = sorted(user_info["favourite_meals"])                  # legyen újra abc-ben
# print(user_info)                                                                   # chk
favourite_meals_first = user_info["favourite_meals"].pop(0)                          # kitesszük és töröljük az első elemet
favourite_meals_last = user_info["favourite_meals"].pop(-1)                          # kitesszük és töröljük az utólsó elemet
# print(favourite_meals_first)                                                       # chk
# print(favourite_meals_last)                                                        # chk
user_info["favourite_meals"].insert(0, favourite_meals_last)                         # utólsó megy előre
user_info["favourite_meals"].append(favourite_meals_first)                           # első megy a végére
# print(user_info)                                                                   # chk
user_info["phone_contacts"]["Ivy"] = +36303033785                                    # hozzámegy egy új kulcs-érték pár
# print(user_info)                                                                   # chk
del(user_info["phone_contacts"]["Tim"])                                              # töröljük Tim-et
#print(user_info)                                                                    # chk
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")         # átnevezzűk Tim2-t Tim-re
# print(user_info)                                                                   # chk Tim rendezve
user_info["phone_contacts"]["DoubleJoe"] = [+36301234567, +36201234567]              # új, két tel számos embert hozzáad
# print(user_info)                                                                   # chk
print(user_info["skills"][::-1][:3])                                                 # skills utólsó 3 eleme visszafelé
# end
