import sys
from random import randint


# Prints out the game board in a way the user can see it nicely
def print_board(board):
    for row in board:
        print "\t\t" + " ".join(row)


# Check to see whether there is a winner or not
def winner(board, magic_square):
    # Put code here to check diagonal and anti-diagonal lines
    return check_horizontal(board, magic_square) or check_vertical(board, magic_square) \
        or check_diagonal(board, magic_square) or check_anti_diagonal(board, magic_square)


def check_horizontal(board, magic_square):
    player_one_score = 0
    player_two_score = 0
    # Count the value of the sum of the magic square of each row.
    # If a row adds up to 15, then the player who's score is 15 won
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            if board[row][col] == "X":
                player_one_score += magic_square[row][col]
            elif board[row][col] == "O":
                player_two_score += magic_square[row][col]
        if player_one_score == 15:
            print "Player 1 wins!"
            return True
        elif player_two_score == 15:
            print "Player 2 wins!"
            return True
        # Reset the counter to 0 if no score was 15 to prep for the next row
        player_one_score = 0
        player_two_score = 0

    return False


def check_vertical(board, magic_square):
    player_one_score = 0
    player_two_score = 0
    # Count the value of the sum of the magic square of each row.
    # If a column adds up to 15, then the player who's score is 15 won
    for col in range(0, len(board)):
        for row in range(0, len(board)):
            if board[row][col] == "X":
                player_one_score += magic_square[row][col]
            elif board[row][col] == "O":
                player_two_score += magic_square[row][col]
        if player_one_score == 15:
            print "Player 1 wins!"
            return True
        elif player_two_score == 15:
            print "Player 2 wins!"
            return True
        # Reset the counter to 0 if no score was 15 to prep for the next column
        player_one_score = 0
        player_two_score = 0

    return False


def check_diagonal(board, magic_square):
    player_one_score = 0
    player_two_score = 0
    for i in range(0, len(board)):
        if board[i][i] == "X":
            player_one_score += magic_square[i][i]
        elif board[i][i] == "O":
            player_two_score += magic_square[i][i]
    if player_one_score == 15:
        print "Player 1 wins!"
        return True
    elif player_two_score == 15:
        print "Player 2 wins!"
        return True
    return False


def check_anti_diagonal(board, magic_square):
    player_one_score = 0
    player_two_score = 0
    for i in range(len(board), 0):
        if board[i][i] == "X":
            player_one_score += magic_square[i][i]
        elif board[i][i] == "O":
            player_two_score += magic_square[i][i]
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
        try:
            row = int(raw_input("Row: "))
        except ValueError:
            row = -1
            print "Please enter an integer"
    while not (-1 < col < 3):
        try:
            col = int(raw_input("Col: "))
        except ValueError:
            col = -1
            print "Please enter an integer"
    if board[row][col] != "-":
        print "This place has already been taken up. Please choose another spot."
        print_board(board)
        make_move(board, player)
    else:
        board[row][col] = player


# TODO: Make the AI smarter
def ai_make_move(board, computer, human, board_checked):
    row = -1
    col = -1
    if not board_checked:
        # TODO: Add check for human piece for defensive moves
        for row_taken in range(0, len(board)):
            if computer in board[row_taken]:
                if row_taken == 2:
                    row = -1
                    break
            else:
                row = row_taken
                break
        # Take the transpose of the board to check the columns
        transpose = zip(*board)
        for col_taken in range(0, len(transpose)):
            if computer in transpose[col_taken]:
                if col_taken == 2:
                    col = -1
                    break
            else:
                col = col_taken
                break
    while not (-1 < row < 3):
        row = randint(0, 2)
    while not (-1 < col < 3):
        col = randint(0, 2)
    if board[row][col] != "-":
        ai_make_move(board, computer, human, True)
    else:
        board[row][col] = computer


def main():
    # Setup the game board
    board = []
    for i in range(0, 3):
        board.append(["-",  "-",  "-"])

    # Magic square to hold the values of each tile
    # Used to determine a winner
    magic_square = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

    # Used to count the number of moves taken to check for a draw
    num_moves = 0

    # Prompt the user to see whether he/she would like to play the computer or not
    print "\nWelcome to TicTacToe"
    print_board(board)

    game_choice = raw_input("\nWould you like to play with another 'player', or the 'computer?' ").lower()

    # If the input was of incorrect format, ask the user again until he/she gets it right
    while game_choice != "player" and game_choice != "computer":
        print "Please enter either 'player' or 'computer'"
        game_choice = raw_input("Would you like to play with another player, or the computer? ")

    player_one = "X"
    player_two = "O"
    player_one_turn = True

    if game_choice == "player":
        print "Playing PvP"

        print "Player 1: " + player_one
        print "Player 2: " + player_two

    else:
        print "Playing against the computer"

        print "Player 1 (Human): " + player_one
        print "Player 2 (Computer): " + player_two

    print_board(board)

    # If there is no winner, then check for a draw, if no draw, then make a move.
    while not winner(board, magic_square):
        if num_moves != 9:
            if player_one_turn:
                print "Player 1's turn"
                make_move(board, player_one)
                player_one_turn = False
            else:
                print "Player 2's turn"
                if game_choice == "player":
                    make_move(board, player_two)
                else:
                    ai_make_move(board, player_two, player_one, False)
                player_one_turn = True

            print_board(board)
        else:
            print "It's a Draw!"
            sys.exit()
        num_moves += 1

if __name__ == "__main__":
    main()
