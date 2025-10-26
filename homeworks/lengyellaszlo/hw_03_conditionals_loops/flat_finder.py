# Szabályok
city_limits = {
    #5000: ["Boston"],
    4000: ["New York", "San Francisco"]
}

# never
forbidden = ["Washington"]

# always
any_price = ["Chicago"]

# város input
city = input("Enter the city name: ").strip().title()

# ár input validálással
attempts = 0
while attempts < 3:
    price_input = input("Enter the monthly rent (USD): ").strip()
    if price_input.isdigit():
        price = int(price_input)
        break
    else:
        attempts += 1
        print(f"Invalid input. Please enter a number. Attempts left: {3 - attempts}")
else:
    print("You entered an invalid price 3 times. Exiting.")
    exit()

# for-hoz input
thresholds = sorted(city_limits.keys(), reverse=True)

# never
if city in forbidden:
    print(f"You would never move to {city}.")

# always
elif city in any_price:
    print(f"You'd move to {city} at any price.")

# olcsó lakások
elif price <= min(thresholds):
    print(f"You can move to {city} for ${price} per month.")

# kivételek
else:
    for limit in thresholds:
        if price <= limit and city in city_limits[limit]:
            print(f"You can move to {city} for ${price} per month.")
            break
    else:
        print(f"You cannot move to {city} for ${price} per month.")
