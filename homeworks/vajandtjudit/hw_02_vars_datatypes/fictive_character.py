name = input("Add meg a felhasználó nevét:")
age_inpt = input("Add meg a felhasználó életkorát (években):)")
python_exp = float(input("Add meg a Python tapasztalait:"))
name = name.strip().capitalize()
age = int(age_inpt)
age_in_days = age * 365
print(f"A felhasználó neve: {name}")
print(f"A felhasználó {age_in_days} nap és {python_exp} év tapasztalat")
