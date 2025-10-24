#adatbekérés
city= input("Kérem adja meg melyik városban van a kiadó lakás: ").title().strip()
price= int(input("Kérem adja meg a havi bérleti díjjat dollárban: "))

"""Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban
kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD
havonta.
 Gyűlöli Washington-t, és semmi pénzért nem lakna ott
Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit
megadna azért hogy ott lakhasson
Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér
ellenében költözne oda."""

if city == "Washington":
    print ("Sajnáljuk, nem érdekel az ajánlat")
elif city == "Chicago":
    print ("Az ajánlatát elfogadjuk")
elif city== "New York" or "San Fransisco":
    if price <= 4000:
        print ("Az ajánlatát elfogadjuk")
    else:
        print ("Sajnáljuk, nem érdekel az ajánlat")
elif price <= 3000:
    print ("Az ajánlatát elfogadjuk")
else: print ("Sajnáljuk, nem érdekel az ajánlat")



