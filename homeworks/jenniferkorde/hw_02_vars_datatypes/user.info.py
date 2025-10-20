from pprint import pprint


user_info = {
"name": "Mike",
"age": 25,
"favourite_meals": ["pizza","carbonara","sushi"],
"phone_contacts": {"Mary": "+36701234567","Tim": "+36207654321","Tim2": "+36304567321","Jim": "+364005000"}}

pprint(user_info)

user_info["favourite_meals"].sort()
pprint(user_info["favourite_meals"])
pprint(user_info)
pprint(user_info["favourite_meals"][-2])
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info)
del user_info["favourite_meals"][-2]
print(user_info["favourite_meals"])
del user_info["favourite_meals"][-1]
print(user_info["favourite_meals"])
if len(user_info["favourite_meals"]) >=2:
       first =user_info["favourite_meals"][0]
       last= user_info["favourite_meals"][-1]
       user_info["favourite_meals"][0]= last
       user_info["favourite_meals"][-1]=first 
       
print(user_info["favourite_meals"])
user_info["phone_contacts"]["Thomas"] = "+36304496995"
print(user_info["phone_contacts"])
del user_info["phone_contacts"]["Tim"]
print(user_info)
user_info["phone_contacts"]["Laura"]=["+36205112724", "+36204456785"]
print(user_info["phone_contacts"]["Laura"])
print(user_info)
programming_languages= "Java,C++,Python,JavaScript"
skills=programming_languages.split(",")
user_info["skills"]=skills

print(user_info["skills"])
last_three=user_info["skills"][-3:]
last_three.reverse()
print(last_three)
user_info["phone_contacts"]["Tim"]=user_info["phone_contacts"]["Tim2"]
del user_info["phone_contacts"]["Tim2"]
print(user_info)









