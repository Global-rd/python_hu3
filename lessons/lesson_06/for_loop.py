import time
songs = ["I'm a barbie girl", "Heavy is the crown", "8 óra munka", "I got options"]

for song in songs:
    print(f"Playing {song}")
    #time.sleep(2)

print("--------------")
student = {"name": "Jimmy",
           "age": 20,
           "grades": {"grammar":[4,5,5],
                      "math": [2,3,4]},
           "major": "Computer Science",
           "is_active": True}

for k,v in student.items():
    print(f"Key: {k}, Value: {v}")

print("--------------")
for k in student.keys():
    print(k)

print("--------------")
for v in student.values():
    print(v)

#range
for i in range(0,5):
    print(i)