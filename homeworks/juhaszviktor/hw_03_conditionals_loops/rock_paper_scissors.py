while True:
    max_circle = int(input ("Mennyi kört játszotok (páratlan számot adj meg): "))
    if max_circle %2 == 1:
        break

score1 = 0
score2 = 0
circle = 1

while circle <=3:
    print("")
    print(f"{circle}. kör, első játékos: {score1} pont, második játékos {score2} pont.")    
    while True:
        answ1 = input ("Első játékos mit választ (rock/paper/scissors)")
        if answ1 in ["rock", "paper", "scissors"]:
            break

    while True:
        answ2 = input ("Második játékos mit választ (rock/paper/scissors)")
        if answ2 in ["rock", "paper", "scissors"]:
            break

    if answ1 == answ2:
        print("döntetlen.")
    elif (answ1 == "rock" and answ2 == "paper") or \
        (answ1 == "paper" and answ2 == "scissors") or \
        (answ1 == "scissors" and answ2 == "rock"):
            score2 += 1
            circle += 1
            print("második játékos nyerte a kört.")
    elif (answ1 == "paper" and answ2 == "rock") or \
            (answ1 == "scissors" and answ2 == "paper") or \
            (answ1 == "rock" and answ2 == "scissors"):
            score1 += 1
            circle += 1
            print("első játékos nyerte a kört.")

print("Vége a játéknak, eredmények:")
print(f"Első játékos: {score1} pont, második játékos {score2} pont.")
if score1 > score2:
    print("Első játékos nyert!")
else:
    print("Második játékos nyert!")
print("Gratulálunk!")