# flat_finder

town_name = input("Dear Sarah. Please type in the town name: ").title()                                         # nagybetűs lesz
rent_price = int(input("Give me the max rent price $: ")) if town_name not in ["Chicago", "Washington"] else 0  # csak ha kell
   
if town_name == "Chicago":
    print(f"{town_name} is Your favourite town. Move there!") 
elif town_name == "Washington":
    print(f"You hate {town_name}. You should nevr move there!")
elif (town_name in ["New York", "San Francisco"] and rent_price < 4000) or (town_name not in ["New York", "San Francisco"] and rent_price <= 3000): 
    print(f"{rent_price} $ is good offer for You to move in {town_name}!")
else:
    print(f"Unfortunetly {rent_price} $ is too much for You to move in {town_name} :(")
