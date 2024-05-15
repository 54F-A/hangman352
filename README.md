# Hangman

## Table of Contents:

#### [1. What is Hangman?](#1-what-is-hangman)
#### [2. The Aim of the Project](#2-the-aim-of-the-project)
- #### [Milestone 2](#milestone-2)
- #### [Milestone 3](#milestone-3)
- #### [Milestone 4](#milestone-4)
- #### [Milestone 5](#milestone-5)
#### [3. Installation Instructions](#3-installation-instructions)
#### [4. Usage instructions](#4-usage-instructions)
#### [5. File structure of the project](#5-file-structure-of-the-project)
#### [6. License information](#6-license-information)

---

### What is Hangman?

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

---

### The Aim of the Project

The aim of the project is for the user to guess a single alphabetical letter of a secret word. The computer will print "Sorry, '{guessed letter}' is not in the word. Try again." if the letter guessed is not contained in the secret word. However, if it is contained in the word, the computer will print "Good guess! '{guessed letter}' is in the word."

#### Milestone 2:

Asks the user to input a guessed letter related to a list of words.

#### Milestone 3:

Asks the user to input a letter, if the letter is not in the secret word, the user may try again. There is no limit, the user may try as many times as possible until a correct letter is guessed.

#### Milestone 4:

Asks the user to input a letter, if the letter is not in the secret word, the user may try again. However, the user has a limited number of lives. For each incorrect letter, the user loses 1 life.

#### Milestone 5:

Asks the user to input a letter, if the letter is not in the secret word, the user may try again. However, the user has a limited number of lives. For each incorrect letter, the user loses 1 life. Once the user has no lives he has lost, but if the user correctly inputs all of the letters the user has won.

---

### Installation Instructions

To run the Hangman game, follow these steps:
1. Clone the repository to your local machine: __git clone https://github.com/54F-A/hangman352.git__
2. Navigate to the project directory: __cd hangman352__
3. Run the file to play the game: python milestone_5.py

---

### Usage instructions

Once you've installed the Hangman game, follow the instructions to play:
1. The computer will select a random word from a list.
2. Guess letters one at a time by entering them via keyboard input.
3. If the letter is in the word, it will print "Good guess! '{letter}' is in the word.".
4. If the letter is not in the word, it will print "Sorry, {letter} is not in the word.".
5. If the letter has already been used, it will print "You already tried that letter!".
6. If the letter is not a single alphabetical letter, it will print "Invalid letter. Please, enter a single alphabetical character.".
7. Keep guessing letters until you either guess the word correctly or run out of lives.

---

### File structure of the project

The file structure is as follows:
- __hangman.py__: The main Python script containing the Hangman game.
- __.gitignore__: A text file used by Git to specify intentionally untracked files that Git should ignore.
- __milestone_2.py__: A python file asking the user to input a single alphabetical letter.
- __milestone_3.py__: A python file converting a guessed letter into lower case and checking if it is in a randomly-selected word.
- __milestone_4.py__: A python file asking for a user to input a single alphabetical letter and reducing the number of lives if it is not contained in the randomly-selected word.
- __milestone_5.py__: A python file asking for a user to input a single alphabetical letter and reducing the number of lives if it is not contained in the randomly-selected word. This user input continues until the user has lost or won.
- __README.md__: A markdown file providing essential information about the hangman game.

---

### License information

This project is licensed under the MIT License.
