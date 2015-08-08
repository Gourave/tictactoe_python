# Prints out the game board in a way the user can see it nicely
def print_board(board):
    for row in board:
        print (" ").join(row)

# Checks to see if there is a winner yet
def check_winner():
    return False

if __name__ == "__main__":
    # Setup the game board
    board = []
    for i in range(0, 3):
        board.append(["- | - | -"])

    # Prompt the user to see whether he/she would like to play the computer or not
    print "Welcome to TicTacToe"
    game_choice = raw_input("Would you like to play with another player, or the computer? ")

    # If the input was of incorrect format, ask the user again until he/she gets it right
    while game_choice != "player" and game_choice != "computer":
        print "Please enter either 'player' or 'computer'"
        game_choice = raw_input("Would you like to play with another player, or the computer? ")

    # Prints the game board out
    print_board(board)