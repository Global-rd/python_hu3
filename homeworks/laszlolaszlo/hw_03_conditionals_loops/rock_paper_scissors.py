# Task 02

while True:
    max_game_rounds = input(
        "Please enter the number of game_rounds (only odd will accepted): "
    ).strip()

    if (
        max_game_rounds.isnumeric()
        and int(max_game_rounds) % 2 != 0
        and int(max_game_rounds) > 0
    ):
        max_game_rounds = int(max_game_rounds)
        break
    else:
        print(
            f"You have to enter an odd number larger than 0. You entered '{max_game_rounds}'"
        )

allowed_choices = {"rock", "paper", "scissors"}
user1_points = 0
user2_points = 0
game_round = 1

# Result mapping
rules = {
    ("paper", "rock"): "user1",
    ("paper", "scissors"): "user2",
    ("paper", "paper"): "draw",
    ("rock", "paper"): "user2",
    ("rock", "scissors"): "user1",
    ("rock", "rock"): "draw",
    ("scissors", "paper"): "user1",
    ("scissors", "rock"): "user2",
    ("scissors", "scissors"): "draw",
}

while game_round <= max_game_rounds:
    print(f"game_round {game_round}: ")
    result = ""

    while result not in ("user1", "user2"):
        # Ask user1 choice and validate it.
        while True:
            user1_choice = input(
                "User1, enter your choice (rock/paper/scissors): "
            ).strip()

            if user1_choice.lower() in allowed_choices:
                break
            else:
                print(
                    f"User1 have to enter one of the allowed values from 'rock, paper, scissors'. Try again!"
                )

        # Ask user2 choice and validate it.
        while True:
            user2_choice = input(
                "User2, enter your choice (rock/paper/scissors): "
            ).strip()
            if user2_choice.lower() in allowed_choices:
                break
            else:
                print(
                    f"User2 have to enter one of the allowed values from 'rock, paper, scissors'. Try again!"
                )

        result = rules[(user1_choice.lower(), user2_choice.lower())]

        if result == "user1":
            print(f"User1 won the game_round!")
            user1_points += 1
            break
        elif result == "user2":
            print("User2 won the game_round!")
            user2_points += 1
            break
        else:
            print("Draw, try again!")

    game_round += 1

if user1_points > user2_points:
    print(f"User1 won the game with {user1_points} vs {user2_points} points.")
else:
    print(f"User2 won the game with {user2_points} vs {user1_points} points.")
