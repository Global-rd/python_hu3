#input bekérések, ahol szükséges kötött fromával
name = input("Enter your name:")
age = int(input("Enter your age:"))
py_experience = int(input("Enter your years of Python experience:"))

#dátum számolás csak évekre, most nem kell napokat figyelembe venni...+ fölösleg levágása és nagybetűsítés nyelvhelyesség miatt
age_in_days = age * 365
name_capitalized = name.title().strip()
name = name_capitalized

#csak ternary operátort használva
py_dev_or_not = input("Do you want to be a Python developer? (yes/no):")
be_dev_yes_not = "He/she wants to be a Python developer!" if py_dev_or_not.lower().strip() == "yes" else "He/she does not want to be a Python developer."

#f string összeállítása
information = f"My character is {age_in_days} days old, His/her name is {name} and he/she has {py_experience} years of Python experience. {be_dev_yes_not}"
print(information)

