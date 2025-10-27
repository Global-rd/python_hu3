while True:
    try:

        round = int(input("Hány kört szeretnétek játszani? "))
        if round % 2 == 1 and round > 0:
            break
        else:
            print("Adj meg pozitív páratlan számot! ")

    except ValueError:
        print("Adj meg egész számpt! ")

player1_score = 0
player2_score = 0
valid_choices = ["rock", "paper", "scissors", "lizard", "spock"]

for round_number in range(1, round+1):
    print(f"\nkör {round_number}: ")
    while True:
        player1_choice = input(
            "Játékos 1 válasszon (rock/paper/scissors/lizard/spock): ").strip().lower()
        if player1_choice not in valid_choices:
            print("Hiba! Érvénytelen választás.")
            continue

        player2_choice = input(
            "Játékos 2 válasszon (rock/paper/scissors/lizard/spock): ").strip().lower()
        if player2_choice not in valid_choices:
            print("Hiba! Érvénytelen választás.")
            continue
        if player1_choice == player2_choice:
            print("Döntetlen. Ismételjük meg a kört!")
            continue
        elif (
            (player1_choice == "rock" and player2_choice == "scissors") or
            (player1_choice == "scissors" and player2_choice == "paper") or
            (player1_choice == "paper" and player2_choice == "rock") or
            (player1_choice == "lizard" and player2_choice == "spock") or
            (player1_choice == "rock" and player2_choice == "lizard") or
            (player1_choice == "spock" and player2_choice == "scissors") or
            (player1_choice == "scissors" and player2_choice == "lizard") or
            (player1_choice == "lizard" and player2_choice == "paper") or
            (player1_choice == "paper" and player2_choice == "spock") or
            (player1_choice == "spock" and player2_choice == "rock")
        ):
            print("Játékos 1 nyert a körben! ")
            player1_score += 1
        else:
            print("Játékos 2 nyert a körben! ")
            player2_score += 1
        break

print("\nVégső eredmény: ")
if player1_score > player2_score:
    print(f"Játékos 1 nyert {player1_score} ponttal!")
else:
    print(f"Játékos 2 nyert {player2_score} ponttal!")
