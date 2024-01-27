"""
Conway's Game of Life Simulator

This program simulates Conway's Game of Life, a cellular automaton devised by the mathematician John Conway. The game consists of a grid of cells, where each cell can be alive or dead. The state of the cells evolves through generations based on simple rules.

Usage:
1. Choose an option:
   - Generate a new random board (Option 1)
   - Try a preexisting board pattern (Option 2)
2. If selecting a new random board:
   - Enter the desired height and width for the random board.
3. If selecting a preexisting board pattern:
   - Choose a pattern from the available options (Toad, Bullet, Beacon, Blinker, Gospel Glider Gun).
4. The simulation will start, and each generation of the board will be displayed with a delay of 0.5 seconds.

Patterns available:
1) Toad
2) Bullet
3) Beacon
4) Blinker
5) Gospel Glider Gun

Note: To interrupt the simulation, press Ctrl+C.
"""
from functions import *
import time
def run_game(board_file):
    """
    Run the Game of Life simulation with a given board file.

    Args:
        board_file (str): The path to the file containing the initial board state.
    """
    print("Starting game...")
    time.sleep(2)
    board_state = load_board_state(board_file)
    while True:
        board_state = next_board_state(board_state)
        render(board_state)
        time.sleep(0.5)
print("\nWelcome to the Conway's Game of life!!")
board_state = []
while True:
    option = input("\nDo you wanna:\n 1) Generate a new random board \n 2) Try a preexisting board\n")
    if option == "1":
        height, width = int(input("Enter the height: ")), int(input("Enter the width: "))
        if height <= 0 and width <= 0:
            print("Please enter a new height and width!!!\n")
            continue
        board_state = random_state(height, width)
        print("Starting game...")
        time.sleep(2)
        while True:
            board_state = next_board_state(board_state)
            render(board_state)
            time.sleep(0.5)
    elif option == "2":
        print("----------------------------------------------------------------")
        option2 = input("1) Toad\n 2) Bullet\n 3) Beacon\n 4) Blinker\n 5) Gospel Glider Gun\n")
        pattern_files = {
            "1": "examples/toad.txt",
            "2": "examples/bullet.txt",
            "3": "examples/beacon.txt",
            "4": "examples/blinker.txt",
            "5": "examples/gospel.txt",
        }
        board_state = pattern_files.get(option2)
        if board_state:
            run_game(board_state)
        else:
            print("Please enter a valid board!!!")
            continue
    else: 
        print("Please enter a valid board!!!")
        continue
