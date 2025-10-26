# rock_paper_scissors

while True:
    max_rounds = int(input("Type in how many rounds do you want to play? "))               
    if (max_rounds % 2 != 0):                 
        break
    print("You need to enter an odd number") 


gamer_A_point = 0
gamer_B_point = 0
act_round = 1
while act_round <= max_rounds:
    print("")
    print(f"All rounds: {max_rounds}. Comming: {act_round}. Gamer_A: {gamer_A_point}, Gamer_B: {gamer_B_point}")
    while True:
        gamer_A_answer = input("GAMER_A > Type in your answer (rock-paper-scissors): ").lower()
        if gamer_A_answer in ["rock", "paper", "scissors"]:
            break
        print("Please type in the word according to rule!")
    while True:
        gamer_B_answer = input("GAMER_B > Type in your answer (rock-paper-scissors): ").lower()
        if gamer_B_answer in ["rock", "paper", "scissors"]:
            if gamer_A_answer == gamer_B_answer:
                print("Same answer. Round again!")                           # nem növeli az act_round-ot
                break                                                        # csak kiszáll
            elif (gamer_A_answer == "rock" and gamer_B_answer == "scissors") or \
                 (gamer_A_answer == "paper" and gamer_B_answer == "rock") or \
                 (gamer_A_answer == "scissors" and gamer_B_answer == "paper"):
                act_round += 1
                gamer_A_point += 1
                break
            else:
                act_round += 1
                gamer_B_point += 1    
                break
        else:
            print("Please type in the word according to rule!")

print("")
print(f"Game over. Result: GAMER_A: {gamer_A_point} point;  GAMER_B: {gamer_B_point} point. The winner: {"GAMER_A" if gamer_A_point > gamer_B_point else "GAMER_B"}")


