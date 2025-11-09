def divide_numbers(a,b):
    return a / b


#ZERO DIVISION ERROR
result = divide_numbers(10, 1) #0
print(result)

#VALUE ERROR
#age = int(input("How old are you?"))
#print(age)

#INDEX ERROR

my_list = [1,2,3,4,5]
print(my_list[1])

#KEY ERROR

my_dict = {"a": 12,
           "b": 13}

#print(my_dict["c"])
print(my_dict.get("b", 0))

try:
    a = float(input("First number:"))
    b = float(input("Second number:"))
    c = a / b
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivision Error: {e}")
except Exception as e:
    print(f"Something unexpected happened: {e}")
else:
    print(c)
finally:
    print("Division attempt finished")

#RAISE EXCEPTIONS

#bad example:

def calculate_rectangle_area(a, b):
    return a * b

area = calculate_rectangle_area(10, 5)
print(area)
area = calculate_rectangle_area(10, -1)
print(area)

#good example:

def calculate_rectangle_area(length, width):
    if length <=0 or width <=0:
        raise ValueError("Both params must be a positive number!")
    return length * width

#calculate_rectangle_area(10, -2)

try:
    area = calculate_rectangle_area(10, -2)
except ValueError as e:
    print(f"ValueError: {e}")


#custom exception!