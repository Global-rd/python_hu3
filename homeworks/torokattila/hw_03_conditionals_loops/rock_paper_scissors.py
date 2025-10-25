# Kő-papír-olló játék

answer = ["rock","paper","scissors"]

while True:
    rounds = int(input("Hány kört szeretnél játszani? (Páratlan számot írj!) "))
    if rounds % 2 != 0:
        break
print("Kezdődjön a játék!")
print("------------------")

pts_pl1 = 0
pts_pl2 = 0
round = 0

# Indul a játék
while round < rounds:
    print()
    print(f"{round+1}.kör")
    print("---------")
    # Tippek bekérése    
    tip_pl1, tip_pl2 = ('','')
    while True:
        tip_pl1 = input("1.játékos tipp:")
        if tip_pl1 in answer:
            break
    while True:
        tip_pl2 = input("2.játékos tipp:")
        if tip_pl2 in answer:
            break            
    # Pontozás
    if tip_pl1 == tip_pl2:
        print("Döntetlen, kérem újra a tippeket!")
        continue
    if (
        (tip_pl1 == "rock" and tip_pl2 == "scissors" ) or 
        (tip_pl1 == "paper" and tip_pl2 == "rock") or
        (tip_pl1 == "scissors" and tip_pl2 == "paper")
        ):
            pts_pl1 +=1
    else:
            pts_pl2 +=1

    round +=1
 
# Eredményhirdetés        

print("----------")
print("A játék végeredmény:")

winner = "1.játékos" if pts_pl1 > pts_pl2 else "2.játékos"
winner_pts = pts_pl1 if pts_pl1 > pts_pl2 else pts_pl2

print(f"A játékot a(z) {winner} nyerte {winner_pts} ponttal.")



