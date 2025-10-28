city = input("City: ")
rent = float(input("Monthly rent (USD): "))

city = city.lower()


if city == "chicago":
    move = True
elif city == "washington":
    move = False
elif city == "new york" or city == "san francisco":
    move = rent < 4000
else:
    move = rent <= 3000

if move:
    print(f"Sarah would move to {city.title()} for {rent:.0f} USD/month.")
else:
    print(f"Sarah would NOT move to {city.title()} for {rent:.0f} USD/month.")