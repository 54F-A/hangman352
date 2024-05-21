import random


class Hangman:
    """A class to represent a game of Hangman.

    Attributes:
        word (str): The word to be guessed.
        word_guessed (list): A list representing the guessed letters
                             of the word.
        num_letters (int): The number of unique letters in the word.
        num_lives (int): The number of lives the player has.
        word_list (list): A list of fruit from which the secret 
                          word is chosen.
        list_of_guesses (list): A list to store the guessed letters.
    """

    def __init__(self, word_list, num_lives=5):
        """Initialises the Hangman game with a word and number of lives.

        Args:
            word_list (list): A list of fruit.
            num_lives (int): Number of lives for the player.
        """
        self.word = random.choice(word_list)    
        self.word_guessed = ['_' for _ in range(len(self.word))]       
        self.num_letters = len(set(self.word))     
        self.num_lives = num_lives     
        self.word_list = word_list      
        self.list_of_guesses = [] 

    def check_guess(self, guess):
        """Check if the guessed letter is in the word.

        Args:
            guess (str): The guessed letter.

        Returns:
            str: A message indicating if the guess was correct or not.
        """
        guess = guess.lower()   
        
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")     

            for element, letter in enumerate(self.word):        
                if letter == guess: 
                    self.word_guessed[element] = guess  
            self.num_letters = sum(1 for letter in self.word_guessed
                                   if letter == "_")

            print("Secret Word:", self.word_guessed)
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -=1
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        """Prompt the player to guess a letter.""" 
        while True:
            guess = input("Guess a letter: ")

            if len(guess) != 1 or not guess.isalpha():  
                print("Invalid letter. Please, enter a single \
                       alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!") 
            else:
                self.check_guess(guess) 
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    """Play the game of Hangman.

    Args:
        word_list (list): A list of fruit to choose from.
    """
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


if __name__ == "__main__":
    word_list = [
                 "apple", "banana", "grapes", 
                 "orange", "strawberry", "kiwi"
                ]
    play_game(word_list)

