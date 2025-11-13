city = input("Enter the city: ").strip().lower()
rent = float(input("Enter the monthly rent in USD: "))


if city == "washington":
    decision = False
elif city == "chicago":
    decision = True
elif city in ["new york", "san francisco"]:
    decision = rent < 4000
else:
    decision = rent <= 3000

print(f"Sarah {'can' if decision else 'cannot'} move to {city.title()} with a rent of ${rent:.2f}/month.")
