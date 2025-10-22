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

# 1. Get program laguages and add it to user_info dictionary
#user_info["skills"]=['C','C++','C#','Python']
user_info.update({"skills": input("Adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül: ").split(",")})

# 2. Sort favourite_meals 
user_info["favourite_meals"].sort()

# 3. Print meal
print(user_info["favourite_meals"][-2])

# 4. Add meal
user_info["favourite_meals"].append("spaghetti")

# 5. Add 2-3 items
#user_info["favourite_meals"].append(user_info["favourite_meals"][2])
#user_info["favourite_meals"].append(user_info["favourite_meals"][3])
user_info["favourite_meals"].extend(user_info["favourite_meals"].range[2:4])

# 6. Remove duplicated
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# 7. Change first and last items
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

# 8. Add new contact
user_info["phone_contacts"]["Joe"]= "+36203245678"

# 9. Remove Tim
del user_info["phone_contacts"]["Tim"]

# 10 Add contact with two numbers
user_info["phone_contacts"]["Bill"]= ["+36202456789","+36204567890"]

# Extra 1 print last 3 skills reverse
print((user_info["skills"][:-4:-1]))

# Extra 2 rename Tim2
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")