import random

while True:
    choices = ["rock, paper, scissors"]
    computer = random.choices(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors ? : ").lower()

        if player == computer:
            print("computer: ", computer)
            print("player: ", player)
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Loser!")
            if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("winner!")
         elif player == "scissors":
            if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("Loser!")
            if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("winner!")
         elif player == "paper":
            if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("Loser!")
            if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("winner!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")