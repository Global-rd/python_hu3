location = input ("Please write the city: ")
price = int(input("Please write your price: "))

if location == "Washington":
    print("No way, you hate this city and you know it.")

elif (location == "New York" or location =="San Francisco") and price < 4000:
        print(f"Welcome to {location} and you monthly fee will be {price} USD")

elif location == "Chicago":
        print("You are welcome to Chicago baby, definitely you can afford it.")

elif price < 3000:
        print (f"Welcome to {location} and you monthly fee will be {price} USD")

else:
    print(f"No flat available with your parameters. Good bye")