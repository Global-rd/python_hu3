game_index = 1
player1_score = 0
player2_score = 0

win_dict = {"rock": "scissors",
            "scissors": "paper",
            "paper": "rock"}

while True:
    number_of_games = int(input("How many games do you want to play? "))
    if number_of_games % 2 == 0:
        print("Invalid number, please provide an odd number")
    else:
        break

while game_index <= number_of_games:
    while True:
        player1 = input(f"Game [{number_of_games}/{game_index}] - Player1, what is your choice? ")
        if player1 in ["rock", "paper", "scissors"]:
            break
        else:
            print("Invalid choice, please provide a valid choice!")

    while True:
        player2 = input(f"Game [{number_of_games}/{game_index}] - Player2, what is your choice? ")
        if player2 in ["rock", "paper", "scissors"]:
            break
        else:
            print("Invalid choice, please provide a valid choice!")

    if player1 == player2:
        print("Draw, replaying...")
    elif win_dict[player1] == player2:
        print("Player1 wins this game")
        player1_score += 1
        game_index += 1
    else:
        print("Player2 wins this game")
        player2_score += 1
        game_index += 1

if player1_score > player2_score:
    winner = "Player1"
    winner_score = player1_score
else:
    winner = "Player2"
    winner_score = player2_score

print(f'Final result: {winner} wins with {winner_score} points')