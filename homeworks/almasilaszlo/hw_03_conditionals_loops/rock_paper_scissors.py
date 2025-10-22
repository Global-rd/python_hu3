rounds=1
rounds=int(input("How many round you want to play maximum?"))
if rounds % 2 != 0:
    pass
else:
    print("Please provide an even number!")
    rounds=int(input("How many round you want to play maximum?"))
rounds_to_win=rounds//2+1
print(f"The first who reach {rounds_to_win} rounds, will win the match! Please make your choices R=Rock,P=Paper,S=Scisors")

RPS=["R","P","S"] #rövidítettem a stringeket
actual_round=0
P1_points=0
P2_points=0
while actual_round < rounds:
    P1=input("Player_1 it is yout turn: R/P/S ?: ").upper()
    while P1 not in RPS:
        print("Please provide R/P/S")
        P1=input("Player_1 it is yout turn: R/P/S ?: ").upper()
    P2=input("Player_2 it is yout turn: R/P/S ?: ").upper()
    while P2 not in RPS:
        print("Please provide R/P/S")
        P2=input("Player_2 it is yout turn: R/P/S ?: ").upper()
    if P1==P2:
        print("TIE! Try again")
    elif P1=="R" and P2=="S" or P1=="P" and P2=="R" or P1=="S" and P2=="P":
        print("P1 won this round")
        actual_round=actual_round+1
        P1_points=P1_points+1
        if P1_points>rounds/2: #Ha valaki eléri a szükséges győzelem számot, akkor vége!
             break
        else:
            print(f"The actual score is P1:{P1_points} P2:{P2_points}, keep going!")
    else:
        print("P2 won this round")
        actual_round=actual_round+1
        P2_points=P2_points+1
        if P2_points>rounds/2: #Ha valaki eléri a szükséges győzelem számot, akkor vége!
            break
        else:
            print(f"The actual score is P1:{P1_points} P2:{P2_points}, keep going!")
if P1_points>P2_points:
    print(f"It is over! The winner is P1 by {P1_points} to {P2_points}!")
else:
    print(f"It is over! The winner is P2 by {P2_points} to {P1_points}!")
