import os

# Képernyő törlés.

os.system('cls' if os.name == 'nt' else 'clear')

# A szükséges adatok bekérése a felhasználótól (Név, életkor, Python tapasztalat.)

name = input("Please enter your name! : ").strip().upper() #sSzóközök levágása és nagybetűsként való eltárolása
age = int(input("How old are you? : ")) # A bekért életkor integer típussá alakítása.
python_exp = int(input("Your Python experience in years? : ")) # A bekért Python tapasztalat integer típussá alakítása.

# A személy életkora napokban meghatározva.

age_in_days = age*365

# Az adatok olvasható formába rendezése és a "result" változóban való eltárolása, valamint képernyőre írása.

result = f"This person was born {age_in_days} ago. Her/His name is {name} and she/he has {python_exp} years Python experience."
print(result)

# Érdeklődés a további Python tervekről. A válasz alapján a result változó megváltoztatása. Majd az adatok képernyőre írása.

python_dev = input("Do you want to be an expert Python developer? (yes/no) : ")
dev_intention = "want" if python_dev == "yes" else "does not want"

result = f"This person was born {age_in_days} ago. Her/His name is {name} and she/he has {python_exp} years Python experience. He/She {dev_intention} to be an expert Python developer."

print(result)