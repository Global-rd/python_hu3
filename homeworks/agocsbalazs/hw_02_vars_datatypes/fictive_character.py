#input bekérések, ahol szükséges kötött fromával
name = input("Enter your name:").title().strip()
age = int(input("Enter your age:"))
py_experience = int(input("Enter your years of Python experience:"))

#dátum számolás csak évekre, most nem kell napokat figyelembe venni...+ fölösleg levágása és nagybetűsítés nyelvhelyesség miatt
age_in_days = age * 365

#csak ternary operátort használva
py_dev_or_not = input("Do you want to be a Python developer? (yes/no):").lower().strip()
be_dev_yes_not = "wants" if py_dev_or_not == "yes" else "does not"

#f string összeállítása
information = f"My character is {age_in_days} days old, His/her name is {name} and he/she has {py_experience} years of Python experience.  He/She {be_dev_yes_not} want to be a Python developer."
print(information)

