#mire jók a function-ök?
#kód újrahasznosítása
#rendezettség fokozása
#separation of concerns" -> különböző feladatok különböző function-ökre bontása
#szabályok amiket érdemes betartani:
#DRY: Don't Repeat Yourself!
#Single Responsibility Principle: 
#Kerüljük el a mutable object-eket default argumentekként!

#bad example:

name_1 = "Alice"
name_2 = "Bob"
name_3 = "Dexter"

print(f"Hello {name_1}, welcome home!")
print(f"Hello {name_2}, welcome home!")
print(f"Hello {name_3}, welcome home!")
print("----------------------------")
#good example:

def greet_user(name):
    print(f"Hello {name}, welcome home!")

greet_user(name_1)
greet_user(name_2)
greet_user(name_3)

print("----------------------------")

names = ["Alice", "Bob", "Jim"]
for name in names:
    greet_user(name=name)


