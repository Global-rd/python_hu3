name = input("What is your name? ")
age = input("How old are you? ")
python_experience = input("Python experience in years? ")

name = name.title().strip()

age = int(age)
days = age * 365
print(f"My character is {days} days old. Her name is {name} and she has {python_experience} years experience.")