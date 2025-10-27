name = input("Add meg a felhasználó nevét:").strip().capitalize()
age_inpt = input("Add meg a felhasználó életkorát (években):)")
python_exp = float(input("Add meg a Python tapasztalait:"))
age = int(age_inpt)
age_in_days = age * 365
print(f"A felhasználó neve: {name}")
print(f"A felhasználó {age_in_days} nap és {python_exp} év tapasztalat")
