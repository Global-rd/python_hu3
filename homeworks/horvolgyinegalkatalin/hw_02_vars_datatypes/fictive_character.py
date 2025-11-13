# fiktív alak létrehozása : név, életkor, pyton tapasztalat

# adatok bekérése

person=input("Add meg a neved:")
person_upperkays_onespace=person.strip().upper()

age=input("Add meg az életkorod:")
age_in_days=int(age)*365
skill_level=float(input("Add meg a Pyton tapasztalatodat években:"))

"""adatok formai ellenőrzése lépésenként, tartalmi ellenőrzést nem tartalmaz:
azaz nem ellenőrzöm hogy kitöltötte-e a nevet és ha igen betükkel-e, 
egész számot írt-e az életkorhoz és 
számot írt-e a szakmai tapasztalathoz
nem nagyobb-e a szakmai tapasztalata az életkoránál
szükség esetén kidolgozható
"""

# végeredmény tartalmi ellenőrzés nélkül

output_msg=f"My character is {age_in_days} old. His/her name is {person_upperkays_onespace} and he/she has {skill_level} years experience."
print(output_msg)
