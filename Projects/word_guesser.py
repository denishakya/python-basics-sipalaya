# Project : simple word guesser 
# o Create a game where user tries to guess a random generator word 
# o Provide hint which letter is startwith 
# o Use recursion function to play again

import random

def word_guesser():
    words = ["apple", "banana", "orange", "mango", "grape"]
    word = random.choice(words)
    print(f"Hint: The word starts with '{word[0]}'")

    guess = input("Guess the word: ").lower()

    if guess == word:
        print("Correct! You guessed the word.")
    else:
        print(f"Wrong! The word was '{word}'.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        word_guesser()
    else:
        print("Thanks for playing!")

word_guesser()
