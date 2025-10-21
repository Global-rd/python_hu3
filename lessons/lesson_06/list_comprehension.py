import time

numbers = [1,2,3,4,5]
squared_numbers = []

#without list comprehension:

for number in numbers:
    squared_numbers.append(number ** 2)

print(squared_numbers)


#list comprehension

squared_numbers = [number ** 2 for number in numbers]

#without list comprehension:

even_squares = []

for number in numbers:
    if number % 2 == 0:
        even_squares.append(number ** 2)

print(even_squares)

#with list comprehension:

even_squares = [number ** 2 for number in numbers if number % 2 == 0]

#performance comparison

numbers = range(1, 1000000)

start = time.time()
print(start)
squares_loop = []
for num in numbers:
    squares_loop.append(num ** 2)

print(f"For loop: {time.time() - start}")

start = time.time()
squares_comprehension = [num ** 2 for num in numbers]
print(f"Comprehension: {time.time() - start}")


