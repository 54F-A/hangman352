import random

# Create a list containing the names of your 5 favorite fruits.

list_of_fruit = ["Apple", "Banana", "Grapes", "Orange", "Strawberry"]

# Print out the newly created list to the standard output (screen).

print(list_of_fruit)

# Create the random.choice method and pass the variable into the choice method.
# Assign the randomly generated word to a variable.

chosen_fruit = random.choice(list_of_fruit)

# Print out word to the standard output.

print(chosen_fruit)

# Using the input function, ask the user to enter a single letter.
# Assign the input to a variable.
# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
# In the body of the if statement, print a message that says "Good guess!".
# Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.

chosen_letter = input("Enter a single letter: ")
if len(chosen_letter) == 1 and chosen_letter.isalpha():
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")

