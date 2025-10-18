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
#kerd be a 4 programozasi nyelvet es tarold el listaban
prog_lang = input("Please give 4 program languages: (e.g.: Python, Java, VB, C)").strip()
user_info["skills"] = prog_lang.split(",")
#print("1:")
#print(user_info)

#rendezd a favourite_meals ABC sorrendbe
#print("---------------------------------------")
#print("2.:")
user_info["favourite_meals"].sort()
#print(user_info)

#print("---------------------------------------")
#print("3.:")
#nyomtasd ki a favourite_meals utolso elotti elemet
print (user_info["favourite_meals"][-2])

#print("---------------------------------------")
#print("4.:")
#adj hozza egy spaghetti stringet
user_info["favourite_meals"].append("spaghetti")
#print(user_info)

#print("---------------------------------------")
#print("5.:")
#a favourite_meals plusz 3 es 4 eleme, nem index
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
#print(user_info)

#print("---------------------------------------")
#print("6.:")
#torold a duplikalt elemeket
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
#print(user_info)

#print("---------------------------------------")
#print("7.:")
#elso es utolso elem csere
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
#print(user_info)

#print("---------------------------------------")
#print("8.:")
#phone_cont hozzaad egy nev es telefonszam
user_info["phone_contacts"]["Sandor"] = "+36207770709"
#print(user_info)

#print("---------------------------------------")
#print("9.:")
#Tim telefonszam torol
del user_info["phone_contacts"]["Tim"]
#print(user_info)

#print("---------------------------------------")
#print("10.:")
#Olyan ember hozzaad akinek 2 szama van
user_info["phone_contacts"]["Bela"] = ["+36202221212", "+36302950202"]
#print(user_info)

#print("---------------------------------------")
#print("Extra1-2:")
# skills utolso 3 eleme,ellentétes sorrendben, majd Tim2-Tim-re
print(user_info["skills"][-1:-4:-1])

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
#print(user_info)