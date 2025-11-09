# Szabályok
rules = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

# körök bekérése validálással
while True:
    try:
        rounds = int(input("Enter number of rounds (must be odd): ").strip())
        if rounds > 0 and rounds % 2 != 0:
            break
        else:
            print("Please enter a positive odd number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# pontszám beállítás
player1_score = 0
player2_score = 0
round_count = 0

while round_count < rounds:
    # 1 játékos input validálással
    while True:
        move1 = input(f"Player 1, enter your move {list(rules.keys())}: ").strip().lower()
        if move1 in rules:
            break
        print("Invalid move. Try again.")

    # 2 játékos input validálással
    while True:
        move2 = input(f"Player 2, enter your move {list(rules.keys())}: ").strip().lower()
        if move2 in rules:
            break
        print("Invalid move. Try again.")

    # kiértékel
    if move1 == move2:
        print("It's a tie. Replay the round.")
        continue

    if rules[move1] == move2:
        print("Player 1 wins the round!")
        player1_score += 1
    else:
        print("Player 2 wins the round!")
        player2_score += 1

    round_count += 1

# eredményhírdetés
print("\nFinal Result:")
if player1_score > player2_score:
    print(f"Player 1 wins with {player1_score} points!")
else:
    print(f"Player 2 wins with {player2_score} points!")
