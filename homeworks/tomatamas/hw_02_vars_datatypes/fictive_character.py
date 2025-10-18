name = input("Your name: ").upper().strip()
age = int(input("Your age in years: ").strip())
age_in_days = age * 365
py_experience = int(input("Your experience with python in years: ").strip())
dev_intent = input("Do you want to be a developer? Type Y for yes and N for no: ").upper().strip()
string_intent = "wants" if (dev_intent == "Y") else "does not want"

character = {
    "name": name,
    "age": age,
    "age_in_days": age_in_days,
    "py_experience": py_experience,
}

print(f"My character is {character["age_in_days"]} days old. His/her name is {character["name"]} and he/she has {character["py_experience"]} years of experience. He/she {string_intent} to be a developer.")
