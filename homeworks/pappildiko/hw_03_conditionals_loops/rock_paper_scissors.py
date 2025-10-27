while True:
    round_input = input("Enter how many rounds (odd number) would you like to play: ").strip()
    if round_input.isdigit():
        rounds = int(round_input)
        if rounds == 0:
            print("The number must be positive.")
        elif rounds % 2 == 0:
            print("The number must be odd.")
        else:
            break
    else:
        print("Invalid input. Please enter an integer.")

# Initalizing scores
player1_score = 0
player2_score = 0

# Game cycle
while player1_score + player2_score < rounds:

    # Player 1 input
    while True:
        player1_answer = input("Enter rock, paper or scissors for Player 1: ").strip().lower()
        if player1_answer in ["rock", "paper", "scissors"]:
            break
        print("Please enter rock, paper or scissors.")

    # Player 2 input
    while True:
        player2_answer = input("Enter rock, paper or scissors for Player 2: ").strip().lower()
        if player2_answer in ["rock", "paper", "scissors"]:
            break
        print("Please enter rock, paper or scissors.")

    # Checking if they chose the same.
    if player1_answer == player2_answer:
        print("Both players chose the same. No points awarded. Try again.\n")
        continue

    # Deciding who won the round
    if (player1_answer == "rock" and player2_answer == "scissors") or \
       (player1_answer == "paper" and player2_answer == "rock") or \
       (player1_answer == "scissors" and player2_answer == "paper"):
        player1_score += 1
        print("Player 1 wins this round!\n")
    else:
        player2_score += 1
        print("Player 2 wins this round!\n")

    # Display the score after each round - optional
    # print(f"Score: Player 1 = {player1_score}, Player 2 = {player2_score}\n")

print("Game over!")
if player1_score > player2_score:
    print(f"Player 1 wins the game! Player 1 score = {player1_score}, Player 2 sore = {player2_score}\n")
else:
    print(f"Player 2 wins the game! Player 1 score = {player1_score}, Player 2 sore = {player2_score}\n")