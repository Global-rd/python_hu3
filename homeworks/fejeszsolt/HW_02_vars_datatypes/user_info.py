from pprint import pprint

# alapadatok

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
# 1. feladat
# adatbekérés
skills_bekérés = str(input("Adj meg 4 programozási nyelvet vesszővel elválasztva: "))
#lista
skills= skills_bekérés.split(",")
#hozzáadás
user_info["skills"] = skills
pprint(user_info)

#2. feladat

print ("------------------------------------------")

user_info["favourite_meals"].sort()

print (user_info)

#3. feladat

print ("------------------------------------------")

print(user_info["favourite_meals"][-2])

#4. feladat

print ("------------------------------------------")

user_info["favourite_meals"].append("spaghetti")

pprint (user_info)

# 5. feladat

print ("------------------------------------------")
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
pprint(user_info)

#6. feladat
print ("------------------------------------------")
set_user_info = set(user_info["favourite_meals"])
user_info["favourite_meals"]= list(set_user_info)
print (user_info["favourite_meals"])

#7. feladat
print ("------------------------------------------")
első=user_info["favourite_meals"].pop(0)
utolsó=user_info["favourite_meals"].pop(-1)

print (user_info["favourite_meals"])

user_info["favourite_meals"].insert(0, utolsó)
user_info["favourite_meals"].insert(-1, első)

print (user_info["favourite_meals"])

#8. feladat
print ("------------------------------------------")
user_info["phone_contacts"]["Béla"]="+36801234567"

pprint(user_info["phone_contacts"])

#9. feladat
print ("------------------------------------------")
del user_info["phone_contacts"]["Tim"]

pprint(user_info["phone_contacts"])

#10. feladat
print ("------------------------------------------")
user_info["phone_contacts"]["Géza"]=["+36811234567","+36909999999"]
pprint(user_info["phone_contacts"])

# +1
print ("------------------------------------------")
print (user_info["skills"][-3:][::-1])

#+2
print ("------------------------------------------")

user_info["phone_contacts"]["Tim"]= user_info["phone_contacts"].pop("Tim2")
pprint (user_info["phone_contacts"])
