condition = True

if condition == True:
    print("This condition is true.")
else:
    print("The conditions is false or none.")

print("test")

#truthy-falsy values
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("something"))
print(bool([]))
print(bool([1,2,3]))

if condition:
    print("This condition is true.")
else:
    print("The conditions is false or none.")

number = 0

if number:
    print(f"The value of the number is other than 0: {number}")
else:
    print(f"The number is 0")


numbers = []

if numbers:
    print("There are values in the list")
else:
    print("The list is empty")

print("-------------------")
#if-elif-else
number = 12

if number == 10:
    print("The number is 10")
elif number == 11:
    print("The number is 11")
elif number == 12:
    print("The number is 12")
else:
    print("The number is something else")


#if-elif-else using mempership/logical operators
print("----------------")
fruits = ["raspberry", "banana", "cherry", "watermelon"]

if "cherry" in fruits:
    print("cherry is in fruits")

if "banana" in fruits:
    print("banana is in fruits")

if "raspberry" in fruits or "banana" in fruits:
    print("either raspberry or banana is present in fruits")


#if-elif else with logical operators

a = 1
b = 2

if a is b:
    print("the 2 objects are the same")

c = 3

# combining multiple operators in a single statement:

if (a is not b and c == 3 and ("cherry" in fruits or "elderflower" in fruits)):
    print("All these are true")