from datetime import date
age=int(input("How old are you?"))
#print(age)
dummy_days= age*365
#print(dummy_days)

""" Ez kicsit pontosabb lehet a szökőévek miatt.
actual_date=date.today()
birth_year=date.today().year-age
birth_month=date.today().month
birth_day=date.today().day
birth_date=date(birth_year,birth_month,birth_day)
#print(birth_date)
accurate_days=(actual_date-birth_date).days
print(accurate_days)
"""
fullname=input("Who the hell are you?").upper().strip()
#print(fullname)
python_exp=int(input("How long have you been working with pyton (in years)?" ))
#print(python_exp)
#javasolt megoldás:
profi=(input("Wana be a pro pyhton developer? (YES/NO)")).upper()
answ= "want" if profi=="YES" else "don't want" #ez a jól látom case sensitive, lehet úgy csinálni, hogy ne legyen az?
intro= f"My character is {dummy_days} days old. His name is {fullname} and he has {python_exp} years experience. He {answ} to be a pro python developer!! "
print(intro)
