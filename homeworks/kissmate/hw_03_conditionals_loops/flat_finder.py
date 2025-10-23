cities = input("Enter city names separated by commas: ").split(",")
if any(city.strip() in [ "Chicago"] for city in cities):
    print(f"You have selected Chicago.")
budget = float(input("Enter your budget: "))
if any(city.strip() in ["New York", "San Francisco"] for city in cities) and budget >= 4000:
    print(f"You can afford to live in one of the selected cities.")
else:
    print(f"Consider looking for cities with a lower cost of living.")

