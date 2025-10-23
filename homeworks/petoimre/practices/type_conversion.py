
fruit = "apple"
print(type(fruit))    # type() egy method
age = 43
print(type(age))

# megkérdezni a típust
print(isinstance(fruit, str))      # isistance() egy function

y_n = isinstance(age, int)          # str, int, float, bool
print(y_n)

# type conservation

num_int = 10
num_float = 10.5
result = num_int * num_float
print(result)
print(type(result))   # ha float van benne, az eredméy is float lesz

age = "14"
print(age*4)   # eredmény 14141414

result = int(age) * 4    # típuskonverzió
print(result)

# input bekérése

age = int(input("How old are you? "))   # input mindig str  --> kell a típ conv

# thruthy-falsy

print(bool(1))            # minden a mi több mint 0 = True
print(bool(0))            # False
print(bool(""))           # üres karakterlánc False
print(bool("apple"))      # ha van benne szöveg mindig True  Ellenőrizni, hoy tatalmaz-e karaktereket.






