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

# Defines a function that passes in a letter as a parameter for the function.

def check_guess(guessed_letter):

    # Converts the letter into lower case.

    guessed_letter = guessed_letter.lower()
    
    if guessed_letter in secret_word:
        print(f"Good guess! '{guessed_letter}' is in the word.")
    else:
        print(f"Sorry, '{guessed_letter}' is not in the word. Try again.")

# Defines a function called ask_for_input.

def ask_for_input():

    while True:
        guessed_letter = input("Guess a letter: ")
        if len(guessed_letter) == 1 or guessed_letter.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.") 

    # Calls the check_guess function to check if the letter is in the word & ask_for_input function to test your code.

    check_guess(guessed_letter) 
ask_for_input() 

