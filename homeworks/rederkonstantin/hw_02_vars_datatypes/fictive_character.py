""" 
Ask and store basic information about user's character.

"""

"""
name_of_character = input("Add meg a karaktered nevét: ")\
    .lstrip()\
    .rstrip()\
    .upper()

A strip funkcióról azt hittem, hogy a string besejében levő space-ekat is kiveszi..... 

"""
name_of_character = input("Add meg a karaktered nevét: ").strip().upper()



age_of_character_in_years = int(input("Add meg a karaktered életkorát években: "))
age_of_character_in_days = age_of_character_in_years * 365

age_of_experience_in_python = int(input("Add meg a python programozásban eltöltött éveidet: "))

future_level_of_python_skill = input("Szerernéd, hogy a karaktered profi python fejlesztő legyen? ( igen/nem )")

wish_of_future_python_skill = "szeretne" if future_level_of_python_skill == "igen" else "nem szeretne"

print(f"A karakterem {age_of_character_in_days} napot töltött el a világában, \
a neve {name_of_character}, \
{age_of_experience_in_python} év python programozói tapasztalattal rendelkezik \
és {wish_of_future_python_skill} profi python fejlesztő lenni.")
