import os
import time

# Képernyő törlés.
os.system('cls' if os.name == 'nt' else 'clear')

# Győzelmi feltételek tárolása egy mátrixban.
win_conditions = [
    ["r","s"], # A kő/rock(r) üti az ollót/scissor(s)
    ["p","r"], # A papír/paper(p) üti a követ/rock(r)
    ["s","p"], # Az olló/scissor(s) üti a papírt/paper(p)
]

# A szükséges változók létrehozása
i = 1
player1_score = 0
player2_score = 0
congrat = "won the game. Congratulations!"
symbols = ["r","p","s"]

# Játékos- és játékadatok bekérése.
player1_name = input("Player1 name? : ").replace(" ","")  # Az első játékos neve és a szóközök eltávolítása.
player2_name = input("Player2 name? : ").replace(" ","")  # A második játékos neve és a szóközök eltávolítása.
rounds = int(input("How many rounds would you like to play?: ")) # A játszani kívánt körök száma

# A körök számának bekérése és vizsgálata, a döntetlen elkerölése céljából
while rounds % 2 == 0: 
    print("Please choose an odd number to avoid a draw!")
    rounds = int(input("How many rounds would you like to play?: ")) 

# A játék lebonyolítása, és az aktuális állás képernyőre írása.
while i <= rounds:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--------Score Board----------")
    print(f"{player1_name}: {player1_score}")
    print(f"{player2_name}: {player2_score}")
    print(f"-----------------------------")
    
    player1_choice = input(f"So {player1_name}, what did you pick? Rock(r), Paper(p) or Scissor(s)?: ").lower()
    while player1_choice not in symbols:
        print(player1_choice)
        player1_choice = input(f"{player1_name}, Please choose from the followings! Rock(r), Paper(p) or Scissor(s)?: ").lower()  
   
    player2_choice = input(f"Alright {player2_name}, Show your hand! Rock(r), Paper(p) or Scissor(s)?: ").lower()
    while player2_choice not in symbols:
        print(player2_choice)
        player2_choice = input(f"{player2_name}, Please choose from the followings! Rock(r), Paper(p) or Scissor(s)?: ").lower()
    
    if player1_choice == player2_choice: # Döntetlen
        print(f"--------------------------------------------")
        print(f"IT IS A TIE! No points awarded!")
        print(f"--------------------------------------------")
        time.sleep(3)
    elif [player1_choice, player2_choice] in win_conditions: # Player 1 nyert.
        player1_score += 1
        print(f"--------------------------------------------")
        print(f"{player1_name} WON!!!!")
        print(f"--------------------------------------------")
        time.sleep(3)
        i += 1
    else:
        player2_score += 1 # Player 2 nyert.
        print(f"--------------------------------------------")
        print(f"{player2_name} WON!!!!")
        print(f"--------------------------------------------")
        time.sleep(3)
        i += 1
               

# A végső pontszám és a győztes nevének kiírása       
os.system('cls' if os.name == 'nt' else 'clear')
print(f"--------FINAL SCORE----------")
print(f"{player1_name}: {player1_score}")
print(f"{player2_name}: {player2_score}")
print(f"-----------------------------")
print(f"{player1_name} {congrat}" if player1_score > player2_score else f"{player2_name} {congrat}")