city = input("In which city is the apartment located?").strip().title()
price = int(input("What is the price in US$"))

#print(city)
#print(price)

if city in ["New York","San Fransisco"] and price < 4000:
    print(f"Good conditions. The apartment is in {city} and it costs ${price}")
elif city == "Washington":
    print("Not inetrested in the city.")
elif city == "Chicago":
    print(f"She loves Chicago, the price is ${price}")
elif price <= 3000:
    print(f"Good conditions. The apartment is in {city} and it costs ${price}")
else :
    print(f"The price is too high. It is ${price}.")
