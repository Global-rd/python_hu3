
DAYS_OF_YEAR = 365

# Input data request

name = input("Enter your name: ")
age = input("Enter your age: ")
python_exp_in_years = input ("Enter your Python experience (year): ")

# Extra question
pro_dev = input("Do you want to become a professional python developer (yes/no)? ")

# Variables conversion

name = name.strip().upper()
age_in_days = int(age) * DAYS_OF_YEAR

# Display results 

print(f"My charcter is {age_in_days} old. His/her name {name} and he/she has {python_exp_in_years} years experience.")
print("He/she wants to be a Python developer!" if pro_dev == 'yes' else "He/she does not want to be a Pyton developer")

