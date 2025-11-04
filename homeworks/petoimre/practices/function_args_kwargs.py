

# Mi a single responsibility principle lényege?   Minden függvénynek csak egy felelősségi kört kell ellátnia
# A Single Responsibility Principle (SRP), vagyis az egyetlen felelősség elve.


#  Mi az a type annotation Pythonban?    Egy megjegyzés, amely információt ad a változók típusáról.
# A type annotation (típusannotáció) Pythonban azt jelenti, hogy megadhatod egy változó, 
# függvényparaméter vagy visszatérési érték típusát — tehát jelezheted, milyen típusú adatot vársz vagy adsz vissza.
# Ez nem kötelező (a Python továbbra is dinamikusan típusos), de segít az olvashatóságban, 
# hibakeresésben és az IDE-k/ellenőrző eszközök (pl. mypy, Pyright) munkájában.

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("aaaa"))

# name: str  azt jelenti, hogy a name paraméter típusa str
# -> str   azt jelenti, hogy a függvény sztringet ad vissza



# Mit jelent az *args?
# Az *args egy változó számú pozícionális paramétert jelent:
# több értéket is átadhatsz a függvénynek, és ezek egy tuple-be kerülnek a függvényen belül.

def display_personal_info(*args):
    for i in args:
        print(i)

display_personal_info("Imre", 35, "Mezőkövesd")


# Mi történik itt?
# A függvény két paramétert vár: a és b.
# A return után két értéket ad vissza:
# az a + 5 kifejezés eredményét
# és a b + 5 kifejezés eredményét.
#Pythonban, ha több értéket adsz vissza vesszővel elválasztva, azokat egy tuple-ként (azaz párként) adja vissza.

def add(a, b):
    return a + 5, b + 5

result = add(3, 7)
print(result)                # (8, 12)
print(type(result))          # <class 'tuple'>

# Ha külön változókba bontod:

x, y = add(3, 7)
print(x)
print(y)
print(type(x))         # <class 'int'>


# Mit csinál a **kwargs?
# A **kwargs a függvényben kulcs–érték párokat fogad el (tehát név szerint megadott argumentumokat).
# Ezeket egy dictionary-ba (szótárba) gyűjti össze.
# Ebben a példában a kwargs értéke:
# {"name": "Kelly", "gender": "female"}

def display(**kwargs):
    for i in kwargs:
        print(i)

display(name="Kelly", gender="female")

# A for i in kwargs: sor
# A dictionary-n való iterálás alapértelmezetten a kulcsokon megy végig.
# Tehát i rendre:
# "name"
# "gender"

# Ha azt szeretnéd, hogy az értékeket is kiírja, akkor így kellene írni:

def display(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

display(name="Kelly", gender="female")



