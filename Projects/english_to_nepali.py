# Project 1 : English to Nepali Dictionary 
# o Create a simple English to Nepali dictionary using python dictionaries 
# o Allow the user to enter English word and display their Nepali tranlations 
# o Handle cases where the word is not found in the dictionary 

def english_to_nepali():
    dictionary = {
        "cat": "बिरालो",
        "dog": "कुकुर",
        "house": "घर",
        "water": "पानी",
        "sun": "घाम",
        "moon": "चन्द्र"
    }

    word = input("Enter an English word: ").lower()

    if word in dictionary:
        print("Nepali meaning:", dictionary[word])
    else:
        print("Word not found in dictionary!")