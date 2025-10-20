from pprint import pprint

name = input("What's your name? ").strip().capitalize()
age_in_days = int(input("What's your age? "))*365
python_experience_in_years = int(input("What's your Python experience, in years? "))

my_character = {
    "name": name,
    "age": age_in_days,
    "Python_experience": python_experience_in_years
}

print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience_in_years} years experience.")

#extra - ternary operator
become_python_developer = input("Would you like to become a Python developer? Please answer with Y or N ")

yes_answer = f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience_in_years} years experience. He/she wants to be a Python developer!"
no_answer = f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience_in_years} years experience. He/she does not want to be a Python developer!"

print(yes_answer) if become_python_developer == "Y" else print(no_answer) if become_python_developer=="N" else print("Wrong answer, please try again!")

"""
n = 5
res = "Even" if n % 2 == 0 else "Odd"
print(res)
"""