city = input("Add meg a várost: ")
rent = int(input("Add meg az albérlet havi árát USD-ben: "))
if (city == "New York" or city == "San Francisco") and rent < 4000:
    print("Sarah ki fogja venni a lakást!")
elif city == "Washington":
    print(f"Sarah gyűlöli {city}, és semmi pénzért nem lakna ott!")
elif city == "Chicago":
    print(f"Sarah imádja {city}, és bármit megadna, hogy ott lakhasson!")
elif rent < 3000:
    print(f"Sarah kiköltözne {city}-ba, mert az ár elfogadható: {rent} USD.")
else:
    print(f"Sarah nem költözne {city}-ba, mert túl drága ({rent} USD).")
