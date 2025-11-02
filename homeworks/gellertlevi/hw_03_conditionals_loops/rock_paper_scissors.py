
rounds_of_game = int(input("Enter the number of game rounds:"))
while rounds_of_game % 2 == 0: 
    
    rounds_of_game = int(input("Enter an odd number of game rounds:"))   
else:
    print(f"You will play {rounds_of_game} rounds!")




gamer1_points = 0
gamer2_points = 0

for round in range(1, rounds_of_game + 1):
    print(f"Round {round}")

    gamer1_choice = input("gamer1 should provide his/her choice: ").lower()
    while gamer1_choice not in ["rock", "paper", "scissors"]:  
        gamer1_choice = input("gamer1, please choose rock, paper, or scissors: ").lower()

    gamer2_choice = input("gamer2 should provide his/her choice: ").lower()
    while gamer2_choice not in ["rock", "paper", "scissors"]:  
        gamer2_choice = input("gamer2, please choose rock, paper, or scissors: ").lower()

    # the game starts here
    while gamer1_choice == gamer2_choice:
        print("It's a draw!")
        gamer1_choice = input("gamer1 should provide his/her choice again: ").lower()
        while gamer1_choice not in ["rock", "paper", "scissors"]:  
            gamer1_choice = input("gamer1, please choose rock, paper, or scissors: ").lower()

        gamer2_choice = input("gamer2 should provide his/her choice again: ").lower()
        while gamer2_choice not in ["rock", "paper", "scissors"]:  
            """gamer2_choice = input("gamer2, please choose rock, paper, or scissors: ").lower()"""    

    if (gamer1_choice == "rock" and gamer2_choice == "scissors") or \
         (gamer1_choice == "scissors" and gamer2_choice == "paper") or \
         (gamer1_choice == "paper" and gamer2_choice == "rock"):
        print("Gamer 1 wins the round!")
        gamer1_points += 1

    else:
        print("Gamer 2 wins the round!")
        gamer2_points += 1

    print(f"Score after Round {round}: Gamer1 = {gamer1_points}, Gamer2 = {gamer2_points}")
if gamer1_points > gamer2_points:
    print("Gamer 1 is the overall winner!")
else:
    print("Gamer 2 is the overall winner!")

 
