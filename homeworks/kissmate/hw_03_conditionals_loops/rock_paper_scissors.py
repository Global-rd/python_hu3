player1_score = 0
player2_score = 0
round_count = 0
while True:
    rounds = int(input("Enter number of rounds to play: "))
    if rounds % 2 == 0:
        print("Please enter an odd number of rounds for a decisive winner.")
    else:
        print(f"Starting a game of {rounds} rounds!")
        break
print("Game setup complete.")
while round_count < rounds:
    player1 = input("Player 1, enter your choice (rock, paper, scissors): ")
    if player1 not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    player2 = input("Player 2, enter your choice (rock, paper, scissors): ")
    if player2 not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    if player1 == player2:
        print("It's a tie! No points awarded.")
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins this round!")
        player1_score += 1
    else:
        print("Player 2 wins this round!")
        player2_score += 1
    round_count += 1
    if round_count == rounds:
        print("Game over!")
        print(f"Final Scores - Player 1: {player1_score}, Player 2: {player2_score}")
