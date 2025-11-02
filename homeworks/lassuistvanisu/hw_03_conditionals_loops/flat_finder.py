print("Sarah is looking for an apartment. Please send her your offers!")

order_city = input("Please specify in which city you recommend renting a flat: ")
price =int(input("Please specify the rent for the flat.: $"))

#Nagyon szereti - New York, San Fransisco - ára kevesebb mint 4000 USD havonta.
if order_city == "new york" or order_city == "san francisco" and price < 4000:
    print(f"The {price}$ is good. Let's go {order_city}!")
#Gyűlöli Washington-t, nem lakna ott
elif order_city == "washington":
    print(f"I'm sorry, I don't want to live in {order_city}")
#Imádja, Chicago, bármmennyi
elif order_city == "Chicago":
     print(f"I like {order_city}! Let's go!")
#Más helyről, 3000 USD vagy ez alatti
else:
    if price < 3000:
        print(f"Sara would like to move to {order_city} and the {price}$ is good. Let's go!")
    else:
        print(f"Keep searching. Thank you!")
