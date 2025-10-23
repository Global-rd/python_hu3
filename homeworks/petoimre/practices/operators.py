import math


# assigment operators

fruit = "apple"

a = 5
a += 5   # a = a + 5

# aritmtoc operators

a = 10
b = 3
result = a + b   # / * -
modulus = a % b  # maradék osztás 
print(modulus)   # eredmény 1      10/3 = 3, maradék 1

# terminálra cls parancs -> törlés

# négyzetgyök

a = 333

# egyik megoldás
square_root = a ** (1/2)  
print(square_root)

# másik megoldás
# import math
square_root = math.sqrt(a)
print(square_root)

# logical operators

a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(not b)

# comparise operators

a = 10
b = 3

print(a > b)   # a nagyobb?
print(a == b)  # egyenlő-e?
print(a != b)  # ugye nem egyenlő?
print(a >= b)  # a nagyobb egyenlő?

# identity, membership, bitwise, ternary operators --> next lesson




