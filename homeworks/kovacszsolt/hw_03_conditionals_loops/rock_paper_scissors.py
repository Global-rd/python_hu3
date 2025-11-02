# rock paper scissors

round=2
i=1

A=0
B=0
a=0
b=0

while round %2==0 :
    rounds= input("How many rounds shall we play? (it has to be odd): ")
    round=int(rounds)
    print(round)
    if round %2==0:
        print (f" Wrong data because it isn't odd! Let's do it agan.")
print(f"It's ok. There will be {round} round(s).  Let's start it!")

answer_a_player=""
answer_b_player=""



while  i<=round:

    

    answer_a_player = input("Player 'A' Enter your choice from these: stone or scissors or paper ").strip()
    
    while answer_a_player not in ("stone","scissors","paper"):
        print (f" Wrong data from 'A' player: {answer_a_player} Let's write it agan.")
        answer_a_player = input("Player 'A' Enter your choice from these: stone or scissors or paper ").strip()
    else: 
        print(f"Player 'A' {i} choice is:{answer_a_player}")
        

    answer_b_player = input("'B' Player Enter your choice from these: stone or paper or scissors ").strip()

    while answer_b_player not in ("stone","scissors","paper"):
            print (f" Wrong data from 'B' player: {answer_b_player} Let's write it agan .")
            answer_b_player = input("'B' Player Enter your choice from these: STONE or PAPER or SCISSORS ").strip()
    else: 
            print(f"'B' Player {i} choce is :{answer_b_player}")
        

    print(f"Number of round in this :{i}")
    print(f"Size of Round(s) :{round}")
    i+=1

    # POINTS CALCULATOR
    if answer_a_player==answer_b_player:
        A=0
        B=0
       

        print(f"There is no winner in this {i-1} round so we must repet it !")
        i=i-1

        continue

    elif answer_a_player=="stone" and answer_b_player=="paper":
        A=0
        B=1
    elif answer_a_player=="stone" and answer_b_player=="scissors":
        A=1
        B=0
    elif answer_a_player=="scissors" and answer_b_player=="stone":
        A=0
        B=1
    elif answer_a_player=="scissors" and answer_b_player=="paper":
        A=1
        B=0
    elif answer_a_player=="paper" and answer_b_player=="stone":
        A=1
        B=0
    elif answer_a_player=="paper" and answer_b_player=="scissors":
        A=0
        B=1
    
   
    a=a+A
    b=b+B
    print(f" 'A' player has {A} points in this {i-1} round and she/he collects :{a} points till now")
    print(f" 'B' player has {B} points in this {i-1} round and she/he collects :{b} points till now")
   

print(f" The 'A' player collects at the end of this game :{a} points")
print(f" The 'B' player collects at the end of this game :{b} points")


if a>b:
    print(f"The WINNER is the 'A' player!")
elif b>a:
     print(f"The WINNER is the 'B' player!")



