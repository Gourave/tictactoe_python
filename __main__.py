# Prints out the game board in a way the user can see it nicely
def print_board(board):
    for row in board:
        print " ".join(row)

# Check to see whether there is a winner or not
# TODO: Clean up the if loops, im not feeling the code...
def winner(board, magic_square):
    if not check_horizontal(board, magic_square):
        if not check_vertical(board, magic_square):
            # Put code here to check diagonal and anti-diagonal lines
            return False

def check_horizontal(board, magic_square):
    player_one_score = 0
    player_two_score = 0
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            if board[row][col] == "X":
                player_one_score += magic_square[row][col]
            elif board[row][col] == "O":
                player_two_score += magic_square[row][col]
    # TODO: Issue is due to the if statement below
    if player_one_score == 15:
        print "Player 1 wins!"
        return True
    elif player_two_score == 15:
        print "Player 2 wins!"
        return True
    return False

def check_vertical(board, magic_square):
    player_one_score = 0
    player_two_score = 0
    for col in range(0, len(board)):
        for row in range(0, len(board)):
            if board[row][col] == "X":
                player_one_score += magic_square[row][col]
            elif board[row][col] == "O":
                player_two_score += magic_square[row][col]
    # TODO: Issue is due to the if statement below
    if player_one_score == 15:
        print "Player 1 wins!"
        return True
    elif player_two_score == 15:
        print "Player 2 wins!"
        return True
    return False


# Prompt the user to make a move and take up the spot that was specified by
# the players piece
def make_move(board, player):
    row = -1
    col = -1
    while not (-1 < row < 3):
        row = int(raw_input("Row: "))
    while not (-1 < col < 3):
        col = int(raw_input("Col: "))
    if board[row][col] != "-":
        print "This place has already been taken up. Please choose another spot."
        print_board(board)
        make_move(board, player)
    else:
        board[row][col] = player

if __name__ == "__main__":
    # Setup the game board
    board = []
    for i in range(0, 3):
        board.append(["-",  "-",  "-"])

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
        player_one = "X"
        player_two = "O"
        player_one_turn = True

        print "Player 1: " + player_one
        print "Player 2: " + player_two

        print_board(board)

        while not winner(board, magic_square):
            if player_one_turn:
                print "Player 1's turn"
                make_move(board, player_one)
                player_one_turn = False
            else:
                print "Player 2's turn"
                make_move(board, player_two)
                player_one_turn = True

            print_board(board)

    else:
        print "Playing against the computer"
        # Put code here for Ai game
        # Create class for Ai game

    # Prints the game board out

