possible_answers = ["yes", "no"]

nev = input("Name: ").strip().upper()
age = int(input("Age: "))
python_experience = int(input("Python experience (in years): "))
wants_to_be_a_prof_dev=(input("Do you want to be a professional python developer? (yes or no): "))

if wants_to_be_a_prof_dev not in possible_answers:
    print("I said yes or no! Please retry!")
    exit()
want_or_not = "wants" if wants_to_be_a_prof_dev == 'yes' else "does not want"

age_in_days =age * 365
print(f"My character is {age_in_days} days old.His/Her name is {nev} and he/she has {python_experience} years experience.He/she {want_or_not} to be a Python developer!")

