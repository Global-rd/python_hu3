# Bekérjük a felhasználótól a várost és a lakbért
city = input("Kérlek add meg a várost: ")
rent = int(input("Kérlek add meg a havi lakbért USD-ben: "))
# Sara preferenciái
decision = (
    city == "Chicago"
    or (city in ("New York", "San Francisco") and rent < 4000)
    or (city not in ("Washington", "New York", "San Francisco", "Chicago") and rent <= 3000)
    )
# Printelem f-stringgel
if decision:
    print(f"Sarah beköltözne {city}ba, havi {rent} USD bérleti díjért")
else:
    print(f"Sarah nem költözne ide {city}ba, havi {rent} USD bérleti díjért.")