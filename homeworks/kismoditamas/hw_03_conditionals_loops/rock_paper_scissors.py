import os
import platform

if platform.system() == "Windows":
    clear_string="cls"
else:
    clear_string="clear"

player1_score = 0 
player2_score = 0

print("Rock - paper - scissors game")

while True:
    games = int(input("Enter the number of rounds: "))    
    if games % 2 ==0:
        print("An even number of rounds may result in a draw. Enter an odd number.")
    else:
        break

for game in range(1, games+1):
     while True:
        while True:
            player1_answer = input("Choose Player 1 (rock / paper / scissors): ").lower()
            if player1_answer.lower() in ["rock","r","paper","p","scissors","s"]:
                os.system(clear_string)
                break
            else:
                print("The answer can only be rock, paper, or scissors.")
        
        while True:
            player2_answer = input("Choose Player 2 (rock / paper / scissors): ").lower()
            if player2_answer.lower() in ["rock","r","paper","p","scissors","s"]:
                os.system(clear_string)
                break
            else:
                print("The answer can only be rock / r, paper / p or scissors / s.")

						if player1_answer != player2_answer:
    										if (
     											   (player1_answer in ["rock", "r"] and player2_answer in ["scissors", "s"]) or
  											      (player1_answer in ["paper", "p"] and player2_answer in ["rock", "r"]) or
    	 											   (player1_answer in ["scissors", "s"] and player2_answer in ["paper", "p"])
    											):
      												  player1_score += 1
    											else:
      												  player2_score += 1

 							   print(f"Game: {games} / {game} - Player 1 score: {player1_score} - Player 2 score: {player2_score}")
   						 break
						else:
    						print("It's a tie, play again.")
      
```  if player1_answer != player2_answer:
            if player1_answer.lower() in ["rock","r"]:
                if player2_answer.lower() in ["paper","p"]:
                    player2_score += 1                         
                else:
                    player1_score += 1                                         
            elif player1_answer.lower() in ["paper","p"]:
                if player2_answer.lower() in ["rock","r"]:
                    player1_score += 1                         
                else:
                    player2_score += 1 
            else:
                if player2_answer.lower() in ["paper","p"]:
                    player1_score += 1                         
                else:
                    player2_score += 1 
            
            print(f"Game: {games} / {game} - Player 1 score: {player1_score} - Player 2 score: {player2_score}")
            break                 
        else:
            print("It's a tie, play again.")```

result = 1 if player1_score > player2_score else 2
print(f"The Player {result} won by {abs(player1_score-player2_score)} points!")