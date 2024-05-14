# Create a while loop and set the condition to True.
while True:

# Ask the user to guess a letter and assign this to a variable called guess.
    guess = input("Guess a letter: ")

# Check that the guess is a single alphabetical character. 
    if len(guess) == 1 and guess.isalpha():

# If the guess passes the checks, break out of the loop.
        break

# If the guess does not pass the checks:
# Print a message saying "Invalid letter. Please, enter a single alphabetical character."
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

#%%

# Create an if statement that checks if the guess is in the word.
secret_word = "apple"

if guess in secret_word:

# In the body of the if statement, print a message saying: 
# "Good guess! {guess} is in the word.".
    print(f"Good guess! '{guess}' is in the word.")

# Create an else block that prints a message saying:
# "Sorry, {guess} is not in the word. Try again."
else:
    print(f"Sorry, '{guess}' is not in the word. Try again.")

#%%

# Define a function called check_guess. pass in the guess as a parameter for the function.
def check_guess(guess):

# Convert the guess into lower case.
    guess = guess.lower()
    
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# Define a function called ask_for_input.
def ask_for_input():

    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. 
    check_guess(guess)
    
# Outside the function, call the ask_for_input function to test your code.
ask_for_input()