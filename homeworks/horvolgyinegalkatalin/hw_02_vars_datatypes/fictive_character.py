# fiktív alak létrehozása : név, életkor, pyton tapasztalat

# adatok bekérése
print("Add meg a neved:")
Person=input("")
Personnagybetüvel=Person.upper()
Personnagybetüvelszóköznélkül=Personnagybetüvel.strip()

print("Add meg az életkorod:")
Életkor=float(input(""))
Életkornapokban=int(Életkor)*365
print("Add meg a Pyton tapasztalatodat években:")
Tudásszint=float(input(""))

"""adatok formai ellenőrzése lépésenként, tartalmi ellenőrzést nem tartalmaz:
azaz nem ellenőrzöm hogy kitöltötte-e a nevet és ha igen betükkel-e, 
egész számot írt-e az életkorhoz és 
számot írt-e a szakmai tapasztalathoz
nem nagyobb-e a szakmai tapasztalata az életkoránál
szükség esetén kidolgozható
"""

# végeredmény tartalmi ellenőrzés nélkül

kiirandó=f"My character is {Életkornapokban} old. His/her name is {Personnagybetüvelszóköznélkül} and he/she has {Tudásszint} years experience."
print(kiirandó)
