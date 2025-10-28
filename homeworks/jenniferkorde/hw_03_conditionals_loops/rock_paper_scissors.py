while True:
    text = input("How many rounds (odd number like 3, 5, 7): ").strip()
    if text.isdigit():
        rounds = int(text)
        if rounds > 0 and (rounds % 2 == 1):
            break
    print("Error: type a positive ODD whole number (e.g., 3 or 5).")

p1_score = 0
p2_score = 0
decided = 0

while decided < rounds:
    print(f"\nRound {decided + 1} of {rounds}")

    while True:
        m1 = input("Player 1 (rock/paper/scissors): ").strip().lower()
        if not (m1 == "rock" or m1 == "paper" or m1 == "scissors"):
            print("Invalid. Type exactly: rock, paper, or scissors.")
            continue

        m2 = input("Player 2 (rock/paper/scissors): ").strip().lower()
        if not (m2 == "rock" or m2 == "paper" or m2 == "scissors"):
            print("Invalid. Type exactly: rock, paper, or scissors.")
            continue

        if m1 == m2:
            print("Draw. Replay this round.")
            continue


        if m1 == "rock" and m2 == "scissors":
            p1_score += 1
            print("Player 1 wins this round!")
        elif m1 == "rock" and m2 == "paper":
            p2_score += 1
            print("Player 2 wins this round!")
        elif m1 == "paper" and m2 == "rock":
            p1_score += 1
            print("Player 1 wins this round!")
        elif m1 == "paper" and m2 == "scissors":
            p2_score += 1
            print("Player 2 wins this round!")
        elif m1 == "scissors" and m2 == "paper":
            p1_score += 1
            print("Player 1 wins this round!")
        elif m1 == "scissors" and m2 == "rock":
            p2_score += 1
            print("Player 2 wins this round!")

        decided+=1
        break


print("\n=== Final Result ===")
if p1_score > p2_score:
    print(f"Player 1 wins by {p1_score - p2_score} point(s) — {p1_score}:{p2_score}.")
else:
    print(f"Player 2 wins by {p2_score - p1_score} point(s) — {p2_score}:{p1_score}.")
    