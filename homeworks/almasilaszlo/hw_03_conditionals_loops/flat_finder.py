flat_prices={"New York":"4000","San Fransisco":"4000","Washington":"0","Chicago":"9999999999"}
choosen_city=input("Where are you looking for a rent? : ")C
rent_fee=input("How much does the rent cost?")
print(choosen_city)
if choosen_city not in flat_prices.keys():
    limitprice=3001
else:
     limitprice= flat_prices.get(choosen_city)
print(limitprice)
if rent_fee<limitprice:
    print(f"You can move in to {choosen_city} for {rent_fee} $/month")
else:
    print(f"You can't move in to {choosen_city} for {rent_fee}!")