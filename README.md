# Hangman

## Table of Contents:

#### [1. What is Hangman?](#1-what-is-hangman)
#### [2. The Aim of the Project](#2-the-aim-of-the-project)
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

---

### Installation Instructions

To run the Hangman game, follow these steps:
1. Clone the repository to your local machine: __git clone https://github.com/54F-A/hangman352.git__
2. Navigate to the project directory: __cd hangman__
3. Run the game: __python hangman.py__

---

### Usage instructions

Once you've installed the Hangman game, follow the instructions to play:
1. The computer will select a word and display blanks representing each letter of the word.
2. Guess letters one at a time by entering them via keyboard input.
3. If the letter is in the word, it will be revealed in the blanks. If not, you'll lose a life.
4. Keep guessing letters until you either guess the word correctly or run out of lives.

---

### File structure of the project

The file structure is as follows:
- __hangman.py__: The main Python script containing the Hangman game.
- __.gitignore__: A text file used by Git to specify intentionally untracked files that Git should ignore.
- __milestone_2.py__: A python file asking the user to input a single alphabetical letter.
- __milestone_3.py__: A python file converting a guessed letter into lower case and checking if it is in a secret word.
- __README.md__: A markdown file providing essential information about the hangman game.


---

### License information

This project is licensed under the MIT License.
