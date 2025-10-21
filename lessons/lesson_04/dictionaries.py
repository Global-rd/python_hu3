from pprint import pprint

student = {"name": "Jimmy",
           "age": 20,
           "grades": {"grammar":[4,5,5],
                      "math": [2,3,4]},
           "major": "Computer Science",
           "is_active": True}

pprint(student)

#accessing values
print(student["name"])
print(student["grades"]["math"][-1])

#accessing all keys

print(student.keys())
print(type(student.keys()))

#accessing all values
print(student.values())
print(type(student.values()))

student["failed_exames"] = 2
pprint(student)

student["failed_exames"] = 3
pprint(student)
print("------------------")
student["grades"]["math"].append(1)
pprint(student)


latest_grade = int(input("Grade: "))

us_grade_mapping = {
    5: "A",
    4: "B",
    3: "C",
    2: "D",
    1: "F"
}

print(us_grade_mapping[latest_grade])

