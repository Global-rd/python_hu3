# A felhasználótól bekérdbekérem a következő input-okat:
first_name = input("Add meg a kersztneved: ").strip()
last_name = input("Add meg a vezetékneved: ").strip()
full_name = f"{first_name} {last_name}".title()
age = int(input("Add meg az életkorod (számmal): "))
python_exp = input("Add meg a Python tapasztalalatod években: ")
# type conversion
python_exp = int(python_exp)
# feltételezem, hogy ma van a születésnapja
age_in_days = age * 365
print(f"My character is {age_in_days} old.")
print(f"His/her name is {full_name.title()} and he/she has {python_exp} in years experience.")