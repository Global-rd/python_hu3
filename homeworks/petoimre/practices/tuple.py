#  tuple

# több elem tárolása
# rendezett és megváltozhatatlan, írásvédett   inmutuble
# zárójelekkel(), vagy a tuple() konstruktorral hozható létre

cordinates = (25.587444, 48.524877)
print(cordinates[0])                    # indexxel lehet hivatkozni az elemeire
print(cordinates[1:2])                  # uganúgy mint a string és list
print(type(cordinates[1:2]))            # type: 'tuple'

# methodes

cordinates.count(48.524877)            # a beírt érték (hányszor) szerepel benne
cordinates.index(25.587444)            # hányadik indexen van az érték

# modify

my_tuple = (1,2,3,4)

new_tuple = my_tuple + (5,)            # csak így lehet módosítani. új mamória címre kerül.

# mutable types: 
# list, dictionary, set, (bytearray)

# immutuable
#  int, bool, float, string, tuple, frozenset, none






