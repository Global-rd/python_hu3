# Kő-papír-olló játék

answer = ["rock","paper","scissors"]

while True:
    rounds = int(input("Hány kört szeretnél játszani? "))
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
    tipp1, tipp2 = ('','')
    while True:
        while True:
            tipp1 = input("1.játékos tipp:")
            if tipp1 in answer:
                break
        while True:
            tipp2 = input("2.játékos tipp:")
            if tipp2 in answer:
                break            
        if tipp1 != tipp2:
            break
        else:
            print("Ugyanaz....")
    # Pontozás
    if tipp1 == 'rock':
        if tipp2 == "paper":
            pts_pl2 +=1
        else:
            pts_pl1 +=1
    if tipp1 == 'paper':
        if tipp2 == "rock":
            pts_pl1 +=1
        else:
            pts_pl2 +=1
    if tipp1 == 'scissors':
        if tipp2 == "rock":
            pts_pl2 +=1
        else:
            pts_pl1 +=1
    round +=1
print("----------")
print("A játék végeredmény:")

nyertes = "1.játékos" if pts_pl1 > pts_pl2 else "2.játékos"
nyertes_pts = pts_pl1 if pts_pl1 > pts_pl2 else pts_pl2

print(f"A játékot a(z) {nyertes} nyerte {nyertes_pts} ponttal.")



