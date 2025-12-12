# Project: Word counter 
# Create a command-line program that counts the number of unique words in a sentence 

def word_counter():
    
    sentence = input("Enter a sentence: ")

    sentence = sentence.lower().strip()
    words = sentence.split()
    unique_words = set(words)

    print("\nTotal words:", len(words))
    print("Unique words:", len(unique_words))
    print("Unique list:", unique_words)
