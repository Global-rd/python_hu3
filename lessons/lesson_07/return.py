#function without return value
def add(num_1, num_2):
    print(num_1, num_2)

value = add(1, 2)
print(value)
print(type(value))

#function with return value
def add(num_1, num_2):
    return num_1 + num_2

value = add(1, 2)
print(value)
print(type(value))


# return early

print("---------------")
def calculate_age_in_days(age):
    if age < 0:
        print("Invalid age! Please provide a positive number!")
        return
    age_in_days = age * 365
    return age_in_days
    
age_in_days = calculate_age_in_days(-1)
print(age_in_days)

#returning multiple values

def multiply_values(a, b):
    return a*2, b*2

print(type(multiply_values(1,2)))
x,y = multiply_values(1,2)
print(x)
print(y)
