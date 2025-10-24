#rock_paper_scissors

# Bekéri a 1-es játékos nevét és üres név esetén hiba
player_1_name = input("Enter Player 1's name: ").strip().title()
while player_1_name == "":
    print("Error: Please enter a valid name.")

# Bekéri a 2-es játékos nevét és üres név esetén hiba
player_2_name = input("Enter Player 2's name: ").strip().title()
while player_2_name == "":
    print("Error: Please enter a valid name.")

#Körök száma , de csak páratlan értékeket fogad el
while True:
    rounds_played = int(input("How many rounds do you want to play? (Must be an odd number): "))
    if rounds_played % 2 == 1:
        break
    print("Please enter an odd number and try again.")

# játékosok pontjainak inicializálása
player_1_score = 0
player_2_score = 0

#Kezdés
print("-------------------------------------------------------------")
print(F"GAME IS COMMING ...  {rounds_played} ROUNDS: {player_1_name} vs. {player_2_name}!")

# megfelelő kézjelek listája
hand_sign = ["rock", "paper", "scissors"]
for round in range(1, rounds_played + 1):
    print("-------------------------------------------------------------")
    print(F"ROUND: {round}!")
    print("-------------------------------------------------------------")
    # Kézjelek 1 játékosnál, érvénytelen esetén újra
    player_1_hand = input(F"{player_1_name}, enter your hand sign (rock, paper, scissors): ").strip().lower()
    while player_1_hand not in hand_sign:
        print("Invalid!!!! Please try again.")
        player_1_hand = input(F"{player_1_name}, enter your hand sign (rock, paper, scissors): ").strip().lower()
    
    # Kézjelek 2 játékosnál, érvénytelen esetén újra
    player_2_hand = input(F"{player_2_name}, enter your hand sign (rock, paper, scissors): ").strip().lower()
    while player_2_hand not in hand_sign:
        print("Invalid!!!! Please try again.")
        player_2_hand = input(F"{player_2_name}, enter your hand sign (rock, paper, scissors): ").strip().lower()

    # eredmény meghatározása,ha döntetlen
    if player_1_hand == player_2_hand:
        print("-------------------------------------------------------------")
        print("Tie!!! Play again.")

    #amikor az 1-es játekos nyer, megadva a pontot
    elif (player_1_hand == "rock" and player_2_hand == "scissors") or (player_1_hand == "paper" and player_2_hand == "rock") or (player_1_hand == "scissors" and player_2_hand == "paper"):
        print("-------------------------------------------------------------")
        print(F"{player_1_name} won this round!")
        print("-------------------------------------------------------------")
        player_1_score += 1

    # 2-es játékos nyer, megadva a pontot     
    else:
        print("-------------------------------------------------------------")
        print(F"{player_2_name} won this round!")
        print("-------------------------------------------------------------")
        player_2_score += 1

print("GAME OVER!")

# végső eredmény kiírása    
print(F"{player_1_name}'s score: {player_1_score}")
print(F"{player_2_name}'s score: {player_2_score}")

# győztes vagy döntetlen
if player_1_score > player_2_score:
    print("-------------------------------------------------------------")
    print(F"{player_1_name} wins the game! Congratulations!")
    print("-------------------------------------------------------------")
elif player_2_score > player_1_score:
    print("-------------------------------------------------------------")
    print(F"{player_2_name} wins the game! Congratulations!")
    print("-------------------------------------------------------------")
else:
    print("-------------------------------------------------------------")
    print("The game is a tie!")
    print("-------------------------------------------------------------")
