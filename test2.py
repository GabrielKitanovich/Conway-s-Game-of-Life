from functions import *
import time
board = load_board_state("examples/bullet.txt")
render(board)
while True:
    board = next_board_state(board)
    render(board)
    time.sleep(0.3)