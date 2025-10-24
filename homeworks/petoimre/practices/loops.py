# iterable jelentése: iterálható azaz végig lehet menni az elemein. list, str, dict
# iterator: egy objektum ami egyszerre egy elemet ad vissza az iterable-ből.
#           iter() functionnal hozzuk létre és a next() és a next functiont hívjuk meg.
# iteration: az egyik elemről a másikra haladás folyamata. iteráció
# loop: ennek az egésznek az automatizálása

import time

songs = ["Dal_1", "Dal_2", "Dak_3", "Dal_4"]

it = iter(songs)
print(songs)
print(type(it))           # 'list_iterator'

print(next(it))
print(next(it))
print(next(it))
print(next(it))


# for loop     egy iterable (list, tuple, dict, set, range, str stb) feletti iterációra szolgál

for song in songs:
    print(song)
 #   time.sleep(1)


student = {"name": "Jimmy",
           "age": 20,
           "grades": {"grammar":[4,5,5],
                      "math": [2,3,4]},
           "major": "Computer Science",
           "is_active": True}

for k,v in student.items():
    print(f"Key:  {k}, Value:  {v}")

for k in student.keys():
    print(k)

for v in student.values():
    print(v)

# range   (iterable)

for i in range(0,5):
    print(i)

# while loop       utasításkészletet hajtunk végre amíg a megadott feltétel igaz.

i = 1

while i <= 6:
    print(i)
    i += 1              # 1-6-ig írja ki

# input adatbekérés

while True:
    answer = input("Do you want to be a professional python developer? (yes/no)")
    if answer in ["yes", "no"]:
        break

# list comprehension

# without list comprehension    listát tölt fel négyzetre emelt értékekkel
numbers = [1, 2, 3, 4, 5]
sqr = []

for number in numbers:
    sqr.append(number ** 2)    # négyzetre emeli
print(sqr)

# with list comprehension

sqr = [number ** 2 for number in numbers]

# without list comprehension csak párosak

even_sqr = []
for number in numbers:
    if number % 2 == 0:           # ha maradék osztás == 0
        even_sqr.append(number ** 2)
print(even_sqr)

# with list comprehension

even_sqr = [number ** 2 for number in numbers if number % 2 == 0]

# futási sebesség mérése

numbers = range(1, 1000000)

# loop -al
start = time.time()
print(start)
sqr_loop = []
for num in numbers:
    sqr_loop.append(num ** 2)
print(f"For loop: {time.time() - start}") 

# comp-al
start = time.time()
sqr_comp = [num ** 2 for num in numbers]
print(f"Comp: {time.time() - start}") 

# brake, continue, pass

# break: kilépés a ciklusból azelőtt, hogy véget érne.
# valamilyen feltételhez kötjük, pl keresünk egy elemet és nincs értelme tovább menni.

# continue: kilépés a jelenlegi iterációból és ugrás a következőre. pl valamelyik elem kivételt képez.

# pass: nem kizárólag a loop-hoz kötődik. "placeholder" olyan kódrészletekgez, amit később írunk meg.

# break
# a felh max 3-szor próbálkozhat

attemps = 0

while attemps < 3:
    passw = input("Enter your password: ")
    if passw == "secret":
        print("Access granted")
        break
    else:
        print("Wrong password. Try again!")
    attemps += 1
else:
    print("Reached maximum amoun of retries, try again tomorrow! ")

# continue

number = 0

while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(f"Processing number:  {number}")


# pass

numbers = [1,2,3,4,5]
for num in numbers:
    pass
# semmi sem történik

# nested loop

seating_chart = [["Alice", "Bob", "Dexter"],
                ["Emily", "Timmy", "Jimmy"],
                ["Charles", "Henry", "Anette"]]

for row in seating_chart:
    print(row)                 # kivehető
    for person in row:
        print(person)

# enumerate

# without enumeration
playlist = ["zene_1", "zene_2", "zene_3", "zene_4"]

id = 1
for song in playlist:
    print(id, song)
    id += 1

# with enumeration

id = 1
for id, song in enumerate(playlist, 1):     # tupple-t ad vissza, id-t az enum adja. nem kell növelni
    print(id, song)

# zip

students = ["Alice", "Bob", "Dexter"]
scores = [100, 89, 95]                        # ahol kevesebb tag van addig megy

for student, score in zip(students, scores):
    print(f"{student} has scored {score} points.")

# FizzBuzz  list-be írva

result = []
n = 15

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        result.append("FizBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(i)

print(result)





    








