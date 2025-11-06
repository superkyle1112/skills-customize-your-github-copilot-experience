
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic word-guessing game using Python where players try to discover a hidden word by guessing one letter at a time, practicing core programming concepts like string manipulation, loops, and user input.

## 📝 Tasks

### 🛠️ Create the Word Selection System

#### Description
Create a system that randomly selects a word from a predefined list of words for the player to guess.

#### Requirements
Completed program should:

- Create a list of at least 10 words for the game to choose from
- Implement random word selection using Python's random module
- Convert the selected word into a hidden format (using underscores)

### 🛠️ Implement Game Mechanics

#### Description
Build the main game loop that handles player input, tracks progress, and manages the game state.

#### Requirements
Completed program should:

- Accept and validate letter guesses from the player
- Display the word with correctly guessed letters revealed and others hidden (_ _ _ format)
- Track and display the number of incorrect guesses remaining
- Show all previously guessed letters
- End the game when either the word is fully guessed or attempts are exhausted
- Display appropriate win/lose messages with the correct word revealed
