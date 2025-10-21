#ITERABLE: egy objektum amely képes visszaadni az elemeit (pl: string, list, dict)
#ITERATOR: egy speciális objektum amely egyszerre egy elemet ad vissza egy iterable-ből, iter() function-nel hozzuk létre, és a next() function-t hívjuk meg
#ITERATION: elemenkénti haladás folyamata, egyik elemről a másikra való eljutás
#LOOP: automatizálja az iteration folyamatát

#PÉLDA:

#ITERABLE: egy spotify (vagy bármilyen) lejátszási lista, benne a kedvenc zenéinkkel
#ITERATOR: mi magunk, akik egyik zeneszámról a másikra tudunk kattintani, tudjuk hogy most melyik szám szól, és képesek vagyunk a következőre ugrani
#ITERATION: következő számra való ugrás a next gombbal
#LOOP: automatikus lejátszás anélkül, hogy mi magunk megnyomnánk a next gombot, egészen adig amíg van zene a listában

#ITERABLE:
playlist = ["I'm a barbie girl", "Heavy is the crown", "8 óra munka", "I got options"]
#ITERATOR:
it = iter(playlist)
#print(type(it))
#ITERATION:
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

