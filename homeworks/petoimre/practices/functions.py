# functions

name_1 = "Alice"
name_2 = "Dexter"
name_3 = "Bob"

def great_user(name):
    print(f"Hello {name}, welcome home!")

great_user(name_2)



# for-loop-ban is meghívható
names = ["Alice", "Dexter", "Bob"]
for name in names:
    great_user(name)                        # great_user(name=name) is lehetséges

# return
def add(num_1, num_2):                     # num_1, num_2   paraméterek
    return num_1 + num_2

x = add(5, 3)                               # 5, 3    agunentum-ok
print(x)

# return early
def calc_age_in_days(age):
    if age <= 0:
        print("Give a positive number")
        return                                          # return none   ugyanaz
    age_in_days = age * 365
    return age_in_days

# returning multiple variables

def multiple_var(a, b):                  
    return a*2, b*2

print(type(multiple_var(2, 4)))                  # <class 'tuple'>
x,y = multiple_var(4, 6)                      # tuple unpacking
print(x)
print(y)

# positional argument

def add(x, y):
    return x+y

result = add(1,2)
result = add(x=1,y=2)
result = add(y=1,x=2)

# default arguments

def get_greeting(name="Guest"):
    print(f"Hello {name}")

get_greeting("Janice")
get_greeting()

# combnate default and posizional arguments

def show_book_details(title, author="Test Writer", year=2025):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"year: {year}")

show_book_details("Test book")
show_book_details("Test book", "X Y")
show_book_details("Test book", "X Y", 2020)

# MUTABLE OBJECT AS DEFAULT ARGUMENT
#BAD EXAMPLE                               # ne adjunk meg mutable értéket argumentumként!!!!!!!
def append_to_list(value,my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))                   # [1]
print(append_to_list(2))                   # [1, 2]
print(type(append_to_list(2)))             # <class 'list'>


# GOOD EXAMPLE

def append_to_list(value,my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

print(append_to_list(1))                   # [1]
print(append_to_list(2))                   # [2]
print(type(append_to_list(2)))             # <class 'list'>


# arbitrary positional arguments

def calc_total_price(*items):
    total = 0

    for _, price, quantity in items:
        total += price*quantity
    return total 

total_price = calc_total_price(("apple", 300, 2),
                               ("banana", 500, 4),
                               ("orange", 150, 3))

print(total_price)


# arbitrary keyword arguments

def describe_person(**kwargs):
    print(kwargs)
    print(type(kwargs))                           # <class 'dict'>
    for k,v in kwargs.items():
        print(f"key: {k}, value: {v}")

describe_person(name="John", age=28, job="programmer")



def introduce_person(name, age, *hobbyes, country="Hungary", **additional_info):
    print(f"Name: {name}")
    print(f"age: {age}")
    print(f"Country: {country}")

    if hobbyes:
        print("Hobbyes: ")
        for hobby in hobbyes:
            print(hobby)
    if additional_info:
        print("Additional info")
        for k,v in additional_info.items():
            print(f"{k} - {v}")





introduce_person("Bob", 25, "Hiking", "reading", "driving", country="Swis", occupation="programmer", has_pet=True)
print(introduce_person)



# példa project

def register_user(users, name, age):       # def register_user(users:list, name:str, age:int) -> None:
    """
    Registers an user to the users list.
    """
    user = {"name": name, "age": age}
    users.append(user)
    print(f"user reg success: {user}")

def update_user():
    pass

def display_user_age()
    pass

def display_all_users():
    pass

def main():
    pass

main()







# [
#  {"name": "John", "age": 10}
#  {"name": "Mary", "age": 11}
#  {"name": "Timy", "age": 12}
# ]

                                                     
                                                     
                                                     
                                                     
                                                     













