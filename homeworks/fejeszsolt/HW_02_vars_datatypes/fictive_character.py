from pprint import pprint

 #adatbekérés
name=input("Add meg a neved: ").title().strip()
age_in_years=input("Add meg az életkorod: ")
python_experience=input("Add meg hány éve foglalkozol Pythonnal: ")

#konverzió

age_in_days=int(age_in_years)*365

#eredmény1
character = (f"A karakterem {age_in_days} napos. {name} a neve és {python_experience} év tapasztalata van.")
print (character)

#Extra
development = input ("Akarsz profi Python fejlesztő lenni? Igennel vagy nemmel válaszolj:" )

#ternary

development_response = "Profi Python fejlesztő szeretne lenn" if development.strip().title()=="Igen" else "Nem szeretne profi Python fejlesztő lenni"

pprint (f" {character} {development_response}")

#if (egyszerűbb, áttekinthetőbb)

if development.strip().title() == "Igen":
    pprint (f" {character} Profi Python fejlesztő szeretne lenni")
elif development.strip().title() == "Nem":
    pprint (f" {character} Nem szeretne profi Python fejlesztő lenni")
else:
    pprint (f"{character} Eséyltelen hogy profi Python fejlesztő legyen, ha erre sem tud normálisan válaszolni!")
