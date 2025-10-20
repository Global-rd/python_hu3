#Homework 02
# Task 1

name =input("Full name:").strip().upper()

age = int(input("Age:"))


age_in_calendar_days = age*365

python_exp_in_years = input("Python experience in years:")

python_dev = input("Would you like to become a python developer? Yes/No: ")

python_dev_answer = "He wants to be a Python developer!" if python_dev == "Yes" else "He does not want to be a Python developer!"

print(f"My character is {age} years old. His name is {name} and he has {python_exp_in_years} years experience.{python_dev_answer}")