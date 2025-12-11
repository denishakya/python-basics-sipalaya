# Project: Sissor, Papper, Rock game 

import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = input("Enter rock, paper, or scissors: ").lower()

    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("Computer wins!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid choice!")
