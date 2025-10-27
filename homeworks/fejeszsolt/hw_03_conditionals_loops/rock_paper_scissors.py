rules = """
Ez egy kő-papír-olló játék.
A szabályok a következőek:
- A kő eltöri az ollót.
- Az olló elvágja a papírt.
- A papír becsomagolja a követ.
"""
print(rules)

player1 = input("Első játékos neve: ").title().strip()
player2 = input("Második játékos neve: ").title().strip()
valid_answers = ["rock", "paper", "scissors"]
round=0
player1_wins=0
player2_wins=0

while True:
    rounds = int(input("Hány kört akartok játszani? Pératlan számot adj meg!"))
    if rounds % 2 != 0:
       break
    print ("ez nem páratlan, adj meg másikat")   

while round != rounds:
    while True:
        answer_player1= input(f"{player1}: Rock, Paper, Scissors? ").strip().lower()
        if answer_player1 in valid_answers:
             break
        print ("A felsoroltak közül válassz!")
    while True:
        answer_player2= input(f"{player2}: Rock, Paper, Scissors? ").strip().lower()
        if answer_player2 in valid_answers:
            break
        print ("A felsoroltak közül válassz!")
    if answer_player1==answer_player2:
        print ("Ez a kör döntetlen, játszatok újjat!")
    elif (answer_player1 == "rock" and answer_player2 == "scissors") or \
    (answer_player1 == "paper" and answer_player2 == "rock") or \
    (answer_player1 == "scissors" and answer_player2 == "paper"):
        print (f"{player1} nyerte ezt a kört!")
        player1_wins +=1
        round +=1
    else:
        print (f"{player2} nyerte ezt a kört!")
        player2_wins +=1
        round +=1
else:
    if  player1_wins > player2_wins:
        print (f" {player1} pontjai száma: {player1_wins}, {player2} pontjai száma: {player2_wins}. {player1} nyerte a játékot")
    else:
        print (f" {player1} pontjai száma: {player1_wins}, {player2} pontjai száma: {player2_wins}. {player2} nyerte a játékot")