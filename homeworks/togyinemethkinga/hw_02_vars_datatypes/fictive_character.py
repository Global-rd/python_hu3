
name = input("Mi a keresztneved?")
#print(name.capitalize())
age = int(input ("Hány éves vagy?"))
#print(age)
age_in_days = age * 365
#print(age_in_days)
experience = int(input("Hány év tapasztalatod van a Pythonnal?"))
#print(experience)

intr = f"My character is {age_in_days} old. His/her name is {name.capitalize()} and he/she has {experience} years experience."

print(intr)

answer = input("Szeretnél profi Python fejlesztő lenni? Kérlek 'yes' vagy 'no'-val válaszolj!")

result = print(f"My character is {age_in_days} old. His/her name is {name.capitalize()} and he/she has {experience} years experience. He/She wants to be a Python developer.") if answer == "yes" else print(f"My character is {age_in_days} old. His/her name is {name.capitalize()} and he/she has {experience} years experience. He/She doesn't want to be a Python developer.")

