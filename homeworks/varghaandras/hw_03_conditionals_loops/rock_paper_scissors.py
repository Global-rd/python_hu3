valid_choices = ["rock", "paper", "scissors"]

rounds = 0
while True:
    rounds = int(input("How many rounds would you like to play? (Must be an odd number): "))
    if rounds % 2 == 1:
        break
    else:
        print("Error: You must enter an odd number to avoid a tie!")

score1 = 0
score2 = 0
total_rounds = 0
needed_to_win = rounds // 2 + 1

while score1 < needed_to_win and score2 < needed_to_win:
    print(f"--- Round {total_rounds + 1} ---")
    while True:
        choice1 = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
        if choice1 not in valid_choices:
            print("Error: Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        choice2 = input("Player 2, enter your choice (rock/paper/scissors): ").lower()
        if choice2 not in valid_choices:
            print("Error: Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        if choice1 == choice2:
            print("It's a tie! Replay the round.")
            continue
        elif (choice1 == "rock" and choice2 == "scissors") or \
             (choice1 == "scissors" and choice2 == "paper") or \
             (choice1 == "paper" and choice2 == "rock"):
            score1 += 1
            print("Player 1 wins this round!")
        else:
            score2 += 1
            print("Player 2 wins this round!")
        break

    total_rounds += 1

print("--- Game Over ---")
if score1 > score2:
    print(f"Player 1 wins the game with {score1} points!")
else:
    print(f"Player 2 wins the game with {score2} points!")