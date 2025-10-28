valid_answers = ["rock", "paper", "scissors"]

rules = {"rock":"scissors", "scissors":"paper", "paper":"rock"}

scores = {"Player 1":0, "Player 2": 0}


while True:
    n_rounds = int(input("How many rounds do you wish to play: "))
    if n_rounds >= 3 and n_rounds % 2 != 0:
        print(f"Number of rounds to play is: {n_rounds}")
        break 
    else:
        print(f"Please give an odd number higher than 3")

#Player 1 input

for n_round in range(1, n_rounds+1):     
    while True:            
        answer1 = input(f"Player 1 please enter your answer: ")
        if answer1 in valid_answers:
            print(f"Player 1 answer for round number {n_round} is: {answer1}")
            break
        else:
            print("Please enter a valid answer")

#Player 2 input

    while True:            
        answer2 = input(f"Player 2 please enter your answer: ")
        if answer2 in valid_answers:
            print(f"Player 2 answer for round number {n_round} is: {answer2}")
            break
        else:
            print("Please enter a valid answer")

    if answer1 == answer2:
        result = "Tie"
        print(f"It is a {result}, replay the round")
        continue
    
    elif rules[answer1] == answer2:
        result = "Player 1 is the winner"
        print(result)        
    else:
        result = "Player 2 is the winner"
        print(result)

    if result == "Player 1 is the winner":
        scores["Player 1"] += 1
    elif result == "Player 2 is the winner":
        scores["Player 2"] += 1
    else:
        scores["Player 1"] += 1
        scores["Player 2"] += 1

    print(scores)

    



        



    
    












