print("Helló this is a Rock-Paper-Scissors Game!")
while True:
    try:
        rounds = int(input("Add meg hány kört akartok játszani (páratlan szám): "))
        if rounds % 2 == 0:
            print("X Csak páratlan számot adhatsz meg!")
        elif rounds <= 0:
            print("X Pozitív számot adj meg!")
        else:
            break
    except ValueError:
        print("X csak számot adj meg!")
# Pontszámok
p1_score = 0
p2_score = 0
# Érvényes válaszok
valid_moves = ["rock", "paper", "scissors"]
# Körök lejátszása
for i in range(1, rounds + 1):
    print(f"\n---{i}. kör --- ")
    while True:
        p1 = input("Első játékos választása (rock/paper/scissors):").lower()
        if p1 not in valid_moves:
            print("X Hibás választás, próbáld újra")
            continue
        p2 = input("Második játékos választása (rock/paper/scissors):").lower()
        if p2 not in valid_moves:
            print("X Hibás választás, próbáld újra!")
            continue
        # Döntetlenek kezelése
        if p1 == p2:
             print("Döntetlen! A kört újra kell játszani.")
             continue
        # Eredmény meghatározása
        if (p1 == "rock" and p2 == "scissors") or \
           (p1 == "paper" and p2 == "rock") or \
           (p1 == "scissors" and p2 == "paper"):
            print("Az első játékos nyert ebben a körben!")
            p1_score +=1
        else:
            print("A második játékos nyert ebben a körben!")
            p2_score +=1
        break
# Játék vége eredmény kiírása
print("\njáték vége!")
print(f"Eredmény: 1. játékos {p1_score} pont, 2. játékos {p2_score} ponttal")
if p1_score > p2_score:
    print(f"Az első játékos nyert {p1_score - p2_score} ponttal!")
elif p2_score > p1_score:
    print(f"A második játékos nyert {p2_score - p1_score} ponttal!")
else:
    print("Döntetlen")




