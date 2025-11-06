def divide_number(a, b):
    return a / b

# zero division
result = divide_number(10, 3)
print(result)

# value error
#age = int(input("How old are you? "))
#print(age)

# index error
m_list = [1,2,3,4,5]
print(m_list[2])

# key error
m_dict = {"a": 1,
          "b": 2}

#print(m_dict["d"])   # key error
print(m_dict.get("w", 0))   # ha rossz a key, 0-t adja vissza

try:                                                  # mindig lefut
    number = int(input("How old are you? "))
    res = 10/number
except ValueError:                                    # lefut, ha ValueError van. Ha nem számot ír be.
    print(f"The input isn't number.")
except ZeroDivisionError:                             # lefut, ha 0-t ír be.
    print(f"Error: Can't divide with zero.")                       
else:                                                 # lefut, ha nincs hiba.
    print(f"Result: {res}")                               
finally:                                              # mindig lefut.
    print(f"The application ready running.")

#---another example

try:
    a = float(input("First number:"))
    b = float(input("Second number:"))
    c = a / b
    # print(c)                                            # akkor, ha el van hagyva az else: és a finally:
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError as e:                           # az  as e:  az e visszaadja a hiba szöveger és a kódot 
    print(f"ZeroDivisionError: {e}")
except Exception as e:                                    # előre nem definiált, váratlan hibákhoz.
    print(f"Something unexpected happend: {e}")
else:                                                      # el lehet hagyni
    print(c)
finally:                                                   # el lehet hagyni
    print("Division attempt finishrd.")


# raise exeption  (saját hibakezelés. ValueError saját szöveggel)

def calculate_rectangle_area(length, width):
    if length <=0 or width <=0:
        raise ValueError("Both params must be a positive number!")    # ha ide fut, kiszáll. Ezért nem kell else: (early return:)
    return length * width

# calculate_rectangle_area(10, -2)

try:
    area = calculate_rectangle_area(10, -2)
except ValueError as e:                           # így az e:-ben a saját hibaüzenetünk jön elő.
    print(f"Value error: {e}")


# custom exception   OOP tudás kell!





                



