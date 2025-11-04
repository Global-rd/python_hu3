# Bekérjük a felhasználótól a várost és a lakbért
city = input("Kérlek add meg a várost: ")
rent = int(input("Kérlek add meg a havi lakbért USD-ben: "))
# Sara preferenciái
if city == "Chicago":
    decision = True
elif city == "New York" or city == "San Francisco":
    if rent < 4000:
        decision = True
    else:
        decision = False
elif city == "Washington":
    decision = False
else:
    if rent <= 3000:
        decision = True
    else:
        decision = False
# Printelem f-stringgel
if decision:
    print(f"Sarah beköltözne {city}ba, havi {rent} USD bérleti díjért")
else:
    print(f"Sarah nem költözne ide {city}ba, havi {rent} USD bérleti díjért.")