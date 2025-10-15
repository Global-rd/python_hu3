name = input("Your name: ").upper().strip()
age = int(input("Your age in years: ").strip())
age_in_days = age * 365
py_experience = int(input("Your experience with python in years: ").strip())
wants_to_be_dev = input("Do you want to be a developer? Type Y for yes and N for no: ").upper().strip()
string_dev = "He/she wants to be a developer" if (wants_to_be_dev == "Y") else "He/she does not want to be a developer"

character = {
    "name": name,
    "age": age,
    "age_in_days": age_in_days,
    "py_experience": py_experience,
}

print(f"My character is {character["age_in_days"]} days old. His/her name is {character["name"]} and he/she has {character["py_experience"]} years of experience. {string_dev}")
