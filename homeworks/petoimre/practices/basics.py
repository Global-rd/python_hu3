# virtual envoriment aktiválási folyamata
# project könyvtárat kinyitni
# .venv file létrehozása:   python -m venv venv      ekkor létrejön a .venv mappa

# a win házirend kikapcsolása:     Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# környezet aktiválása:            .\venv\Scripts\Activate.ps1

# A (venv) jelzi, hogy most már a virtuális környezetedben dolgozol.
# A pip-installált csomagok (pl. pandas, plotly, stb.) csak ebben a környezetben lesznek elérhetők.

# pip install fastapi

# pip freeze > requirements.txt             létrehozza a requirements.txt file-t
# pip install -r requirements.txt           feltelepíti a requirements.txt-ben levő csomagokat

# terminal futásának megállítása:   ctr + C



# beépített nem primitív adattípusok
# list = ["apple", 255, 3.14, None, True]        szögletes zárójel
# dict = 

'''

# Mi lesz az alábbi kódrészlet eredménye?
x = 0

while x < 5:

  x += 1

  if x == 3:

    continue

  print(x)



# Mi lesz az alábbi kódrészlet eredménye?

for i in range(3):

  for j in range(2):

    print(i, j)




# Mi lesz az alábbi kódrészlet eredménye?
numbers = [1, 2, 3, 4, 5]

new_numbers = [n * 2 for n in numbers if n % 2 == 0]

print(new_numbers)



# Mi lesz az alábbi kódrészlet eredménye?
x = 5 

while True:

  if x < 10:

    x += 1 

  else:

    break

print(x)

'''

# Mi lesz az alábbi kódrészlet eredménye?
x = 0

while x < 5:

  x += 1

  if x == 3:

    continue

  print(x)

