"""
homework_2
"""


name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: "))
python_experience = int(input("Enter your python_experiee: "))
age_in_days = age * 365
profi = input("Do you want your character to be a professional Python developer? (Yes/No): ").strip().title()
if profi not in ("Yes", "No"):# valid input
    print("Please answer with Yes or No.")
dev_message = "wants" if profi == "Yes" else "does not want"
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience} years experience. He/she {dev_message} to be a Python developer!")