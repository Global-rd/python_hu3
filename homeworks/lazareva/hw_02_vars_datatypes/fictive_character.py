"""
Fiktív karaktert hoz létre dictionary-vel

A felhasználótól bekérjük a nevét, életkorát és a Python tapasztalatát években.

Két módon tároljuk az adatokat:
- a "fictive_character" dictionary-t a kód elején hozzuk létre, majd feltöltjük a kapott adatok alapján,
- a "fictive_character2" dictionary-t egy lépésben hozzuk létre a bemeneti adatokkal

A kiírásnál a nevet nagybetűsen, a név elején és végén felesleges szóközök nélkül,
és az életkort napokban jelenítjük meg.
"""
fictive_character = {}

name_in = input("What is your name: ")
age_in = int(input("How old are you: "))
python_exp_in_years = float(input("How many years of Python experience do you have: "))

#print(type(name_in))
#print(type(age_in))
#print(type(python_exp_in_years))

name = name_in.upper().strip()
age = age_in * 365

fictive_character["name"] = name #név nagybetűsen
fictive_character["age"] = age #életkor napokban
fictive_character["python_experience_in_years"] = python_exp_in_years #python tapasztalat években

#output string / f-string
print(f"My character is {fictive_character['age']} days old. His/her name is {fictive_character['name']} and he/she has {fictive_character['python_experience_in_years']} years experience.")

fictive_character2 = {"name": name,
                    "age": age,
                    "python_experience_in_years": python_exp_in_years}

#output string / f-string
print(f"My character is {fictive_character2['age']} days old. His/her name is {fictive_character2['name']} and he/she has {fictive_character2['python_experience_in_years']} years experience.")

#szorgalmi
python_developer_goal = input("Does he/she want to be a Python developer? (yes/no): ").strip().lower()

result = "He/she wants be a Python developer!" if python_developer_goal == "yes" else "He/she does not want to be a Python developer."

print(f"My character is {fictive_character2['age']} days old. His/her name is {fictive_character2['name']} and he/she has {fictive_character2['python_experience_in_years']} years experience. {result}")

