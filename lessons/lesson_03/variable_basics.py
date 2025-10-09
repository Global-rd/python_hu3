#variables / változók

name = "Jim"
age = 25

print(name)
age = 25 + 1
print(age)


camelCaseVariableName = "" #BAD PRACTICE
PascalCaseVariableName = ""  # BAD PRACTICE

snake_case_variable_name = ""

#KONSTANSOK

PI = 3.14
MAX_ROUNDS = 3

# dinamikus típusosság / dynamically typed language

"""
int x;
x = 10;
"""

x = 10
print(x)
x = "appletree"
print(x)
#print(x/2)

#reference 
print("---------")

my_var_1 = 15
my_var_2 = 15

print(id(my_var_1))
print(id(my_var_2))

# my_var_1 -> 15 -> 140705754674536
# my_var_2 -> 20 -> 140705754674696
print("---------")
x = 11
y = x #11

print(id(x))
print(id(y))
print(x)
print(y)

x = 10

print(id(x))
print(id(y))
print(x)
print(y)

#GARBAGE COLLECTION
x = 1000 # 1000's reference count: 1
x = 2000 # 1000's reference count: 0