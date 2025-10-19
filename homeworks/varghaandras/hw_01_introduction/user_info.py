#  Base dictionary
 
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

# 1. Ask the user to enter 4 programming languages separated by commas (no spaces)
languages_input = input("Enter 4 programming languages separated by commas (no spaces): ")
skills_list = languages_input.split(",")
user_info["skills"] = skills_list

# 2. Sort the favourite_meals list in alphabetical order
user_info["favourite_meals"].sort()
print("Sorted favourite meals:", user_info["favourite_meals"])

# 3. Print the second-to-last item from the favourite_meals list
print("Second to last favourite meal:", user_info["favourite_meals"][-2])

# 4. Add "spaghetti" to the favourite_meals list
user_info["favourite_meals"].append("spaghetti")
print("Added spaghetti:", user_info["favourite_meals"])

# 5. Add the current third and fourth items (by value) again to the favourite_meals list
third_meal = user_info["favourite_meals"][2]
fourth_meal = user_info["favourite_meals"][3]
user_info["favourite_meals"].extend([third_meal, fourth_meal])
print("Duplicated 3rd and 4th meals:", user_info["favourite_meals"])

# 6. Remove duplicates from the favourite_meals list
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
print("Removed duplicates:", user_info["favourite_meals"])

# 7. Swap the first and last items in the favourite_meals list
meals = user_info["favourite_meals"]
user_info["favourite_meals"] = [meals[-1]] + meals[1:-1] + [meals[0]]
print("Swapped first and last:", meals)

# 8. Add a new contact with any name and phone number to phone_contacts
user_info["phone_contacts"]["Alex"] = "+36501239876"
print("Added new contact Alex:", user_info["phone_contacts"])

# 9. Remove "Tim" from phone_contacts (his number is no longer active)
del user_info["phone_contacts"]["Tim"]
print("Removed Tim:", user_info["phone_contacts"])

# 10. Add a new person to phone_contacts with two phone numbers
user_info["phone_contacts"]["Lara"] = ["+36701112222", "+36703334444"]
print("Added Lara with two numbers:", user_info["phone_contacts"])

