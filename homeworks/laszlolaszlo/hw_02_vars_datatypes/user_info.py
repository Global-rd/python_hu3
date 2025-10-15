from pprint import pprint

user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": ["pizza", "carbonara", "sushi"],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000",
    },
}

# Task 2/1
# I ask 4 programming language as string separated with commas
user_skills = input("Please add 4 programming languages, separated by commas: ")

# With str.split() I get back a list data type from string
user_skills_list = user_skills.split(",")

# With dict.update() method I update the existing user_info dict type variable
user_info.update({"skills": user_skills_list})

# I use pretty print
pprint(user_info)

# Task 2/2
# Order favourite_meals values into alphabetic order
print("------------------")
favourite_meals = user_info.get("favourite_meals")
favourite_meals.sort()  # .sort() modify original list (in-place), not return new object!
print(favourite_meals)

# sorted() returns a new list object
# sorted_favourite_meals = sorted(favourite_meals)
# print(id(favourite_meals))
# print(id(sorted_favourite_meals))

# Task 2/3

# print favourite_meals last before item
print("------------------")
print(favourite_meals[-2])

# Task 2/4
# Add spaghetti to the actual list
print("------------------")
favourite_meals.append("spaghetti")
print(favourite_meals)

# Task 2/5
# Add the actual list 3rd and 4th items to the actual list
print("------------------")
favourite_meals.append(favourite_meals[2])
favourite_meals.append(favourite_meals[3])
print(favourite_meals)

# Task 2/6
# Dedup the list with set(), set items has to be unique
print("------------------")
favourite_meals = list(set(favourite_meals))
print(favourite_meals)

# Task 2/7
# Change favourite_meals list first item with the last item
print("------------------")
print(favourite_meals)
favourite_meals[0], favourite_meals[-1] = favourite_meals[-1], favourite_meals[0]
print(favourite_meals)

# Task 2/8
# Add a new record to phone_contacts
print("------------------")
user_info["phone_contacts"]["Laszlo"] = "+36301234567"
pprint(user_info)

# Task 2/9
# Remove Tim from phone_contacts
print("------------------")
user_info["phone_contacts"].pop("Tim")
pprint(user_info)

# Task 2/10
# Add a new person with multiple phone numbers
print("------------------")
user_info["phone_contacts"]["Peter"] = ["+36701234567", "+36401234567"]
pprint(user_info)

# Task 2 / Extra1
# Print skills list last three element in reverse order
print("------------------")
pprint(user_info["skills"])
skills_reversed = user_info["skills"][-3:]
skills_reversed.reverse()
print(skills_reversed)

# Task 2 / Extra2
# Rename Tim2 to Tim while keep phone number
removed_value = user_info["phone_contacts"].pop("Tim2")
print(removed_value)
user_info["phone_contacts"].update({"Tim": removed_value})
print(user_info)

"""
More compact solution but less readability
user_info['phone_contacts']['Tim'] = user_info['phone_contacts'].pop('Tim2')
"""
