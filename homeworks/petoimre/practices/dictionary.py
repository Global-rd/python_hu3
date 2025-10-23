# import pprint                # az egész modult importálja
from pprint import pprint      # így csak a pprint függvényt importálja be 
# dictionary

# megváltoztatható
# az adatok key-value párokban vannak tárolva
# rendezettek, duplikáció NEN lehetséges
# kapcsos zárójelekkel, vagy dict() konstruktorral hozható létre
# egy adott értékre a key-el hivatkozunk

student = {"name": "Jimmi",
           "age": 20,
           "grades":[4,5,5],
           "major": "computre sience",
           "is_acive": True}
# pprint.pprint(student)    # import pprint -nél
pprint(student)             # from pprint import pprint -nél

# accessing value
print(student["name"])
print(student["grades"])
print(student["grades"][-1])  # utólsó elemet a lisából


student = {"name": "Jimmi",
           "age": 20,
           "grades": {"grammer":[4,5,5],
                      "math":[4,3,4]},
           "major": "computre sience",
           "is_acive": True}

print(student["grades"]["math"])         # listát kapunk vissza
print(student["grades"]["math"][-1])     # a lista utólsó elemét adja vissza

# accessing keys

print(student.keys())                # összes keys-t adja vissza
print(type(student.keys()))          # típusa dict_keys

# accessing values

print(student.values())                # összes values-t adja vissza
print(type(student.values()))          # típusa dict_values

# add new key-value pair

student["falied exam"] = 2             # új pár hozzáadása
student["falied exam"] = 3             # érték megváltoztatása

student["grades"]["math"].append(1)   # érték hozzáadása a listához


latest_grade = int(input("Grade: "))

us_grade_map = {5:"A",
                4:"B",
                3:"C",
                2:"D",
                1:"F"}
print(us_grade_map[latest_grade])





