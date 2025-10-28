#1. feladat

Name = input("Your name:").strip().title()
Age = int(input ("Your age:"))
Age_in_days = Age * 365
Python_exp_in_years = input("How many years of experience do you have in python?")

Character_profile = f"My character is {Age_in_days} old. His/her name is {Name} and he/she has {Python_exp_in_years} years experience."

print(Character_profile)

Answer = input("Do you want to be python a developer? Please answer Yes or No.")
Resoult = "wants" if Answer == "Yes" else "doesn't want"

print(f"My character is {Age_in_days} old. His/her name is {Name} and he/she has {Python_exp_in_years} years experience.He/She {Resoult} to be a python developer! ")