#Homework 02
# Task 1

name =input("Full name:").strip().upper()

age = int(input("Age:"))


age_in_calendar_days = age*365

python_exp_in_years = input("Python experience in years:")

python_dev = input("Would you like to become a python developer? Yes/No: ")

python_dev_answer = "wants" if python_dev == "Yes" else "does not want"

print(f"My character is {age_in_calendar_days} days old. His name is {name} and he has {python_exp_in_years} years experience."
      f"He/She {python_dev_answer} to become a python developer!")