#operators repeat

#arithmetic operators

a = 1 + 2

a = 10
b = 3
c = 10 // 3
print(c)

#assignment operators

a = 2
b = 3
a += 2

#comparison operators
a = 2
b = 3
print(a == b)
print(a != b)

#logical operators

a = True
b = False
print("------------")
print(a and b)
print(a or b)
print(not a)

x = 9
y = 3

print("-------------------")
print(x < 10 and y == 2)
print(x < 10 or y == 2)
print(not(x < 10 and y > 5))
print(not x < 10 and y > 5)

#identity operators
print("---------------")
print(x is y)
print(x is not y)

# identity vs comparison operator
print("---------------")
a = 10
b = 5

print(a is b)
print(a == b)
print(id(a))
print(id(b))
print("--------------")
x = [1,2,3]
y = [1,2,3]

print(id(x))
print(id(y))

print(x == y)
print(x is y)

#membership operator
print("--------------")
print(1 in x)
print(1 not in x)

#operator precedence
print("--------------")
print(True or False and False)
print((True or False) and False)

#short circuit evaluation
print(True and False and False and False)
                