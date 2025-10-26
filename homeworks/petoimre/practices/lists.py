# list
# Bármilyen adatot tárolhat egy lisán belül is
# az adatok sorrendben vannak, indexelve vannak
# az adatok megváltoztathatóak, lehetnek kötük duplikátumok
# szögletes zárójellel, vagy a list constructorral hozzuk létre
# megőrzi a sorrendet

do_list = []         # üres is lehet
do_list = list()     # constructorral
names = ["Sarah", "Tim", "Jimi", "Joe"]
names.append("Marta")       # elem hozzáadása           methodd
names.remove("Joe")             # elem eltávolítása
mixed_list = ["apple", 255, 3.14, None, True]
print(mixed_list)

# iterable
# range obj
numbers = list(range(10))  # 0-99 lesz benne
print(type(numbers))
print(numbers)

# indexing
print(names[0])   # első elem ugyanúgy mint a string-nél.Egy elem esetén sztinget ad vissza
print(names[:2])  # első kettő, és list típst ad vissza

names[0] = "Steve"   # az első elemet Steve-re cseréli. felülírja
names[:2] = ["Maria", "Dexter"]  # az első kettőt cserélli ki. Listát kell megadni
names[:2] = ["Timmy", "Jimy", "Lora"] # az első kettő helyére 3-at adunk be. Megnöveli a lista hosszát
names[1:3] = ["Jeremy"] # a második és harmadikhelyére egyet adunk meg, csökkenti a lista hosszát
#names[:2] = "Joe"  # Ha karakterláncot adunk be, szétszedi karakterekre és elemenként teszi be.
print(names)

# method
names.append("Yvy")    # a végére fűzi
names.remove("Yvy")    # törli az elem első előfordulását
names_to_add = ["Timoty", "Sarah"]
names.append(names_to_add)   # egy plusz listaként jelenik meg a listán belül
print(names)
names.extend(names_to_add)  # így már elemenként fűzi hozzá
print(names)
names.insert(1, "Timoty")  # első szám ami elé akarok beszúrni
print(names)
ret_data = names.pop(1)   # törli és visszaadja a törölt értéket index alapján
del names[1]    # törli, de nem adja vissza az értéket
names.clear()  # törli az összes elemet

# lista létrehozása terminálból

choco = input("Give me your 3 favotite choco sp by comma: ")
choco_list = choco.split(",")   # így list lett
print(len(choco))   # megadja a lista hosszát





