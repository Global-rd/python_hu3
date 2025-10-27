# Second b. Homework

#1.a. Input four program language names
program_languages = input ("Type four program language names (separated by , without space between the names) ")

#1.b.convert string to list
skill_list=program_languages.split(',')

#1.c. Ordered in Alphabet queue 
skill_list.sort(key=str.lower)
#print the ordered skill list for checking
for elem in skill_list:
    print("-",elem)

#1.d. extension dictionary with skills

user_info= {
    "name" : "Mike",
    "age" : 25,
    "favourite_meals" : [
        "pizza",
        "carbonara",
        "sushi"
    ],
    "phone_contacts" : {
    "Mary" : "+36701234567",
    "Tim" : "+36207654321",
    "Tim2" : "+36304567321",
    "Jim" : "+364005000"
    },
    "Skills" : skill_list
}

# 2. Favourite  Meals in alphabetical order
user_info["favourite_meals"].sort(key=str.lower)
#Checking with print
print(user_info["favourite_meals"])

# 3. Printing the last element of the favourite meals list
print(user_info["favourite_meals"][-1])

# 4. Add spaghetti to the favourite melas list
user_info["favourite_meals"].append("spaghetti")
#Check with Print the last element of the favourite meals list
print(user_info["favourite_meals"][-1])

# 5. Extend the meal list with third and fourth meals
"""third_element = user_info["favourite_meals"][2]
#fourth_element= user_info["favourite_meals"][3]
#user_info["favourite_meals"].append(third_element)
#user_info["favourite_meals"].append(fourth_element)"""

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

#check the extended list with print
print(user_info["favourite_meals"])

# 6. Clear the duplicated meals from the list
"""new_favourite_meals_list=[]
for x in user_info["favourite_meals"]:
    if x not in new_favourite_meals_list:
        new_favourite_meals_list.append(x)

user_info["favourite_meals"]=new_favourite_meals_list"""

user_info["favourite_meals"]=list(set(user_info["favourite_meals"]))

#Check 
print(user_info["favourite_meals"])

# 7. Change the first and the last elements in favourite_meal_list
user_info["favourite_meals"][0],user_info["favourite_meals"][-1]=user_info["favourite_meals"][-1],user_info["favourite_meals"][-0]
#Check 
print(user_info["favourite_meals"])

# 8. Extend the phone dictionary
user_info["phone_contacts"]["New_member"]="+36701234567"
#check
print(user_info["phone_contacts"])

# 9. Delete Tim from dictionary
del user_info["phone_contacts"]["Tim"]
print(user_info["phone_contacts"])

# 10.extend the phone dictionary with member who has two phone numbers
user_info["phone_contacts"]["Rich_member"]=["+491234321","+36701234567"]
#check
print(user_info["phone_contacts"])









