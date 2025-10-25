# Task 01

"""
I use constants and set data types for easier modification later on,
but I don't allow changes during runtime and there is no implementation for
changes.
"""

LIKED_CITIES = {"new york", "san francisco"}
HATED_CITIES = {"washington"}
LOVED_CITIES = {"chicago"}

# I remove unnecessary spaces from the input, and if the value is not empty, I do not ask for it again.
while True:
    city = input("Please enter city: ").strip()
    if city != "":
        break

"""
I remove unnecessary spaces from the input, and if the value only contains numbers and
the int() conversion is greater than zero, I do not ask the user to re-enter it.
Unfortunately, based on what I have learned, I have not found a solution that would allow me to accept the float type as well.
Many people suggested using try, but we haven't learned that yet, and I didn't want to mix in things we haven't learned.
"""

while True:
    rent_price = input("Please enter rent price: $ ").strip()
    if rent_price.isnumeric() and int(rent_price) > 0:
        break

"""
I used the .lower() method to perform the comparison so that upper and lower case letters
would not interfere with the comparison.
When writing the output, my goal with the .title() method was to ensure that even if the user entered the city name incorrectly,
it would still appear correctly and work even for cities with multiple words, such as New York.
"""
if city.lower() in HATED_CITIES:
    print(f"Sarah, you hate {city.title()}, you do not want to move there.")
elif city.lower() in LOVED_CITIES:
    print(
        f"Sarah, you find your flat in one of your loved city in {city.title()}. You can move there."
    )
elif city.lower() in LIKED_CITIES and int(rent_price) < 4000:
    print(
        f"Sarah, you find a good flat in {city.title()} for USD {rent_price}. You can move there."
    )
elif int(rent_price) <= 3000:
    print(
        f"Sarah, you find a good flat in {city.title()} for USD {rent_price}. You can move there."
    )
else:
    print(
        f"Sarah, you did not find a suitable flat in {city.title()} at now. Please try again later."
    )
