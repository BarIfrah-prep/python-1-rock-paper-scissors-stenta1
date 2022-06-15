import random
import sys
Choice = {1:"rock", 2:"paper", 3:"scissors" }
winner = {1:3, 2:1, 3:2} # player win options

# Function to loop the game again
def rematch():
    player = int(input(print("choice : rock = 1, paper = 2, scissors = 3 ")))
    player_c = random.randint(1, 3)
    while player not in range(1, 4):
        player = int(input("Enter number in range 1-3"))
    while player in range(1, 4):
        if player == player_c:
            print(f"tie between you.\n  Player chioce:{Choice.get(player)},\n  Computer chioce:{Choice.get(player_c)}\nlet's try again.")
            player = int(input(print("choice : rock = 1, paper = 2, scissors = 3 ")))
            player_c = random.randint(1, 3)
        if winner.get(player) == player_c:
            print(f"You win the computer!\n  Player chioce:{Choice.get(player)},\n  Computer chioce:{Choice.get(player_c)}.")
            round_n = input(print("want another round ? \n y=yes, n=no"))
        else:
            print(f"You lose :(\n  Player chioce:{Choice.get(player)}\n  Computer chioce:{Choice.get(player_c)}.")
            round_n = input(print("Want another round ? \n y=yes, n=no"))
        while round_n not in ["y", "n"]:
            round_n = input("Enter only y/n")
            player_c = random.randint(1, 3)
        else:
            if round_n == "y":
                rematch()
            else:
                print("Thank you bye :)")
                sys.exit()


print("Welcome to a 'Rock, Paper, Scissors' game")
player = int(input(print("choice : rock = 1, paper = 2, scissors = 3 ")))
player_c = random.randint(1, 3)

# allow player number only
while player not in range(1, 4):
   player = int(input("Enter number in range 1-3"))

while player in range(1, 4):
    if player == player_c:
        print(f"tie between you.\n  Player chioce:{Choice.get(player)},\n  Computer chioce:{Choice.get(player_c)}\nlet's try again.")
        player = int(input(print("choice : rock = 1, paper = 2, scissors = 3 ")))
        player_c = random.randint(1, 3)
    if winner.get(player) == player_c:
        print(f"You win the computer!\n  Player chioce:{Choice.get(player)},\n  Computer chioce:{Choice.get(player_c)}.")
        round_n = input(print("want another round ? \n y=yes, n=no"))
    else:
        print(f"You lose :(\n  Player chioce:{Choice.get(player)}\n  Computer chioce:{Choice.get(player_c)}.")
        round_n = input(print("Want another round ? \n y=yes, n=no"))

    while round_n not in ["y", "n"]:
        round_n = input("Enter only y/n")
        player_c = random.randint(1, 3)
    else:
        if round_n == "y":
            rematch()

        else:
            print("Thank you bye :)")
            sys.exit()
















