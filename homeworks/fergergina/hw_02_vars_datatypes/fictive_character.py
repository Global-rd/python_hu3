name = input("What is your name? ").title().strip()
age = int(input("How old are you? "))
python_experience = input("Python experience in years? ")

age_in_days = age * 365
print(f"My character is {age_in_days} days old. Her name is {name} and she has {python_experience} years experience.")