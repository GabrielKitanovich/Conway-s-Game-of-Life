# Conway's Game of Life

Conway's Game of Life is a cellular automaton devised by the British mathematician John Conway. It is a zero-player game, meaning that its evolution is determined by its initial state, with no further input from humans.

## Rules

The Game of Life is played on a two-dimensional grid of cells, where each cell can be either alive or dead. The following rules determine the evolution of the board:

1. **Underpopulation:** A live cell with fewer than two live neighbors dies.
2. **Survival:** A live cell with two or three live neighbors survives.
3. **Overpopulation:** A live cell with more than three live neighbors dies.
4. **Reproduction:** A dead cell with exactly three live neighbors becomes alive.

## How to Run the Code

1. Clone this repository to your local machine.
2. Open a terminal and navigate to the repository directory.
3. Run the `main.py` script using a Python interpreter:
    ```bash
    python main.py
    ```
4. Choose between generating a random board or using a preexisting one.
5. If you choose a preexisting board, select from a list of patterns, including Toad, Bullet, Beacon, Blinker, and Gosper Glider Gun.

## Functionality

### 1. Generating a Random Board

You can choose to generate a random initial board by entering the desired height and width.

### 2. Trying a Preexisting Board

Selecting a preexisting board allows you to experience different patterns in the Game of Life. Patterns include Toad, Bullet, Beacon, Blinker, and Gosper Glider Gun.

### 3. Board Rendering

The state of the board is rendered with symbols:
- ■ represents an alive cell.
- ❏ represents a dead cell.

### 4. Board Evolution

The Game of Life board evolves iteratively based on the defined rules. The evolution is displayed on the terminal, and the game continues until manually stopped.

## Repository Structure

- `main.py`: The main script containing the Game of Life implementation and user interaction.
- `functions.py`: Module with functions for random board generation, rendering, and board evolution.
- `examples/`: Directory containing example board patterns saved as text files.
- `README.md`: This README file providing information on how to use and run the Game of Life.

Feel free to explore and experiment with different patterns in the Game of Life!
