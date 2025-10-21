import math

player_name = input ("Please write characther's name: ")
age_in_years = input(f"{player_name}, how old are you? ")
python_exp_in_years = input(f"{player_name}, how many years phyton experience do you have? ")
age_in_days = age_in_years * 365

print (f"My character's name is {player_name}")
print (f"{player_name} is {age_in_days} yeas old")
print (f"{player_name} has {python_exp_in_years} years python experience")