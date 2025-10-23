city = input("Preferált város: ").strip()
rent = int(input("Maximum lakbér: ").strip())

if city == "New York" or city == "San Francisco" and rent <= 4000:
    print(f"Ezekkel a feltételekkel {city} városban, ${rent} áron ki tudod venni a lakást.")
elif city == "Chicago":
    print(f"Ezekkel a feltételekkel {city} városban, ${rent} áron ki tudod venni a lakást.")
elif city == "Washington":
    print(f"{city} városba semmilyen esetben ne költözz!")
elif rent <= 3000:
    print(f"Ezekkel a feltételekkel {city} városban, ${rent} áron ki tudod venni a lakást.")
else:
    print(f"Ezekkel a feltételekkel {city} városban, ${rent} áron nem tudsz kivenni lakást")