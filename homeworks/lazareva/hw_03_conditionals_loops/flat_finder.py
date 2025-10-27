"""
A program lakás keresésben segít dönteni Sarah-nak. 
A felhasználótól bekéri a várost és a lakbér árát.

Sarah elfogadja az ajánlatot abban az esetben, ha:
- a város New York vagy San Francisco, és az albérlet ára kevesebb, mint 4 000 USD.
- Chicago-t, bármilyen áron
- egyéb városokban, kivétel Washington, max. 3 000 USD lehet a lakbér.

Washington városba semmiképpen nem akar elköltözni Sarah.

Ezeket ellenőrzi a program, és a végén kiírja, hogy Sarah elfogadja-e az ajánlatot vagy sem.
"""

city = input("Enter the city where the flat is located: ").strip().title()
rent = float(input("Enter the rent price (in USD): "))

accept_offer = False

if city != "Washington":
    if (city == "New York" or city == "San Francisco") and rent < 4000:
        accept_offer = True
    elif city == "Chicago":
        accept_offer = True
    elif rent <= 3000:
        accept_offer = True

result = "accepted" if accept_offer else "not accepted"

print(f"Sarah has {result} the offer in {city} city with a rent of {rent} USD.")
