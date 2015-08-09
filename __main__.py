# Prints out the game board in a way the user can see it nicely
def print_board(board):
    for row in board:
        print (" ").join(row)


if __name__ == "__main__":
    # Setup the game board
    board = []
    for i in range(0, 3):
        board.append(["- | - | -"])

    # Magic square to hold the values of each tile
    # Used to determine a winner
    magic_square = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

    # Prompt the user to see whether he/she would like to play the computer or not
    print "Welcome to TicTacToe"
    game_choice = raw_input("Would you like to play with another 'player', or the 'computer?' ")

    # If the input was of incorrect format, ask the user again until he/she gets it right
    while game_choice != "player" and game_choice != "computer":
        print "Please enter either 'player' or 'computer'"
        game_choice = raw_input("Would you like to play with another player, or the computer? ")

    if game_choice == "player":
        print "Playing against another player"
        # Put code here for multiplayer game
    else:
        print "Playing against the computer"
        # Put code here for Ai game

    # Prints the game board out
    print_board(board)
