while True:
    rounds = int(input("Hány körös legyen a játék (csak páratlan számot adj meg)? "))
    
    if rounds % 2 == 0:
        print("Melyik részét nem értetted annak hogy pá-rat-lan?")
        continue
    break

player1_score = 0
player2_score = 0

# Körök indítása
for round_num in range(1, rounds + 1):
    print(f"\n--- {round_num}. kör ---")
    
    
    while True:
        # Játékos 1 inputja
        while True:
            player1_choice = input("Játékos 1, válassz (rock/paper/scissors): ").lower()
            if player1_choice in ["rock", "paper", "scissors"]:
                break
            else:
                print("Csak 'rock', 'paper' vagy 'scissors' lehet!")
        
        # Játékos 2 inputja
        while True:
            player2_choice = input("Játékos 2, válassz (rock/paper/scissors): ").lower()
            if player2_choice in ["rock", "paper", "scissors"]:
                break
            else:
                print("Csak 'rock', 'paper' vagy 'scissors' lehet!")
        
        # Játék kiértékelés
        winner = 0
        
        if player1_choice == player2_choice:
            winner = 0  
        elif (player1_choice == "rock" and player2_choice == "scissors") or \
             (player1_choice == "scissors" and player2_choice == "paper") or \
             (player1_choice == "paper" and player2_choice == "rock"):
            winner = 1
        else:
            winner = 2
        
        if winner==0:
            print("Döntetlen! Játsszátok újra ezt a kört.")
        else:
            if winner == 1:
                player1_score += 1
                print(f"Játékos 1 nyerte ezt a kört! ({player1_choice} vs {player2_choice})")
            else:
                player2_score += 1
                print(f"Játékos 2 nyerte ezt a kört! ({player1_choice} vs {player2_choice})")
            
            print(f"Állás: Játékos 1: {player1_score} - Játékos 2: {player2_score}")
            break  


print("\n")
print("VÉGEREDMÉNY")
print(f"Játékos 1: {player1_score} pont")
print(f"Játékos 2: {player2_score} pont")

if player1_score > player2_score:
    print(f"\nJátékos 1 nyert {player1_score - player2_score} ponttal!")
else:
    print(f"\nJátékos 2 nyert {player2_score - player1_score} ponttal!")