name = input("what is your name?: ")
age = input("How old are you?: ")
python_experience = input("How long do you work with Python (in years): ")
age = int(age)
python_experience = int(python_experience)
age_in_days = age * 365
name = name.strip().upper()
career = input("Do you want to be a pro Python developer (yes/no)?: ")
if career.lower() == "no" :  
 print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience} years experience. He/she does not want to be a Python developer!")
elif career.lower() == "yes":
 print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience} years experience. He/she wants to be a Python developer!")
else:
 print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience} years experience.")
