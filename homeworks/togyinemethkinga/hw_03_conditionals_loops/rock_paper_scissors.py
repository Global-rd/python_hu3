game=["rock","paper","sciccors"]
first_player_points = 0
second_player_points = 0

# Bekérem a körök számát és maradékos osztással megvizsgálom, hogy a szám páratlan legyen.
while True:
    rounds = int(input("How many rounds would you like to play?"))
    if rounds % 2 != 0:
        break
    else:
        print("Please give me an odd number.")

 # Megvizsgáljuk, hogy melyik kört ki nyeri.
round = 1
while round <= rounds:
    first_player = input("What did the first player show?").strip().lower()
    second_player = input("What did the second player show?").strip().lower()
    if first_player in game and second_player in game: # Először érvényes értéket kell, hogy megadjon.
        if first_player != second_player: # Meg kell vizsgálni, hogy a körnek legyen győztese, tehát nem mutathatják ugyanazt.
            if first_player == "rock" and second_player == "sciccors" or first_player == "sciccors" and second_player == "paper" or first_player == "paper" and second_player == "rock":
                first_player_points += 1
            else: second_player_points += 1
            round += 1
        else: 
            print("Egal, you need to repeat.")
    else:
        print("Please give me 'rock', 'paper' or 'sciccors'.")

# Megvizsgálom, hogy ki nyert és annak mennyi pontja lett.
winner = "first player" if first_player_points > second_player_points else "second player"
higher_point = first_player_points if first_player_points > second_player_points else second_player_points

# Kiírom az eredményt.
print(f"The winner is the {winner} with {higher_point} point(s).")

#print(first_player_points)
#print(second_player_points)