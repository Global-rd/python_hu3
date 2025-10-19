
# Ask the user for input data
name = input("Enter your character's name: ")
age_str = input("Enter your character's age (in years): ")
python_experience_str = input("Enter Python experience (in years): ")

wants_to_be_pro = input("Does your character want to be a professional Python developer? (y/n): ")

# Format the name: remove extra spaces and capitalize the letters
name = name.strip().upper()

# Convert age to integer and calculate age in days
age = int(age_str)
age_in_days = age * 365  # Assuming today is the character's birthday

# Convert Python experience to float
python_experience = float(python_experience_str)

# Ternary operator to determine developer ambition
developer_message = "He/she wants to be a Python developer!" if wants_to_be_pro.lower() == "y" else "He/she does not want to be a Python developer!"

# Print the result using an interpolated string
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience} years experience. {developer_message}")