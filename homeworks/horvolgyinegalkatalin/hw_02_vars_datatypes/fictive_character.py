# fiktív alak létrehozása : név, életkor, pyton tapasztalat

# adatok bekérése
print("Add meg a neved:")
Person=input("")
Personnagybetüvel=Person.upper()
Personnagybetüvelszóköznélkül=Personnagybetüvel.strip()

print("Add meg az életkorod:")
Életkor=int(input(""))
Életkornapokban=Életkor*365
print("Add meg a Pyton tapasztalatodat években:?")
Tudásszint=float(input(""))

"""adatok formai ellenőrzése lépésenként, tartalmi ellenőrzést nem tartalmaz:
azaz nem ellenőrzöm hogy kitöltötte-e a nevet és ha igen betükkel-e, 
számot írt-e az életkorhoz és 
számot írt-e a szakmai tapasztalathoz
nem nagyobb-e a szakmai tapasztalata az életkoránál
szükség esetén kidolgozható
"""
#csak az ellenőrzéshez jó az alábbi 6 print tasítás, élesben kitörülhető
print(Person)
print(Personnagybetüvel)
print(Personnagybetüvelszóköznélkül)
print(Életkor)
print(Életkornapokban)
print (Tudásszint)

# végeredmény tartalmi ellenőrzés nélkül
print(Personnagybetüvelszóköznélkül,"vagyok",Életkornapokban,"napos vagyok",Tudásszint,"éves Pyton tapasztalattal")