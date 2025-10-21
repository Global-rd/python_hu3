
name = input("Mi a keresztneved?").strip().capitalize()
#print(name.capitalize())
age = int(input ("Hány éves vagy?"))
#print(age)
age_in_days = age * 365
#print(age_in_days)
experience = int(input("Hány év tapasztalatod van a Pythonnal?"))
#print(experience)

intr = f"My character is {age_in_days} old. His/her name is {name} and he/she has {experience} years experience."

print(intr)

answer = input("Szeretnél profi Python fejlesztő lenni? Kérlek 'yes' vagy 'no'-val válaszolj!")

result = "wants" if answer == "yes" else "doesn't want"

print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {experience} years experience. He/She {result} to be a Python developer.")
