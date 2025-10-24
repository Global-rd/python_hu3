#Bekéri hol szeretne lakni és mennyiért
city = input("Enter the city where you would like to rent a flat: ").strip().upper()
rent = int(input("Enter the expected monthly rent in USD: "))

#SARAH Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD havonta
if city in ["NEW YORK", "SAN FRANSISCO"] and rent < 4000: 
    able_to = True
# Gyűlöli Washington-t, és semmi pénzért nem lakna ott
elif city == "WASHINGTON":
    able_to = False
#Annyira imádja Chicago-t, hogy még a pénz sem akadály
elif city == "CHICAGO":
    able_to = True
# Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér
elif rent <= 3000:
    able_to = True
# Ha egyik fentebbi feltétel sem teljesül
else:
    able_to = False

# Eredmény kiíratása f-string segítségével
if  able_to:
    print(f"She is able to rent a flat in {city} for ${rent} per month.")
else:
    print(f"She isn't able to rent a flat in {city} for ${rent} per month.")
    