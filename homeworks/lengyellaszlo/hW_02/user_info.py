"""
homework_2
"""

import pprint

user_info = { "name": "Mike", 
             "age": 25, 
             "favourite_meals": [ 
                 "pizza", "carbonara", "sushi" ],
             "phone_contacts": { 
                 "Mary": "+36701234567",
                   "Tim": "+36207654321", "Tim2":
                     "+36304567321", "Jim":
                       "+364005000" 
                } 
            }
user_info["skills"] = input("Enter 4 programming languages separated by commas (no spaces): ").split(",")
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"][-2])
user_info["favourite_meals"].append("spaghetti")
user_info["favourite_meals"] += [user_info["favourite_meals"][2], user_info["favourite_meals"][3]]
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
#print(user_info["favourite_meals"])
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
#print(user_info["favourite_meals"])
user_info["phone_contacts"]["Laszlo"] = "+36301234567"
del user_info["phone_contacts"]["Tim"]
user_info["phone_contacts"]["Balasz"] = ["+36301112222", "+36309998888"]
print(user_info["skills"][-3:][::-1])
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
del user_info["phone_contacts"]["Tim2"]
#pprint.pprint(user_info)
