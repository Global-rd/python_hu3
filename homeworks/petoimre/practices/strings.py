
fruit = "rapsberry"
fruit_lenght = len(fruit)
print(fruit_lenght)

# concatenation

first_name = "Peto"
last_name = "Imre"
full_name = first_name + last_name
print(full_name)

# interpolated string / f-string
introduction = f"My name is {first_name} {last_name}."
print(introduction)

# indexing sliceing
print(fruit)          # rapsberry
print(fruit[0])       # első karakter = 0 index
print(fruit[1])       # második karakter = 1 index
print(fruit[-1])      # utólsó karakter
print(fruit[1:4])     # 1-2-3 index  4-ik exclusive    első rész inclusive, második exclusive    --> aps
print(fruit[:3])      # elejétől a 3-ik excl indexig     0-1-2  --> rap
print(fruit[-2:])     # -2 -től a végéig  incl --> ry
print(fruit[-3:-1])   # -3 -tól a vágétőt vissza -1 ig, ami exclusive  --> rr  (a két utólsó karakter)
print(fruit[-1::-1])  # induljon a végétől visszafelé egyesével
print(fruit[-1::-2])  # induljunk a végétől visszafelé kettessével     
print(fruit[0::2])    # elejétől kettessével előre    --> rpbry
print(fruit[-8::2])   # a -8-tól kettessével felfelé   -->  aser

# string method

# method  amit az objektum csinélni tud (ugat, eszik, alszik)
# attibutum ami jellemzi az objektumot (súly, szín, fajta)

print(fruit.capitalize())         # nagybetűssé teszi az első betűt
print(fruit.upper())              # minden karakter nagybetű lesz
print(fruit.title())              # minden szó első betűje nagy
print(fruit.replace("a", "x"))    # az a betűt kicseréli x-re
print(fruit.strip())              # kiveszi elől-hátul a szóközöket
print(fruit.lstrip())             # csak balról veszi ki aszóközöket
print(fruit.rstrip())             # csak jobbról veszi ki a szóközöket
print(fruit.upper().replace("a", "t").strip())  # egymásba ágyazva  method chaining
print(fruit.casefold())          # minden karaktert kisbetűssé alakít, a Unicode szabvány szerint, tehát nem csak az angol ábécére működik, hanem például német ékezetes betűkre is (ß → ss).
print(fruit.center(20, "x"))
print(fruit.center(10))
# print(fruit.center(width, fillchar))  # szöveget középre igazítja egy megadott szélességű mezőben, 
# és a hiányzó helyeket kitölti (alapértelmezetten szóközzel, de más karakter is megadható).
# az üres helyeket kitöltő karakter (opcionális, alapértelmezés: ' ')

 



