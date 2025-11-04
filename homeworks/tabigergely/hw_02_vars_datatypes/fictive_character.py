#1. feladat

name = input("Your name:").strip().title()
age = int(input ("Your age:"))
age_in_days = age * 365
python_exp_in_years = input("How many years of experience do you have in python?")

character_profile = f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience."

print(character_profile)

#Szorgalmi

answer = input("Do you want to be python a developer? Please answer Yes or No.")
resoult = "wants" if answer == "Yes" else "doesn't want"

print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience.He/She {resoult} to be a python developer! ")