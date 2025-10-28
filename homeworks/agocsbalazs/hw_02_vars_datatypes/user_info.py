import pprint

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

#lesz valami input bekéérés, vessző kötelező, szóközök nélkül...
input_programming_language = input("Enter 4 programming language with coma and wto whitespace: for example: Python,Java,C++,JavaScript: ")
print(input_programming_language.count(","))
#ha már lehet bele if else-t is írni ebben a háziban, akkor
if " " in input_programming_language.strip() or input_programming_language.count(",") != 3:
    print("Warning: Input format is incorrect please try again")
else:
        user_info["skills"] =input_programming_language.split(",")
        print("Input accepted")
        print(type(user_info["skills"]))


#ha még nincs if else lehetőség, akkor csak simán szét kell vágni a stringet és betenni a dict-be
#user_info["programming language"] =input_programming_language.split(",")
        
pprint.pprint(user_info)

#------------------------------
#további feladatok:

#2 sorba rendezés
print(sorted(user_info["favourite_meals"]))

#3. meals listából az utolsó előtti elem kiíratása
print(user_info["favourite_meals"][-2])  #carbonara

#4 spagetti hozzáadása a meals listához
user_info["favourite_meals"].append("spagetti")
print(user_info["favourite_meals"])

#5 második és harmadik elem újra hozzáadása
#user_info["favourite_meals"].append(user_info["favourite_meals"] [1:3]) #sushi és spagetti hozzáadása
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])


#6 duplikátumok eltávolítása
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])

#7 első és utolsó elem cseréje
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(user_info["favourite_meals"])

#8 új elem a telefonkönyvhöz
user_info["phone_contacts"]["Peter"] = "+3670845115"

#9 Tim telefonszám törlése
del user_info["phone_contacts"]["Tim"]
pprint.pprint(user_info)

#10 új személy 2 telefonszámmal
user_info["phone_contacts"]["Józsika"] = ["+3620458628, +3630991458"]
pprint.pprint(user_info)

#11 print "skills" fordított sorrendben hátulról
print(user_info["skills"][-1:-4:-1])

#12 Tim2 csere Tim1-re
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
pprint.pprint(user_info)