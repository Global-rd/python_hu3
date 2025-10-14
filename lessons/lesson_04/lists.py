letters = []
letters = list()

letters = ["a", "a", "b", "c"]
print(letters)
mixed_type_list = ["a", 123, 123.4, None, False]
print(mixed_type_list)

numbers = list(range(10))
print(type(numbers))
print(numbers)

#indexing
names = ["Sarah", "Tim", "Jimmy"]
print(names[0])
print(names[:2])

names[0] = "Steve"
print(names)

names[:2] = ["Maria", "Dexter"]
print(names)

names[:2] = ["Timmy", "Jimmy", "Lorah"]
print(names)

names[1:3] = ["Jeremy"]
print(names)


#methods

names.append("RandomName")
print(names)
names.remove("RandomName")
print(names)

names_to_add = ["Timoty", "Sarah"]
names.extend(names_to_add)
print(names)

names.insert(1, "This is the first name")
print(names)

removed_name = names.pop(2)

del names[1]

names.clear()

chocolates = input("Give me your 3 favourite chocolates separated by a comma: ")
print(chocolates)
print(type(chocolates))
chocolate_list = chocolates.split(",")
print(chocolate_list)
print(type(chocolate_list))

print(len(chocolate_list))