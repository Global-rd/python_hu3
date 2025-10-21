
#ADATBEKÉRÉSEK ÉS ELTÁROLások
#név adat
user_name = input("Whats your name ?")
name = user_name.title()

#kor  átalakítva napokra
age = int(input("How old are you?"))
age_in_days = age * 365

#év adat
python_exp_in_years = int(input("How many years of experience do you have in Python?"))

#szorgakmi
extra = input("Would you like to become a professional Python developer? yes or no?")

#VÁLASZOK
#válaszok előkészítése
result_developer = f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He/she wants to be a Python developer!"
result_no_developer = f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience.He/she does not want to be a Python developer!"
result = result_developer if str(extra) == "yes" else result_no_developer  

#FELADAT MEGOLDÁSA
print(result)

