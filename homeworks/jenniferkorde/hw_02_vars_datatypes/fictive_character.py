first_name = input("First name: ").strip().upper()
last_name =input("Last name: ").strip().upper()
age_years  = int(input("Age (in years): ").strip())
python_exp_in_years = int(input("Python exp (years): ").strip())
wants_dev = input("Do you want the character to be a Python developer? (yes/no): ").strip().lower()

full_name  = f"{first_name} {last_name}"
age_in_days = age_years * 365

print(
    f"My character is {age_in_days} days old. "
    f"His/her name is {full_name} "
    f"and he/she has {python_exp_in_years} years experience. "
    f"{(
        'He/she wants to be a Python developer!'
        if wants_dev == 'yes'
        else 'He/she does not want to be a Python developer!'
    )}"
)








