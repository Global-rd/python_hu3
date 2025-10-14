my_list = [1,2,3]
print(f"Original list: {my_list}")
print(f"Original list ID: {id(my_list)}")

my_list.append(4)
print(f"Modified list: {my_list}")
print(f"Modified list ID: {id(my_list)}")

print("------------------")
my_tuple = (1,2,3)
print(f"Original tuple: {my_tuple}")
print(f"Original tuple ID: {id(my_tuple)}")

new_tuple = my_tuple + (4,)

print(f"Modified tuple: {new_tuple}")
print(f"Modified tuple ID: {id(new_tuple)}")

# strings

name = "Sarah"
name[0] = "T"


#mutable types:
#lists, dictionaries, sets, (bytearrays)
#immutable types:
#int, bool, float, string, tuple, frozenset, none