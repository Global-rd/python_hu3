name = input("what is your name?: ").strip().upper()
age = int(input("How old are you?: "))
python_experience = int(input("How long do you work with Python (in years): "))


age_in_days = age * 365

career = input("Do you want to be a pro Python developer (yes/no)?: ")
if career.lower() == "no":
    ending = "He/she does not want to be a Python developer!"
elif career.lower() == "yes":
    ending = "He/she wants to be a Python developer!"
else:
    ending = ""

print(f"My character is {age_in_days} days old. "
      f"His/her name is {name} and he/she has {python_experience} years experience. "
      f"{ending}")
