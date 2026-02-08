city = input("Város amit választanál").strip()
price = int(input("Albérlet ára amerikai dollárban:").strip())

if city in ["New York" , "San Francisco"] and price < 4000: 
    print("Sarah kivesz egy lakást.")
elif city == "Washington":
    print(f"Sarah gyűlöli: {city}, és nem lakna ott.")
elif city == "Chicago":
    print(f"Sarah kedvence: {city}, és a pénz nem akadály, hogy ott lakjon.")
elif price <= 3000:
    print(f"Sarah elköltözne: {city}, mert megfelelő: {price} USD")
else:
    print(f"Sarah nem költözne: {city}, mert drága: {price} USD")