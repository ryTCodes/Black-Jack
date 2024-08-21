# Blackjack Game

This is a simple command-line Blackjack game implemented in Python. The game follows the classic rules of Blackjack, where the player tries to beat the computer by getting a hand as close to 21 as possible without going over.

## Features

- **Deal Cards:** Randomly deal cards to both the player and the computer.
- **Calculate Score:** The score is calculated based on the sum of card values, with special rules for aces (which can count as either 1 or 11).
- **Compare Scores:** The game compares the player's and the computer's scores to determine the winner.
- **Clear Terminal:** The terminal is cleared at the start of each game round using `os.system('cls')`, which works in Visual Studio Code.
- **Replay Option:** The player can choose to play multiple rounds.

## How to Play

1. **Start the Game:** Run the script, and you'll be prompted to start a new game by typing `'y'` or `'n'`.
2. **Deal Cards:** Two cards are dealt to both the player and the computer.
3. **Player's Turn:** The player can choose to draw another card (`'y'`) or pass (`'n'`).
4. **Computer's Turn:** The computer draws cards until its score is 17 or higher.
5. **Determine Winner:** The final scores are compared, and the winner is announced.
6. **Replay:** After the game ends, you can choose to start a new game.

## Requirements

- Python 3.x
- `random` module (pre-installed with Python)
- `os` module (pre-installed with Python)
- `art` module for displaying the game logo

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/blackjack-game.git
    ```

2. Navigate to the project directory:

    ```bash
    cd blackjack-game
    ```

3. Run the game:

    ```bash
    python blackjack.py
    ```

## Game Rules

- The goal is to have a hand with a value as close to 21 as possible without exceeding it.
- Numbered cards (2-10) are worth their face value.
- Face cards (Jack, Queen, King) are worth 10 points.
- Aces can be worth 1 or 11 points, depending on what benefits the hand.
- A Blackjack is when a hand contains an Ace and a 10-point card, summing exactly to 21.
