def greet(name): #PARAMETER
    print(f"Hello {name}")

greet("Johnny") #ARGUMENT

#positional arguments:

def add(x,y):
    return x+y

result = add(1,2)
result = add(x=2,y=1)
result = add(y=1,x=2)

#default arguments:

print("----------")

def get_greeting(name="Guest"):
    print(f"Hello {name}")

get_greeting(name="Janice")
get_greeting()

#combining positional and default arguments
print("----------")

def show_book_details(title, author="Test Writer", year=2025):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")


show_book_details("Test Book")
show_book_details("Test Book", "XY")
show_book_details("Test Book", "XY", 2020)


#MUTABLE OBJECTS AS DEFAULT ARGUMENTS:

#BAD EXAMPLE:
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))

#[1]
#[2]

#GOOD EXAMPLE>
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


print(append_to_list(1))
print(append_to_list(2))