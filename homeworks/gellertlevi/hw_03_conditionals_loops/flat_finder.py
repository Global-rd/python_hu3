flat_price = float(input("Enter the price of the flat in Dollars: "))

if flat_price < 3000:
    print(f"The price is lower than 3000 dollars, for this price you can move anywhere.")
else:
    location = input("Enter the location of the flat: ").lower()

    if location == "washington":
        print(f"You hate {location}, do not move there!")
    elif location == "chicago":
        print(f"You love {location}, so move there whatever it takes!")
    elif "flat_price" < 4000 and (location == "new york" or location == "los angeles"):
        print(f"The flat is suitable for you because it is located in {location} and costs {flat_price} dollars.")
    else:
        print(f"The flat in is not suitable for you.")

