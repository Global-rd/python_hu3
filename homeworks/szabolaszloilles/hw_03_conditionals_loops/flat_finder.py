cities = input("Please give me the city name: ").upper().strip()
rent = int(input("Please give me the monthly rent: $ "))

if cities == "CHICAGO":
    print(f"You can move in to the flat located in {cities} for a monthly rent of $ {rent}.")

elif cities == "NEW YORK" or "SAN FRANCISCO" and rent <4000: 
    print(f"You can move in to the flat located in {cities} for a monthly rent of $ {rent}.")

elif rent <= 3000:
    print(f"You can move in to the flat located in {cities} for a monthly rent of $ {rent}.")

elif cities == "WASHINGTON":
    print(F"You do not want to move to a flat located in {cities}.")

else:
    print(f"There are no available flats for you in {cities} with the given conditions.")