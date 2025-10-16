"""
Ha csak a kezdő betű kell, hogy nagybetű legyen,
akkor az str.capitalize() a használandó metódus.
Vagy bekérem a character_name simán input-tal és később végzem el rajta
a str metódusokat.
character_name = input("Please enter your name: ")
character_name = character_name.upper().strip()
Ez az utóbbi szerintem az olvashatóbb kódot adja.
"""

character_name = input("Please enter your name: ").strip().upper()
character_age = int(input("Please enter your age: "))
character_python_experience_in_years = input(
    "Please enter your Python experience in years: "
)
is_pro_python_developer = input(
    "Would you like your character to be a professional Python developer? (yes/no): "
)

character_age_in_days = character_age * 365

dev_intention = "wants" if is_pro_python_developer == "yes" else "does not want"

print(
    f"My character is {character_age_in_days} days old. "
    f"His/her name is {character_name} and he/she has {character_python_experience_in_years} year(s) experience. "
    f"He/she {dev_intention} to be a Python developer!"
)
