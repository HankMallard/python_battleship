# Setting up a 5 by 5 board
board = []
for i in range(5):
    i = ["O"] * 5
    board.append(i)

# Printing out the board
def print_board(board):
    for row in board:
        print row
