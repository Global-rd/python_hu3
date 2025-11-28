#feladat: kő-papír olló játék
# bekérni hányat akarnak játszani, 
#  játék db-számánál ellenőrizni, hogy ne legyen szöveg, negatv, nulla, páros
# pontozás:olló vágja a papírt, a kó kicsorbítja az ollót, papír becsomagolja a követ
# döntetlenek kezelése: döntetlent nem számoljuk
# ha elértük a bekért darabszámot, akkor kiírjuk a nyertest


game_rounds=int(input("Hányat akartok játszani?"))
while (game_rounds % 2 == 0) or (game_rounds<=0):
    game_rounds=int(input("Hányat akartok játszani, páratlan pozitív számot adj meg!"))

valid_inputs=["p","r","s"]
gamer1_win=0
gamer2_win=0

while True:
    gamer1=input("Gamer1 válassz, hogy kő(r) papír(p) vagy ollo(s)").lower()
    while gamer1 not in valid_inputs :
        gamer1=input("Gamer1 válassz, hogy kő(r) papír(p) vagy ollo(s)").lower()

    gamer2=input("Gamer2 válassz, hogy kő(r) papír(p) vagy ollo(s)").lower()
    while gamer2 not in valid_inputs:
        gamer2=input("Gamer2válassz, hogy kő(r) papír(p) vagy ollo(s)").lower()

    if gamer1=="p" and  gamer2 =="r": 
        gamer1_win+=1
    elif gamer1=="r" and gamer2 =="s": 
        gamer1_win+=1
    elif gamer1=="s" and gamer2 =="p": 
        gamer1_win+=1
    elif gamer1==gamer2:
        continue
    else:gamer2_win+=1
        
    if gamer1_win+gamer2_win==game_rounds:
        break
if gamer1_win>gamer2_win:
    print("Gamer1 nyert") 
else: 
    print("Gamer2 nyert")   
print(f"gamer1 pontja: {gamer1_win}, gamer2 pontja: {gamer2_win}")


