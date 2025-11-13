# rock paper scissors

i_round_counter=1

a_player_point=0 #A
b_player_point=0 #B
a_player_collected_points=0 #a
b_player_collected_points=0 #b

while True:
    rounds= int(input("How many rounds shall we play? (it has to be odd): "))
    round=int(rounds)
    if rounds % 2 == 1:
        break
    print(f"Wrong data because it isn't odd! Let's do it agan.")


print(f"It's ok. There will be {round} round(s).  Let's start it!")

answer_a_player=""
answer_b_player=""



while  i_round_counter<=round:

    while True:
        answer_a_player = input("Player 'A' Enter your choice from these: stone or scissors or paper ").strip()
        while answer_a_player not in ("stone","scissors","paper"):
            print (f" Wrong data from 'A' player: {answer_a_player} Let's write it agan.")
            answer_a_player = input("Player 'A' Enter your choice from these: stone or scissors or paper ").strip()
        else: 
            print(f"Player 'A' {i_round_counter} choice is:{answer_a_player}")
            break
      
    while True:
        answer_b_player = input("Player 'B' Enter your choice from these: stone or scissors or paper ").strip()
        while answer_b_player not in ("stone","scissors","paper"):
            print (f" Wrong data from 'B' player: {answer_b_player} Let's write it agan.")
            answer_b_player = input("Player 'A' Enter your choice from these: stone or scissors or paper ").strip()
        else: 
            print(f"Player 'A' {i_round_counter} choice is:{answer_b_player}")
            break

    # POINTS CALCULATOR
  
    if (
        (answer_a_player == "stone" and answer_b_player == "scissors") or
        (answer_a_player == "scissors" and answer_b_player == "paper") or
        (answer_a_player == "paper" and answer_b_player == "stone")
    ):
        a_player_point, b_player_point = 1, 0  # A wins
    else:
        a_player_point, b_player_point = 0, 1  # B wins

    # SUMM of points
  
    a_player_collected_points=a_player_collected_points+a_player_point
    b_player_collected_points=b_player_collected_points+b_player_point
    print(f" 'A' player has {a_player_point} points in this {i_round_counter} round and she/he collects :{a_player_collected_points} points till now")
    print(f" 'B' player has {b_player_point} points in this {i_round_counter} round and she/he collects :{b_player_collected_points} points till now")
   
    i_round_counter=i_round_counter+1


print(f" The 'A' player collects at the end of this game :{a_player_collected_points} points")
print(f" The 'B' player collects at the end of this game :{b_player_collected_points} points")


if a_player_collected_points>b_player_collected_points:
    print(f"The WINNER is the 'A' player!")
elif b_player_collected_points>a_player_collected_points:
     print(f"The WINNER is the 'B' player!")



