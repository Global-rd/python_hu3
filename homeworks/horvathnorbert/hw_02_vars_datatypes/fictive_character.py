# Képernyő törlés.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# A szükséges adatok bekérése a felhasználótól (Név, életkor, Python tapasztalat.)

name = input("Please enter your name! : ")
age = int(input("How old are you? : ")) # A bekért életkor integer típussá alakítása.
pythonexp = int(input("Your Python experience in years? : ")) # A bekért Python tapasztalat integer típussá alakítása.

# A name változóban tárolt értékről a szóközök levágása és nagybetűsként való eltárolása.

name = (name.strip())
name = (name.upper())

# A személy életkora napokban meghatározva.

ageindays = age*365

# Az adatok olvasható formába rendezése és a "result" változóban való eltárolása, valamint képernyőre írása.

result = f"This person was born {ageindays} ago. Her/His name is {name} and she/he has {pythonexp} years Python experience."
print(result)

# Érdeklődés a további Python tervekről. A válasz alapján a result változó megváltoztatása. Majd az adatok képernyőre írása.

pythondev = input("Do you want to be an expert Python developer? (yes/no) : ")
result = result + " She/He want to be an expert Python developer." if pythondev == "yes" else result + " She/He does not want to be an expert Python developer."
print(result)