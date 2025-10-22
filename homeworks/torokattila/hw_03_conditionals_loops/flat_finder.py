pref_town = ["New York","San Francisco"]
max_price = 4000

town = input("Add meg a várost:")
price = int(input("Lakbér($):"))

choice_msg = ""

if town in pref_town and price < max_price:
    choice_msg = "Kitűnő választás!"
elif town == "Washington":
    choice_msg = "Ezt semmi pénzért ne válaszd!"
elif town == "Chicago":
    choice_msg = "Chicago-ért bármit megadnék!"
elif price <= 3000:
    choice_msg = "Ezt érdemes megnézni! Olcsó!"
else:
    choice_msg = "Ebből még jó dolog is kisülhet!"

print(f"{town} városba, {price}$ a lakbér. Tanácsom: {choice_msg}")




