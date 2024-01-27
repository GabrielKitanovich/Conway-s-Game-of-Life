import random
"""
Conway's Game of Life Implementation

This Python script provides an implementation of Conway's Game of Life, a cellular automaton devised by the British mathematician John Conway. The Game of Life is a zero-player game, meaning that its evolution is determined by its initial state, with no further input from humans.

The script includes the following functions:

1. `random_state(board_height, board_width)`: Generate a random initial state for the Game of Life with the given board height and width.

2. `render(board)`: Render the current state of the Game of Life board with symbols ■ for alive cells and ❏ for dead cells.

3. `next_board_state(board)`: Update the given Game of Life board to its next state based on the rules.

4. `load_board_state(route)`: Load the initial state of the Game of Life board from a file.

5. `run_game(board_file)`: Run the Game of Life with a specified initial state from a file.

Usage:
- Choose between generating a random board or using a preexisting one.
- For preexisting boards, select from a list of patterns, including Toad, Bullet, Beacon, Blinker, and Gosper Glider Gun.

Note: The script contains explanatory comments and docstrings for each function.

"""
def random_state(board_height, board_width):
    """Initiate the board with the given board height and board width with 0 or 1

    Args:
        board_height (int): board height
        board_width (int): board width

    Returns:
        list: the final board
    """
    board = []
    
    for i in range(board_height):
        row = []
        for j in range(board_width):
            row.append(random.randint(0, 1))
        board.append(row)
    return board

def render(board):
    """render the board with the simbols ■ as alive and ❏ as dead

    Args:
        board (list): the board to render
    """
    print("--------------------------------")
    for row in board:
        for i in row:
            print("■", end= " ") if i == 1 else print("❏", end= " ")
        print("\n")

def next_board_state(board):
    """
    Update the given Game of Life board to its next state based on the rules.

    Args:
        board (list): 2D list representing the current state of the Game of Life.

    Returns:
        list: 2D list representing the updated state of the Game of Life.
    """
    rows, cols = len(board), len(board[0])
    new_board = [[0] * cols for _ in range(rows)]  # Create a new board to avoid in-place update issues

    for i in range(rows):
        for j in range(cols):
            neighbors = 0

            if (i == 0 or i == rows - 1) and (j == 0 or j == cols - 1):
                # Sum neighbors for corners excluding cells outside the boundaries
                neighbors += sum(board[x][y] for x in range(max(0, i - 1), min(rows, i + 2)) for y in range(max(0, j - 1), min(cols, j + 2)) if 0 <= x < rows and 0 <= y < cols)
                neighbors -= board[i][j]
            elif i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                # Sum neighbors for edges excluding cells outside the boundaries
                neighbors += sum(board[x][y] for x in range(max(0, i - 1), min(rows, i + 2)) for y in range(max(0, j - 1), min(cols, j + 2)) if 0 <= x < rows and 0 <= y < cols)
                neighbors -= board[i][j]
            else: 
                neighbors += sum(board[i - 1][k] for k in range(j - 1, j + 2)) + \
                            sum(board[i][k] for k in range(j - 1, j + 2)) + \
                            sum(board[i + 1][k] for k in range(j - 1, j + 2))
                neighbors -= board[i][j]

            if board[i][j] == 1:
                # Live cell
                if neighbors < 2 or neighbors > 3:
                    new_board[i][j] = 0  # Dies due to underpopulation or overpopulation
                else:
                    new_board[i][j] = 1  # Stays alive
            else:
                # Dead cell
                if neighbors == 3:
                    new_board[i][j] = 1  # Comes alive due to reproduction

    return new_board
def load_board_state(route):
    """
    Load the initial state of the board from a file.

    Args:
        route (str): The path to the file containing the initial board state.

    Returns:
        list: A 2D list representing the initial state of the board. Each element is either 0 (dead cell) or 1 (alive cell).
    """
    board = []
    aux = []
    with open(route) as file:
        for line in file:
            aux= []
            for i in line:
                if i != '\n': aux.append(int(i)) 
            board.append(aux)
    return board