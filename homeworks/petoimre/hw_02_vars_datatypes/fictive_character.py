'''
Exercise one
Fictive character
'''
character_name = (input("Type in your name:"))
character_age = int(input("Give me how old are you:"))
character_experience = int(input("How much experience do you have in Python?"))
character_name = character_name.title()
character_name = character_name.strip()
character_age_in_day = character_age*365
print(f"My character is {character_age} years old. His/her name is {character_name} and he/she has {character_experience} years experience in Python." )