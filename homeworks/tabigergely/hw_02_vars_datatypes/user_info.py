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


#1. feladat
language = input("Adj meg 4 programozási nyelvet vesszővel elválasztva!")
user_info["skills"] = language.split(",")

print(user_info)
print("-------")

#2. feladat
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])
print("---------")

#3. feladat

print(user_info["favourite_meals"][-2])
print("---------")

#4. feladat

user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])
print("--------")

#5. feladat

add_to_list = user_info["favourite_meals"][2:4]
user_info["favourite_meals"].extend(add_to_list)

print(user_info["favourite_meals"])
print("---------")

#6. feladat

print(list(set(user_info["favourite_meals"])))
print("--------")

#7. feladat

user_info["favourite_meals"][0] , user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1] , user_info["favourite_meals"][0]
print(user_info["favourite_meals"])
print("----------")

#8. feladat

user_info["phone_contacts"]["Geri"] = "+36301234567"
print(user_info["phone_contacts"])
print("----------")

#9. feladat

user_info["phone_contacts"].pop("Tim")
print(user_info["phone_contacts"])
print("----------")

#10. feladat

user_info["phone_contacts"]["Laci"] = "+36301231231" , "+36304567456"
print(user_info["phone_contacts"])
print("----------")

#Extra 1

print(user_info["skills"][::-1][:3])
print(user_info["skills"])
print("----------")

#Extra 2

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print(user_info["phone_contacts"])
print("----------")