#Help for Sarah to find her flat

"""
1. She likes very much : New York, San Francisco
maximum rental fee is 4.000 USD/month

2. She hates Washington
not accepted rental fee limit

3.She adores Chicago
no rental fee limot

4.Other places
max. rental fee 3.000 USD
"""

city_name = input("Please give me the name of the city: ").strip().upper()
print(city_name)
monthly_fee = input("Please give me the monthly rental fee of this flat: ")
f=int(monthly_fee)

print(monthly_fee)
print(f)

if city_name == "WASHINGTON":
    print(f"SARAH HATES WASHINGTON !")
elif city_name =="CHICAGO":
     print(f"SARAH ADORES CHICAGO! She can accept the offer at {f} USD/month")
elif (city_name== "NEW YORK" or "SAN FRANCISCO") and (f<4000):
    print(f"SARAH LIKES {city_name} She can accept the offer at {f} USD/month")
else : print(f"The rental fee  {f} is too high in {city_name}")
#else : print("test")