#rock_paper_scissors

# Bekéri a 1-es játékos nevét és üres név esetén hiba
while True:
    player_1_name = input("Enter Player 1's name: ").strip().title()
    if player_1_name:
        break
    print("Error: Please enter a valid name.")

# Bekéri a 2-es játékos nevét és üres név esetén hiba
while True:
    player_2_name = input("Enter Player 2's name: ").strip().title()
    if player_2_name:
        break
    print("Error: Please enter a valid name.")

#Körök száma , de csak páratlan értékeket fogad el
while True:
    rounds_played = int(input("How many rounds do you want to play? (Must be an odd number): "))
    if rounds_played % 2 == 1:
        break
    print("Error: Please enter an odd number and try again.")

# játékosok pontjainak inicializálása
player_1_score = 0
player_2_score = 0
# megfelelő kézjelek listája
hand_signs = ["rock", "paper", "scissors"]

#Kezdés
print("-------------------------------------------------------------")
print(F"GAME IS STARTING ...  {rounds_played} ROUNDS: {player_1_name} vs. {player_2_name}!")

round_num = 1 
while round_num <= rounds_played:

    print("-------------------------------------------------------------")
    print(F"ROUND: {round_num}!")
    print("-------------------------------------------------------------")
   
    # Kézjelek 1 játékosnál, érvénytelen esetén újra
    while True:
        player_1_hand = input(F"{player_1_name}, enter your hand sign (rock, paper, scissors): ").strip().lower()
        if player_1_hand in hand_signs:
            break
        print("Invalid hand sign!!!! Please try again.")
       
    # Kézjelek 2 játékosnál, érvénytelen esetén újra
    while True:
        player_2_hand = input(F"{player_2_name}, enter your hand sign (rock, paper, scissors): ").strip().lower()
        if player_2_hand in hand_signs:
            break
        print("Invalid hand sign!!!! Please try again.")
            
   

    #amikor az 1-es játekos nyer, megadva a pontot
    if (player_1_hand == "rock" and player_2_hand == "scissors") or (player_1_hand == "paper" and player_2_hand == "rock") or (player_1_hand == "scissors" and player_2_hand == "paper"):
        print("-------------------------------------------------------------")
        print(F"{player_1_name} won this round!")
        
        player_1_score += 1
        # A körszám nő, megyünk a következő körre!
        round_num += 1 

    # 2-es játékos nyer, megadva a pontot     
    elif (player_2_hand == "rock" and player_1_hand == "scissors") or (player_2_hand == "paper" and player_1_hand == "rock") or (player_2_hand == "scissors" and player_1_hand == "paper"):
        print("-------------------------------------------------------------")
        print(F"{player_2_name} won this round!")
        
        player_2_score += 1
            # A körszám nő, megyünk a következő körre!
        round_num += 1
     # eredmény meghatározása,ha döntetlen
    else:
        print("-------------------------------------------------------------")
        print("Tie!!! Play again.")
        continue

print("===============================================================")
print("                      G A M E   O V E R!                       ")
print("===============================================================")

# végső eredmény kiírása    
print(F"{player_1_name}'s score: {player_1_score}")
print(F"{player_2_name}'s score: {player_2_score}")

# győztes vagy döntetlen
if player_1_score > player_2_score:
    print("-------------------------------------------------------------")
    print(F"{player_1_name} wins the game! Congratulations!")
    print("-------------------------------------------------------------")
else:
    print("-------------------------------------------------------------")
    print(F"{player_2_name} wins the game! Congratulations!")
    print("-------------------------------------------------------------")
