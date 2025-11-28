while True:
    rounds=int(input("How many round you want to play maximum?"))
    if rounds % 2 != 0:
        break
    print("Please provide an even number!")

rounds_to_win=rounds//2+1
print(f"The first who reach {rounds_to_win} rounds, will win the match! Please make your choices R=Rock,P=Paper,S=Scisors")

rps=["R","P","S"] #rövidítettem a stringeket
actual_round=0
p1_points=0
p2_points=0
while actual_round < rounds:
    p1=input("Player_1 it is yout turn: R/P/S ?: ").upper()
    while p1 not in rps:
        print("Please provide R/P/S")
        p1=input("Player_1 it is yout turn: R/P/S ?: ").upper()
    p2=input("Player_2 it is yout turn: R/P/S ?: ").upper()
    while p2 not in rps:
        print("Please provide R/P/S")
        p2=input("Player_2 it is yout turn: R/P/S ?: ").upper()
    if p1==p2:
        print("TIE! Try again")
    elif p1=="R" and p2=="S" or p1=="P" and p2=="R" or p1=="S" and p2=="P":
        print("p1 won this round")
        actual_round=actual_round+1
        p1_points=p1_points+1
        if p1_points>rounds/2: #Ha valaki eléri a szükséges győzelem számot, akkor vége!
             break
        else:
            print(f"The actual score is p1:{p1_points} p2:{p2_points}, keep going!")
    else:
        print("p2 won this round")
        actual_round=actual_round+1
        p2_points=p2_points+1
        if p2_points>rounds/2: #Ha valaki eléri a szükséges győzelem számot, akkor vége!
            break
        else:
            print(f"The actual score is p1:{p1_points} p2:{p2_points}, keep going!")
if p1_points>p2_points:
    print(f"It is over! The winner is p1 by {p1_points} to {p2_points}!")
else:
    print(f"It is over! The winner is p2 by {p2_points} to {p1_points}!")
