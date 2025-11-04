"""
Kő, papír, olló játék két játékos között.
A játékosok felváltva mondják válaszaikat.

Három értékből lehet választani: kő, papír vagy olló.
- A kő legyőzi az ollót (a kő összetöri az ollót)
- Az olló legyőzi a papírt (az olló elvágja a papírt)
- A papír legyőzi a követ (a papír becsomagolja a követ)

Ha az adott körben mindkét játékos ugyanazt választja, döntetlen az eredmény.
Ebben az esetben senki sem nyer, új kört kell játszani.
A döntetlen kört nem számoljuk bele a maximális körök számába.
""" 
# nem változik az értéke -> tuple 
correct_answers = ("rock", "paper", "scissors") #kő, papír, olló

max_round = 0

# Bekérjük, hogy maximum hány kört játszanak
while max_round == 0:
    max_round = input("Enter the maximum score possible: ")

    if max_round.isnumeric() and int(max_round) > 0 and int(max_round) % 2 == 1:
        max_round = int(max_round)
    else:
        print("Invalid maximum score. It must be a positive odd integer.")
        max_round = 0  

score_1 = 0 #1. játékos pontszáma
score_2 = 0 #2. játékos pontszáma

round = max_round #max körök szávalmával indulunk

while round > 0:

    #bekérjük az 1. játékos válaszát
    player1_answer = ""

    while bool(player1_answer) == False:
        player1_answer = input("Player 1, enter your choice (rock, paper, scissors): ").strip().lower()

        if player1_answer not in correct_answers:
            print("Invalid choice by Player 1. Please choose rock, paper, or scissors.")
            player1_answer = ""

    #bekérjük az 2. játékos válaszát
    player2_answer = ""

    while bool(player2_answer) == False:
        player2_answer = input("Player 2, enter your choice (rock, paper, scissors): ").strip().lower()

        if player2_answer not in correct_answers:
            print("Invalid choice by Player 2. Please choose rock, paper, or scissors.")
            player2_answer = "" 

    if player1_answer == player2_answer:
        print("It's a tie!")
    else:
        if  (player1_answer == "rock" and player2_answer == "scissors") or \
            (player1_answer == "scissors" and player2_answer == "paper") or \
            (player1_answer == "paper" and player2_answer == "rock"):
            score_1 += 1 #player 1 nyer
        else:
            score_2 += 1 #player 2 nyer

        round -= 1 #csökkentjük a körök számát
    
    print(f"Remaining rounds: {round}") #hátralévő körök száma

if score_1 > score_2:
    print(f"Player 1 wins the game! ({score_1} to {score_2})")
elif score_2 > score_1:
    print(f"Player 2 wins the game! ({score_2} to {score_1})")
else:
    print("The game ends in a tie!") #ide nem fog eljutni, mert max_score páratlan


