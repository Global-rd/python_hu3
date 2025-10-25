# Second a. Homework

user_name = input ("User name: ")
user_name = user_name.strip()
upper_user_name = user_name.upper()

user_age = input("Age of User in years: ")
user_age_itg_years = int(user_age)
user_age_itg_days = int(user_age_itg_years)*365

pyth_exp = input("How many years of the experience of Python: ")

answer = input(" Do you want to be a Python expert? (yes/no)")

if answer == "yes":
    print(f"My character is {user_age_itg_days} old in days. My name is {upper_user_name} and I have {pyth_exp} year(s) experience in Python. I want to be a Python developer! ")
elif answer =="no":
     print(f"My character is {user_age_itg_days} old in days. My name is {upper_user_name} and I have {pyth_exp} year(s) experience in Python. I don't want to be Python developer! ")
else :
      print(f"My character is {user_age_itg_days} old in days. My name is {upper_user_name} and I have {pyth_exp} year(s) experience in Python. I really don't know what i want about the Python yet. ")
