#MILESTONE 3:

# Ask the user to guess a letter & check that the guess is a single alphabetical character.

while True: 
    guess = input("Guess a letter: ")  

    if len(guess) == 1 or guess.isalpha():  
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

#%%

# Create an if statement that checks if the guess is in the word.

secret_word = "apple"

if guess in secret_word:
    print(f"Good guess! '{guess}' is in the word.")
else:
    print(f"Sorry, '{guess}' is not in the word. Try again.")

#%%

def check_guess(guessed_letter):

    guessed_letter = guessed_letter.lower()
    
    if guessed_letter in secret_word:
        print(f"Good guess! '{guessed_letter}' is in the word.")
    else:
        print(f"Sorry, '{guessed_letter}' is not in the word. Try again.")

    # This function takes an input and checks if it's in the secret_word.
    # Args:
    #       str: a single alphabetical letter
    # Returns:
    #       str: "Good guess! '{guessed_letter}' is in the word." - If the letter is in the word.
    #       str: "Sorry, '{guessed_letter}' is not in the word. Try again." - If the letter is not in the word.

def ask_for_input():

    while True:
        guessed_letter = input("Guess a letter: ")
        if len(guessed_letter) == 1 or guessed_letter.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.") 

    # This function checks if the letter is single and alphabetical.
    # Args: None
    # Returns:
    #       str: "Invalid letter. Please, enter a single alphabetical character." - If the input is not single or alphabetical.

    check_guess(guessed_letter) 
ask_for_input() 

