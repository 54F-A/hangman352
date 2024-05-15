#MILESTONE 5:

import random

word_list = ["apple", "banana", "grapes", "orange", "strawberry"]

# Create a class called Hangman.

class Hangman:  

    def __init__(self, word_list, num_lives=5):

        self.word = random.choice(word_list)    

        self.word_guessed = ['_' for _ in range(len(self.word))]       

        self.num_letters = int(len(set(self.word)))     

        self.num_lives = num_lives     
        
        self.word_list = word_list      
        
        self.list_of_guesses = [] 

        # This function is an initializer method for a class.
        # Args:
        #       word_list (list): a list of fruit.
        #       num_lives (int): an integer defining the number of lives

    def check_guess(self, guess):
        guess = guess.lower()   
        
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")     

            for element, letter in enumerate(self.word):        
                if letter == guess: 
                    self.word_guessed[element] = guess  
            self.num_letters = sum(1 for letter in self.word_guessed if letter == "_")  
            
            print("Secret Word:", self.word_guessed)

        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -=1
            print(f"You have {self.num_lives} lives left.")
    
        # This function is designed to check a guessed letter against a word the player is trying to guess. 
        # Args:
        #       guess (str): a single alphabetical letter
        # Returns:
        #       str: "Good guess! '{guess}' is in the word." - If the letter is in the word.
        #       str: "Sorry, {guess} is not in the word." - If the letter is not in the word.
        #       str & int: "You have {self.num_lives} lives left." - If the letter is not in the word.

    def ask_for_input(self): 

        while True:

            guess = input("Guess a letter: ")

            if len(guess) != 1 or not guess.isalpha():  
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!") 
            else:
                self.check_guess(guess) 
                self.list_of_guesses.append(guess)
            if self.num_letters == 0 or self.num_lives == 0:
                break

        # This function prompts the user to guess a letter for the word they are trying to guess.
        # Args: None
        # Returns:
        #       str: "Invalid letter. Please, enter a single alphabetical character." - If the input doesn't meet the conditions.
        #       str: "You already tried that letter!" - If the input is a repeat value.

def play_game(word_list):

    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_letters == 0:
            print("Congratulations. You won the game!")
            break
        elif game.num_lives == 0:
            print("You Lost!")
            break
        else:
            game.ask_for_input()

        # This function is a Python function designed to play a game of Hangman 
        # Args:
        #       word_list (list): a list of fruit.
        # Local Variables:
                # num_lives (int): This variable is set to 5, representing the number of lives.
                # game: This variable initializes an instance of the Hangman game with the word list and the number of lives.
        # Returns:
        #       str: "Congratulations. You won the game!" - If all the letters of the word are found.
        #       str: "You Lost!" - If the lives run out.

play_game(word_list)

