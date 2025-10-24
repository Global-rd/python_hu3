# A felhasználótól bekérdbekérem a következő input-okat:
first_name = input("Add meg a kersztneved: ")
last_name = input("Add meg a vezetékneved: ")
full_name = (first_name.strip() + " " + last_name.strip())
age = input("Add meg az életkorod (számmal): ")
python_exp = input("Add meg a Python tapasztalalatod években: ")

# type conversion
age = int(age)
python_exp = int(python_exp)

# feltételezem, hogy ma van a születésnapja
age_in_days = age * 365

print(f"My character is {age_in_days} old.")
print(f"His/her name is {full_name.title()}and he/she has {python_exp} in years experience.")