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
    }
}

# programnyelv bekérése
Programnyelvek_lista=[]  
while 4!=len(Programnyelvek_lista):
    Programnyelvek=input("Adjál meg 4 programozási nyelvet vesszővel elválasztva szóköz nélkül:")
    Programnyelvek_lista=Programnyelvek.split(',')

user_info ['skills']=Programnyelvek_lista

#favorite meals
user_info["favourite_meals"].sort()

print(user_info["favourite_meals"][-2])

user_info["favourite_meals"].append("spaghetti")
harmadik=user_info["favourite_meals"][2]
negyedik=user_info["favourite_meals"][3]
user_info["favourite_meals"].append(harmadik)
user_info["favourite_meals"].append(negyedik)

# print(user_info["favourite_meals"])

user_info["favourite_meals"]=list(set(user_info["favourite_meals"]))

# print(user_info["favourite_meals"])

user_info["favourite_meals"][0],user_info["favourite_meals"][-1]=user_info["favourite_meals"][-1],user_info["favourite_meals"][0]

user_info["phone_contacts"]['Kati']="+36306820592"
#vagy update függvény user_info["phone_contacts"].update({'Kati':"+36306820592"})

user_info["phone_contacts"] ["Tim"]=None

# print(user_info["phone_contacts"])

#mivel nem egyértelmű, hogy csak a Tim telefonszámát kell kitörülni, vagy a Timet is, ezért 2 lépcsőben csinálom
del user_info["phone_contacts"] ["Tim"]

user_info["phone_contacts"].update({'Zoli':["+36301234567","+36306820595"]})


# print (user_info)

# extra feladat, gondolom nem ez az elegáns megoldása a feladatnak :-)
print(user_info ['skills'][-1], user_info ['skills'][-2],user_info ['skills'][-3])

