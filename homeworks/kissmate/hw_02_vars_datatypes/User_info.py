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
#1.feldata
language = input("Give me 4 programing language separated with commas and without spaces")
user_info["skills"] = language
print(language)
#2 feladat
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])
#3.feladat
favourite_meals = user_info.get("favourite_meals")
print(favourite_meals[-2])
#4.feladat
favourite_meals.append("spaghetti")
print(favourite_meals)
#5.feladat
favourite_meals.append(favourite_meals[2])
favourite_meals.append(favourite_meals[3])
print(favourite_meals)
#6.feladat
favourite_meals = list(set(favourite_meals))
#7.feladat
favourite_meals[0], favourite_meals[-1] = favourite_meals[-1], favourite_meals[0]
print(favourite_meals)
#8.feladat
("John", "+36301234567")
#9.feladat
user_info["phone_contacts"].pop("Tim")
print(user_info["phone_contacts"])
#10.feladat
user_info["phone_contacts"].append("Jimmy":"+364005001","3670364004")
print(user_info["phone_contacts"])