city = input("Melyik városban vennél ki albérletet? ")
rent = int(input("Mennyibe kerül a lakbér? "))

if city == "Chicago":
    ok = True
elif city == "Washington":
    ok = False
elif city in ["New York","San Fransisco"] and rent < 4000:
    ok=  True
elif rent < 3000:
    ok = True
else:
    ok = False

if ok:
    print(f"Be tudsz költözni {city} városába {rent} USD-ért!")
else:
    print(f"Nem tudsz beköltözni {city} városába {rent} USD-ért!")


