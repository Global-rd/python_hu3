city = input("Kélek, adj be egy város nevet: ").strip().title()

rent = int(input("Kérlek, add meg a bérleti díj maximális összegét: "))

if city in ["New York", "San Francisco"]:
    if rent < 4000:
        can_move = True

    else:
        can_move = False

elif city == "Washington":
    can_move = False
elif city == "Chicago":
    can_move = True
else:
    if rent <= 3000:
        can_move = True
    else:
        can_move = False

result = "beköltözne" if can_move else "nem költözne be"

print(f"Sarah {city}-ba, ${rent} lakbér esetén {result}.")
