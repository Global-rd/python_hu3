#nev bekerese
name = input("What is your name?").upper().strip()

#eletkor bekerese atalakitasa napokban
age = int(input("How old are you?"))
age_in_days=age*365

#python tapasztalat evekben
#kicsit atalakitottam a szöveget azaz beletettem a days szot is
py_exp_in_year = int(input("How many years of Python experience do you have?")) 

#szeretne profi lenni
want_to_be_exp = input("Do you want to be a Python expert? (yes/no)").lower().strip()

# a mai ora utan a ternary operator
result="He/she wants to be a Python developer!" if want_to_be_exp=="yes" else "He/she doesn't want to be a Python developer!"

#eredmye kiiratasa
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {py_exp_in_year} years experience. {result}")