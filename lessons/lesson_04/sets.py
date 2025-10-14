original_numbers = {1,2,3,4,5}
new_numbers = {4,5,6,7}

print(id(original_numbers))
original_numbers.update(new_numbers)
print(original_numbers)
print(id(original_numbers))


numbers_list = [0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2]
numbers_list = list(set(numbers_list))
print(numbers_list)
print(type(numbers_list))

original_numbers.add(78)
original_numbers.remove(78)

print("----------------")
original_numbers = {1,2,3,4,5}
new_numbers = {4,5,6,7}

intersection = original_numbers.intersection(new_numbers)
print(intersection)

#frozenset
"""
"bp"-"peking" -> 4000
"bp"-"bratislava"- > 400
"""