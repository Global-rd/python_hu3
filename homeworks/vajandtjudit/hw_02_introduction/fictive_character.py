name = input("")
age = input("")
python_exp = input("")
name = name.strip().capitalize()
age = int(age)
age_in_days = age * 365
python_exp = float(python_exp)
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp} years experience.")
