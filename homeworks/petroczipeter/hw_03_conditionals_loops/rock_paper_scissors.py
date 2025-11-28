# Ez egy kő-papír-olló játék, amit két ember játszik
# Bekérem, hogy hány kört akarnak játszani (csak páratlan szám)
while True:
    rounds = input("Hány kört akartok játszani? (páratlan szám): ")
    if rounds.isdigit():
        rounds = int(rounds)
        if rounds % 2 == 1:
            break
        else:
            print("Kérlek, páratlan számot adj meg!")
    else:
        print("Kérlek számot adj meg!")
# Pontszámok
p1_score = 0
p2_score = 0
current_round = 1
# A játék menete
while current_round <= rounds:
    print(f"\n{current_round}. kör:")
# 1. Játékos választása
    while True:
        p1 = input("1. játékos választása (rock/paper/scissors): ")
        if p1 in ["rock", "paper", "scissors"]:
            break
        else:
            print("Hibás választás! Csak 'rock', 'paper' vagy 'scissors' lehet.")
# 2. Játékos választása
    while True:
        p2 = input("2. játékos választása (rock/paper/scissors): ")
        if p2 in ["rock", "paper", "scissors"]:
            break
        else:
            print("Hibás választás! Csak 'rock', 'paper' vagy 'scissors' lehet.")
# Eredmény megállapítása
    if p1 == p2:
        print("Döntetlen! Új kör")
        continue
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        print("1. játékos nyert ebben a körben!")
        p1_score += 1
    else:
        print("2. játékos nyert ebben a körben!")
        p2_score += 1
    current_round += 1
# Győztes printelése
print("\n--- A játéknak vége! ---")
if p1_score > p2_score:
    print(f"Az 1. játékos nyert {p1_score}:{p2_score} arányban!")
else:
    print(f"A 2. játékos nyert {p2_score}:{p1_score} arányban")