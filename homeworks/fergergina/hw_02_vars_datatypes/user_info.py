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

# lesson 1

languages = input("Give me four programming languages separated by comma and without spaces: ")
languages = languages.split(",")
user_info["skills"] = languages

# lesson 2

user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])

# lesson 3 

print(user_info["favourite_meals"][-2])

# lesson 4

user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])

# lesson 5 

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])

# lesson 6 

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])

# lesson 7 

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(user_info["favourite_meals"])

# lesson 8 

user_info["phone_contacts"]["Gina"] = "+36703844215"
print(user_info["phone_contacts"])

# lesson 9

user_info["phone_contacts"].pop("Tim") 
print(user_info["phone_contacts"])

# lesson 10

user_info["phone_contacts"]["Kiki"] = ["+36703829874", "+36703824738"]
print(user_info["phone_contacts"])
