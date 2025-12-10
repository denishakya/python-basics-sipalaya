import random

def play_game():
    # Word list
    word_list = ["apple", "banana", "python", "computer", "school", "river", "mobile", "dance"]

    # Select random word
    secret_word = random.choice(word_list)

    print("\n====== WORD GUESSING GAME ======")
    print(f"Hint: The word starts with '{secret_word[0]}'")
    print(f"Length: {len(secret_word)} letters")

    # User guess
    guess = input("Your guess: ").strip().lower()

    # Check guess
    if guess == secret_word:
        print("\nCorrect! You guessed the right word!")
    else:
        print(f"\nOops! Wrong guess. The correct word was: '{secret_word}'")

    # Ask user to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if play_again == "yes":
        play_game()  # recursion
    else:
        print("\nThanks for playing! Goodbye")


# Start the game
play_game()
