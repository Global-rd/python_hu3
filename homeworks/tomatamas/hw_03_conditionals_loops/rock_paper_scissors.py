# Körök számának bekérése
rounds = 0
while rounds % 2 == 0:
    rounds = int(input("How many winning rounds do you want to play for: ").strip())
    if rounds % 2 == 0:
        print("There has to be a winner, pick an odd number!")

# Játék
play_round = 1
player_1_wincount = 0
player_2_wincount = 0
not_valid_input_message = "You can only choose from rock, paper or scissors."
player_1_won_message = "- Player 1 won the round."
player_2_won_message = "- Player 2 won the round."
choices = "choose rock/paper/scissors: "

while play_round <= rounds:
    valid_answers = ["rock", "paper", "scissors"]
    player_1 = ""
    player_2 = ""

    while player_1 not in valid_answers:
        player_1 = input(f"Player 1, {choices}").strip()
        if player_1 not in valid_answers:
            print(not_valid_input_message)
    while player_2 not in valid_answers:
        player_2 = input(f"Player 2, {choices}").strip()
        if player_2 not in valid_answers:
            print(not_valid_input_message)

    if player_1 == player_2:
        print("It's a tie, round has to be replayed!")
        continue
    
    if player_1 == "rock":
        if player_2 == "paper":
            print(player_2_won_message)
            player_2_wincount += 1
        elif player_2 == "scissors":
            print(player_1_won_message)
            player_1_wincount += 1
    elif player_1 == "paper":
        if player_2 == "rock":
            print(player_1_won_message)
            player_1_wincount += 1
        elif player_2 == "scissors":
            print(player_2_won_message)
            player_2_wincount += 1
    elif player_1 == "scissors":
        if player_2 == "rock":
            print(player_2_won_message)
            player_2_wincount += 1
        elif player_2 == "paper":
            print(player_1_won_message)
            player_1_wincount += 1

    play_round += 1
    # Ha már valamelyik játékos nyert, kilépni a ciklusból
    winning_score = rounds // 2 + 1
    if player_1_wincount == winning_score or player_2_wincount == winning_score:
        if rounds > 1:
            print("We already have a winner!")
            break

# Eredmény kiírása
if player_1_wincount > player_2_wincount:
    print(f"Player 1 won the game, the score is {player_1_wincount} : {player_2_wincount}")
elif player_2_wincount > player_1_wincount:
    print(f"Player 2 won the game, the score is {player_2_wincount} : {player_1_wincount}")