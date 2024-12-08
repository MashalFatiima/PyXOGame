# Python_GUI_PyGame_TicTacToe
# Tic-Tac-Toe Game

This project is a simple Tic-Tac-Toe game built using Python and the `pygame` library. The game features a graphical interface where two players can play Tic-Tac-Toe against each other on a 3x3 grid. The goal is to align three of your marks (either "X" or "O") in a row, column, or diagonal.

## Features

- **Two-player mode**: Players alternate turns to place either an "X" or an "O" on the grid.
- **Graphical interface**: The game is visually displayed using `pygame`, with a clean and simple grid layout.
- **Win detection**: The game checks for a win condition (Vertical, Horizontal, or Diagonal).
- **Game reset**: Players can press the "R" key to restart the game after it ends.
- **Game over handling**: Highlights the winning combination or ends the game if there's a tie.

## Dependencies

- Python 3.x
- `pygame` library
- `numpy` library

## Code Overview

### Main Components

- **`draw_lines(color=WHITE)`**:  Draws the grid lines for the Tic-Tac-Toe board.
- **`draw_figures(color=WHITE)`**: Draws the circles ("O") and crosses ("X") based on player moves.
- **`mark_square(row, col, player)`**: Marks a square with the player's symbol (either 1 or 2).
- **`available_square(row, col)`**: Checks if a square is available for a move.
- **`is_board_full()`**: Checks if all squares on the board have been filled, indicating a tie if no player has won.
- **`check_win(player)`**: Checks if a player has won by aligning three marks.
- **`win_line()`**: If a player win's, then winning line is drawn.
- **`restart_game()`**: Resets the game board and allows a new game to start.


### Game Flow

1. **Player Alternation**: Players alternate turns clicking on the grid to place their mark.
2. **Win or Tie Detection**: The game checks for a winner after each move or a tie if the board is full.
3. **Restart Option**: Press the "R" key to restart the game.

## Controls

- **Click**: Place your mark ("O" or "X") on the grid by Mouse Click.
- **R key**: Restart the game after it ends (either by a win or a tie).

## Game Over Conditions

1. **Win**: When a player aligns three marks in a row, column, or diagonal.
  <br>
   The game is over:
   - `Player 1's winning` combination is highlighted in **green** and winning line is drawn.
   - `Player 2's winning` combination is highlighted in **red** and winning line is drawn.

2. **Tie**: If the board is full and no player has won.
   - In the case of a `tie`, the board is highlighted in **gray**.

## How to Run

1. Make sure you have Python installed on your system.
2. Install the required libraries using pip:
   ```bash
   pip install pygame numpy
3. Save the code in a .py file and run it.
    ```bash
    python main.p