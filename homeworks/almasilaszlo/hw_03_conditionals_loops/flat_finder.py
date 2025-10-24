flat_prices={"New York":4000,"San Fransisco":4000,"Washington":0,"Chicago":float('inf')}
choosen_city=input("Where are you looking for a rent? : ")
rent_fee=int(input("How much does the rent cost?"))
#print(choosen_city)
limitprice=flat_prices.get(choosen_city, 3001)
#print(limitprice)
if rent_fee<limitprice:
    print(f"You can move in to {choosen_city} for {rent_fee} $/month")
else:
    print(f"You can't move in to {choosen_city} for {rent_fee}!")