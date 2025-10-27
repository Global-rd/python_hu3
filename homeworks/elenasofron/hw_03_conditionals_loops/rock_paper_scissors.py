# game rules
possible_actions = ["rock","paper","scissors"]
player1_points = 0
player2_points = 0

# number of rounds
while True:
    rounds = int(input("How many rounds would you like to play?"))
    if rounds % 2 != 0:
        break
    else:
        print("Not ok.")

# start a game
current_round = 1
while current_round <= rounds:
    player1 = input("Player1, enter your choice (rock, paper, scissors):").strip().lower()
    player2 = input("Player2, enter your choice (rock, paper, scissors):").strip().lower()
    if player1 in possible_actions and player2 in possible_actions:
        if player1 != player2: 
            if ((player1 == "rock" and player2 == "scissors") or 
            (player1 == "scissors" and player2 == "paper") or 
            (player1 == "paper" and player2 == "rock")):
                player1_points += 1
            else: player2_points += 1
            current_round += 1
        else: 
            print("Play again")
    else:
        print("Please enter the valid answer (rock / paper / scissors.")

# results
if player1_points > player2_points:
    winner = "Player1"
    final_points = player1_points
else:
    winner = "Player2"
    final_points = player2_points

print(f"The winner is the {winner} with the points: {final_points}.")