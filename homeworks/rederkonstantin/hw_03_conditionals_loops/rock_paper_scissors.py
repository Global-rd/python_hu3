"""
Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos
között. Aprogram kérje be, hogy hány kört akarnak játszani a játékosok. 
Figyelj oda, hogy olyan számot kell megadnia a felhasználónak ami mellett nem
tudnak döntetlent játszani! Ha nem ilyen számot ad meg, írj ki hibaüzenetet 
és addig kérd be újra a körök számát amíg páratlan számot nem ad meg. Ezután
a program felváltva kérje be az első és második játékos válaszát, ami 
kizárólag a következő stringek valamelyik lehet: "rock", "paper", "scissors".
Ellenkező esetben kezeld úgy a hibát ahogy a körök számánál. Egy adott kör 
addig ne érjen véget, amíg valaki nem nyer (döntetlen esetén az adott kört 
újra kell játszani). Tárold a nyertesek pontjait, és minden kör végén növeld 
az aktuális játékos pontszámát. A végén printeld ki ki nyert, és hány ponttal.
"""

# ████████████████████████████████████████████████████████████████████████████

print("")
print("This is a rock, paper, scissors game. Enjoy it! :)")
print("")

# Main cycle
while True:
    # Number of games

    # eredeti kód rész
    #while True:
    #    rounds = int(input("How many games would you like to play? "))
    #    if rounds % 2 == 0:
    #        print("Please give odd number.")
    #        continue
    #    break

    # Javasolt kódrész
    while True:
        rounds = int(input("How many games would you like to play? "))
        if rounds % 2 != 0:
            break
        print("Please give an odd number.")
    print("")

    # input player names
    possible_answers = ["rock", "paper", "scissors"]
    player_a = input("Please give name of player A: ")
    print("")
    player_b = input("Please give name of player B: ")
    print("")

    # votes
    print("Please use this words exactly to give your choice: ")
    print("rock", "paper", "scissors")
    print("")

    # counters init
    credit_counter_a = int(0)
    credit_counter_b = int(0)
    round_counter = int(0)
    
    # game cycle

    # cycle counter
    while round_counter != rounds:
        choice_a = input(f"{player_a}, please give your choice: ")
        while choice_a not in possible_answers:
            choice_a = input(f"{player_a}, please give correct choice: ")

        choice_b = input(f"{player_b}, please give your choice: ")
        while choice_b not in possible_answers:
            choice_b = input(f"{player_b}, please give correct choice: ")

        # logic of winner

        # same choice checker

        # eredeti kód, jajjj...... :D
        #if ((choice_a == "rock" and choice_b == "rock") or 
        #    (choice_a == "paper" and choice_b == "paper") or
        #    (choice_a == "scissors" and choice_b == "scissors")):
        
        # Javasolt kód! as simple as possible.... :)
        if choice_a == choice_b:
            print("Same choice, give choice again. :)")

        # win chouce counter
        elif ((choice_a == "rock" and choice_b == "paper") or 
            (choice_a == "paper" and choice_b == "scissors") or
            (choice_a == "scissors" and choice_b == "rock")):
            credit_counter_b += 1
            round_counter += 1
        else:
            credit_counter_a += 1
            round_counter += 1

        # not print points if game is end
        if round_counter != rounds:
            print(f"{player_a}/{player_b} :\
                {credit_counter_a}/{credit_counter_b}")

        # winner checker
        if credit_counter_a + credit_counter_b == rounds:
            if credit_counter_a > credit_counter_b:
                print("")
                print(f"Winner is {player_a}!")
            else:
                print("")
                print(f"Winner is {player_b}!")
            print(f"{player_a}/{player_b} :\
                {credit_counter_a}/{credit_counter_b}")
                
    # counters reset
    credit_counter_a = int(0)
    credit_counter_b = int(0)
    round_counter = int(0)

    # next game question
    print("")
    if input("Woul you like to one more game? (y/n)") == "y":
        continue
    else:
        print("")
        print("Have nice day or night and have good life!")
        print("")
        break