"""
homework_2
"""

my_attribution = {"name": "","age": 0,"python_experience": 0,"profi":""}
name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: "))
python_experience = int(input("Enter your python_experiee: "))
age_in_days = age * 365
profi = input("Do you want your character to be a professional Python developer? (Yes/No): ").strip().title()
if profi in ("Yes", "No"):# valid input
    pass
else:
    print("Please answer with Yes or No.")
dev_message = "wants to be" if profi == "Yes" else "does not want to be"
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience} years experience. He/she {dev_message} a Python developer!")
