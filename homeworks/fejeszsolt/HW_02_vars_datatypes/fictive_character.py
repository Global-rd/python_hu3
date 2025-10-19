from pprint import pprint

 #adatbekérés
név=input("Add meg a neved: ")
életkor_években=input("Add meg az életkorod: ")
python_tapasztalat=input("Add meg hány éve foglalkozol Pythonnal: ")

#konverzió
név=str(név.title().strip())
kor_napokban=int(életkor_években)*365

#eredmény1
karakter = (f"A karakterem {kor_napokban} napos. {név} a neve és {python_tapasztalat} év tapasztalata van.")
print (karakter)

#Extra
fejlődés = input ("Akarsz profi Python fejlesztő lenni? Igennel vagy nemmel válaszolj:" )

#ternary

Fejlődés_válasz = "Profi Python fejlesztő szeretne lenn" if fejlődés.strip().title()=="Igen" else "Nem szeretne profi Python fejlesztő lenni"

pprint (f" {karakter} {Fejlődés_válasz}")

#if (egyszerűbb, áttekinthetőbb)

if fejlődés.strip().title() == "Igen":
    pprint (f" {karakter} Profi Python fejlesztő szeretne lenni")
elif fejlődés.strip().title() == "Nem":
    pprint (f" {karakter} Nem szeretne profi Python fejlesztő lenni")
else:
    pprint (f"{karakter} Eséyltelen hogy profi Python fejlesztő legyen, ha erre sem tud normálisan válaszolni!")
