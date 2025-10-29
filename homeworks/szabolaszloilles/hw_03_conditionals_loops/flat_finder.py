city = input("Please give me the city name: ").upper().strip()
rent = int(input("Please give me the monthly rent: $ "))

if city == "CHICAGO":
    print(f"You can move in to the flat located in {city} for a monthly rent of $ {rent}.")

elif city == "NEW YORK" or city =="SAN FRANCISCO" and rent <4000: 
    print(f"You can move in to the flat located in {city} for a monthly rent of $ {rent}.")

elif rent <= 3000:
    print(f"You can move in to the flat located in {city} for a monthly rent of $ {rent}.")

elif city == "WASHINGTON":
    print(F"You do not want to move to a flat located in {city}.")

else:
    print(f"There are no available flats for you in {city} with the given conditions.")