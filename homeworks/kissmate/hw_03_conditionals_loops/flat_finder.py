cities = input("Enter city names separated by commas: ").split(",")
if any(city.strip() in [ "Washington"] for city in cities):
    print(f"Sarah don't want to be live in Washington.")
if any(city.strip() in [ "Chicago"] for city in cities):
    print(f"Sarah definitly like that place.")
budget = float(input("Enter your budget: "))
if any(city.strip() in ["New York", "San Francisco"] for city in cities) and budget >= 4000:
    print(f"Sarah will be happy to enter this citytis for that price.")
if budget >= 3000:
    print(f"Sarah good with this choice.")


