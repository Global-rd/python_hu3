# Second a. Homework

user_name = input("User name: ").strip().upper()


user_age = int(input("Age of User in years: "))

user_age_itg_days = user_age*365

pyth_exp = input("How many years of the experience of Python: ")

answer = input(" Do you want to be a Python expert? (yes/no)")

message=f"My character is {user_age_itg_days} old in days. My name is {user_name} and I have {pyth_exp} year(s) experience in Python."


if answer == "yes":
    print(f"I want to be a Python developer! ")
elif answer =="no":
     print(f"I don't want to be Python developer! ")
else :
      print(f"I really don't know what i want about the Python yet. ")

print(message)