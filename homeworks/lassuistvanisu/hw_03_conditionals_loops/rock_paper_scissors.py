valid_choices = ["rock", "paper", "scissors"]

#Játék körének bekérése és hibakazelés
while True:
    rounds_input = int(input("How many rounds would you like to play (odd number)? "))
    if rounds_input > 0 and rounds_input % 2 == 1:
            break
    print(f"{rounds_input} is not a positive odd number! Please enter a positive odd number!")

# Alapértékek beállítása
player_1_points = 0
player_2_points = 0
current_round = 1

#Kör kezdése és válaszok elenőrzése 
while current_round <= rounds_input:
    print(f"{current_round}. round")
    while True:
        player_1_choice = input("1. player - rock / paper / scissors: ").strip().lower()
        if player_1_choice not in valid_choices:
            print(" Only rock, paper, or scissors are accepted!")
            continue
        player_2_choice = input("2. player - rock / paper / scissors:  ").strip().lower()
        if player_2_choice not in valid_choices:
            print(" Only rock, paper, or scissors are accepted!")
            continue      
        if player_1_choice == player_2_choice:
            print("It's a draw, replay the round!")
            continue
        
#Ellenőrzés
        winner = None
        if player_1_choice == "rock":
            if player_2_choice == "scissors":
                winner = 1
            else:  # player_2_choice == "paper"
                winner = 2
        elif player_1_choice == "paper":
            if player_2_choice == "rock":
                winner = 1
            else:  # player_2_choice == "scissors"
                winner = 2
        else:  # player_1_choice == "scissors"
            if player_2_choice == "paper":
                winner = 1
            else:  # player_2_choice == "rock"
                winner = 2
        print(f"Player {winner} won the round!")
        if winner == 1:
            player_1_points += 1
        elif winner == 2:
            player_2_points += 1
        break

    current_round += 1
# Eredmény
print("Game over!")
if player_1_points > player_2_points:
    print(f"Player 1 won with {player_1_points} points!")
else:
    print(f"Player 2 won with {player_1_points} points!")
