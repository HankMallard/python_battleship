from random import randint
# Setting up a 5 by 5 board
board = []
for i in range(5):
    i = ["O"] * 5
    board.append(i)

# Printing out the board
def print_board(board):
    for row in board:
        print row

print_board(board)

# Creating a battleship at a random location
def random_row(board):
    return randint(0, len(board)-1)

def random_col(board):
    return randint(0, len(board)-1)

#actual location of the battleship
ship_row = random_row(board)
ship_col = random_col(board)

#User input on the location of the battleship
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:")) 
