from pprint import pprint

name = input("What's your name? ").strip().capitalize()
age_in_days = int(input("What's your age? "))*365
python_experience_in_years = int(input("What's your Python experience, in years? "))

my_character = {
    "name": name,
    "age": age_in_days,
    "Python_experience": python_experience_in_years
}

# print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience_in_years} years experience.")

#extra - ternary operator
become_python_developer = input("Would you like to become a Python developer? Please answer with Y or N ")

dev_intention = "wants" if become_python_developer =="Y" else "does not want"

answer = f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience_in_years} years experience. He/she {dev_intention} to be a Python developer!"

if become_python_developer in ('Y', 'N'):
   print(answer)
else:
    print("Wrong answer, please try again!")

