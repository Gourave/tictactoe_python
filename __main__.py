import sys
from Ai import Ai
from Game import Game


def print_board(board):
    # Prints out the game board in a way the user can see it nicely
    for row in board:
        print "\t\t" + " ".join(row)


def make_move(board, player):
    # Prompt the user to make a move and take up the spot that was specified by
    # the players piece
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
    while not Game.winner(board, magic_square):
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
                    Ai.make_move(board, player_two, player_one, False)
                player_one_turn = True

            print_board(board)
        else:
            print "It's a Draw!"
            sys.exit()
        num_moves += 1

if __name__ == "__main__":
    main()
