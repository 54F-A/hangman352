#MILESTONE 4:

import random
from milestone_2 import list_of_fruit

word_list = list_of_fruit

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
        #       word_list: a list of fruit.
        #       num_lives: an integer defining the number of lives

    def check_guess(self, guess):
        guess = guess.lower()   
        
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")     

            for element, letter in enumerate(self.word):        
                if letter == guess: 
                    self.word_guessed[element] = guess  
            self.num_letters -= 1       
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

        # This function is designed to check a guessed letter against a word the player is trying to guess. 
        # Args:
        #       guess: a single alphabetical letter

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

        # This function prompts the user to guess a letter for the word they are trying to guess.

hangman_game = Hangman(word_list)
hangman_game.ask_for_input()
