name = input("Enter your character's name: ").title().strip()
age_in_years = int(input("Enter your character's age: "))
age_in_days = age_in_years * 365
python_exp_in_years = int(input("Enter your character's Python experience in years: "))

result = input("Would your character like to become a professional Python developer? (Yes/No): ")
if result.lower() == "yes" or result.lower() == "y":
    python_will_pro = "Yes"
elif result.lower() == "no" or result.lower() == "n":
    python_will_pro = "No"
else:
    print("Invalid answer")

print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He/she " 
      + ("wants" if python_will_pro == "Yes" else "does not want") + " to be a Python developer!" )

