city = input("Add meg a várost: ")
fee = int(input("Add meg a havi lakbér árát (USD): "))


if city == "Chicago":
    can_move = True
    reason = "mert szereti Chicago-t és bármi áron odaköltözne"
elif city == "Washington":
    can_move = False
    reason = "mert nincs az a pénz, amiért Washington-ba költözne"
elif city == "New York" or city == "San Francisco":
    if fee < 4000:
        can_move = True
        reason = f"mert szereti {city}-t és a lakbér ({fee} USD) kevesebb mint 4000 USD"
    else:
        can_move = False
        reason = f"mert bár szereti {city}-t, a lakbér ({fee} USD) nem kevesebb mint 4000 USD"
else:
    if fee <= 3000:
        can_move = True
        reason = f"mert a lakbér ({fee} USD) legfeljebb 3000 USD"
    else:
        can_move = False
        reason = f"mert a lakbér ({fee} USD) meghaladja a 3000 USD-t"


if can_move:
    print(f"Sarah be tud költözni {city}-ba/be, {reason}.")
else:
    print(f"Sarah NEM tud beköltözni {city}-ba/be, {reason}.")