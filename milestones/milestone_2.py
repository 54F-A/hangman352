#MILESTONE 2:

import random

list_of_fruit = ["apple", "banana", "grapes", "orange", "strawberry"]

# Creates a list containing the names of your 5 favorite fruits.

if __name__ == "__main__":
    print(list_of_fruit)  

    # Prints out a created list to the standard output.  

    chosen_fruit = random.choice(list_of_fruit) 
    print(chosen_fruit) 

    # prints a randomly generated word from a list.  
    
    chosen_letter = input("Enter a single letter: ")    
    if len(chosen_letter) == 1 or chosen_letter.isalpha():  
        print("Good Guess!")
    else:
        print("Oops! That is not a valid input.")   
    
    # Ask the user to input a letter & check if the length of the input is equal to 1 and is alphabetical.

