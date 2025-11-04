# feladat: város és bérleti díj bekérése
# ha város=Chicago akkor költözik
# ha a város =Washington akkor nem költözik
# ha a város = New York vagy San Francisco és a bérleti díj max 4000 akkor költözik
# ha a város bérmi más és a bérletidíj kisebbegyenlő mint 3000 akkor költözik
# if-elif-else, operátorok

city=input("Kérem adjon meg egy város nevét:").upper()
rent=float(input("adja meg a bérleti díjat:"))

if city==("CHICAGO"):
    print("költözik")
elif city==("WASHINGTON"):
    print("nem költözik")
elif city in ("NEW YORK" , "SAN FRANCISCO") and (rent<=4000):
    print("költözik")
elif rent<=(3000):
    print("költözik")
else : 
    print("nem költözik")
