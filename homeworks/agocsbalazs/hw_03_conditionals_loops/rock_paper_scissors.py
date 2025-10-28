#kő, papír olló játék

#hány kört akarunk játszani és nem lehet csak páratlan a szám, hogy ne legyen döntetlen
while True:
    rounds = input("How many rounds do you want to play (odd number only)? ")
    if rounds.isdigit() and int(rounds) % 2 == 1:
        rounds = int(rounds)
        break
    print("Invalid input. Please enter an odd number.")

#mik lehetnek a válaszok, írjuk ki a felhasználónak
valid_answers = ["rock", "paper", "scissors"]
print("Valid answers are: Rock, Paper, Scissors")

#playerek pontszámai 0-ról indulnak
player1_wins=0
player2_wins=0

#cikliba kell tenni, hogy végig menjen a megadott körök számáig, rossz választ visszadobja
#és a döntetleneket újrajátssza, egyébként pedig növeli a pontszámot a győztesnek vagy a megfelelő üzenetet kiírja
for i in range(1,rounds +1):
    print(f"Round {i}:")
    
    while True:

        #első játékos választása, amíg rosszat ad visszadobja
        while True:
            player1 = input("Player 1 move (rock,paper,scissors): ").strip().lower()
            if player1 in valid_answers:
                break
            print("Invalid move. Please enter a valid answer.")

        #második játékos választása, amíg rosszat ad visszadobja
        while True:
            player2 = input("Player 2 move (rock,paper,scissors): ").strip().lower()
            if player2 in valid_answers:
                break
            print("Invalid move. Please enter a valid answer.")

        #döntetlen
        if player1 == player2:
            print("It's a tie! Replay the round.")
            continue
        
        #győztes kalkulálás és pont számolás
        #kő üti az ollót, papír a követ, olló a papírt
        if (player1 == "rock" and player2 == "scissors") or \
            (player1 == "paper" and player2 == "rock") or \
            (player1 == "scissors" and player2 == "paper"):
            print("Player 1 wins this round!")
            player1_wins += 1  
            break
        else:
            print("Player 2 wins this round!")
            player2_wins += 1
            break



    print(f"Score: Player 1 - {player1_wins}, Player 2 - {player2_wins}")

    #végső győztes kiírása
if player1_wins > player2_wins:
    print(f"Player 1 wins the game with a score of {player1_wins} to {player2_wins}!")
else:
    print(f"Player 2 wins the game with a score of {player2_wins} to {player1_wins}!")

