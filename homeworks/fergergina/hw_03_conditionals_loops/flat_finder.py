city = input("Please provide the city: ")
rent = int(input("Please provide the rent: "))

if (city == "Chicago"):
    print(f"You can move in to {city} for {rent}")
elif (city == "Washington"):
    print(f"You can't move in to {city} for {rent}")
elif (city == "New York" or city == "San Francisco") and rent < 4000:
    print(f"You can move in to {city} for {rent}")
elif (rent <= 3000):
    print(f"You can move in to {city} for {rent}")
else:
    print(f"You can't move in to {city} for {rent}")
