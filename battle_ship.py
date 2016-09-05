from random import randint
# Setting up a 5 by 5 board
board = []
for x in range(5):
    board.append(["O"] * 5)

# Printing out the board
def print_board(board):
    for row in board:
        print (row)

print ("Let's Play Battleship!")
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
guess_row = (input("Guess Row:"))
guess_col = (input("Guess Col:"))

# Includes all possible outcome of the game
for turn in range(4): # Added 4 turn per game!
    print ("Turn", turn + 1)
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print ("Oops! You've gone too far!")
        elif(board[guess_col][guess_col] == "X"):
            print ("You've been there before! Move on please!")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)
            if turn == 3:
                print ("Game Over!")
