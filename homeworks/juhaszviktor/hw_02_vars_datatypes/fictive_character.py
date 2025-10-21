name = input("Név: ")
name = name.strip().capitalize()
#print(name)

age = input("Életkor: ")
age_in_days = int(age)*365
#print(age_in_days)

python_exp_in_years = input("Python tapasztalat években: ")

while True:
    dev_python_inp = input("Szeretné-e hogy a karaktere profi Python fejlesztő legyen? (yes/no)")
    if dev_python_inp in ["yes","no"]:
        break

if dev_python_inp == "yes":
    dev_python = "He/she wants to be a Python developer!"
else:
    dev_python = " He/she does not want to be a Python developer!"

print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience. {dev_python}")
