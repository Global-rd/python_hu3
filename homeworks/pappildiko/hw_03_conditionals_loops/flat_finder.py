while True:
    city = input("Give me the name of the city in which the flat is: ").strip().title()
    if city == "":
        print("Please enter a valid city name (not empty).")
    elif city.isdigit():
        print("Please enter a valid city name (not a number).")
    else:
        break


while True:
    user_input = input("Enter rental price: ").strip()
    if user_input.replace('.', '', 1).isdigit():
        rental_price = float(user_input)
        if rental_price > 0:
            break
        else:
            print("The price must be greater than 0.")
    else:
        print("Please enter a valid number (e.g. 1200 or 1200.50).")


if city in ["New York", "San Francisco"] and rental_price < 4000 :
    print(f"Sarah would like to rent the appartement in {city} for $ {rental_price:.2f}.")
elif city in ["Chicago"]:
    print(f"Sarah would like to rent the appartement in {city} for $ {rental_price:.2f}.")
elif city in ["Washington"]:
    print(f"Sarah would not like to rent the appartement in {city} for $ {rental_price:.2f}.")
elif rental_price <= 3000:
    print(f"Sarah would like to rent the appartement in {city} for $ {rental_price:.2f}.")
else: 
    print(f"Sarah would not like to rent the appartement in {city} for $ {rental_price:.2f}.")
