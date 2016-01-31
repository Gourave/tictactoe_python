class Game(object):
    def __init__(self):
        pass

    # Check to see whether there is a winner or not
    @staticmethod
    def winner(board, magic_square):
        # Put code here to check diagonal and anti-diagonal lines
        return Game.check_horizontal(board, magic_square) or Game.check_vertical(board, magic_square) \
            or Game.check_diagonal(board, magic_square) or Game.check_anti_diagonal(board, magic_square)

    @staticmethod
    # Checks if pieces aligned horizontally are a win
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

    @staticmethod
    def check_vertical(board, magic_square):
        # Checks if pieces aligned vertically are a win
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

    @staticmethod
    def check_diagonal(board, magic_square):
        # Checks if pieces aligned diagonally are a win
        player_one_score = 0
        player_two_score = 0
        # Check the diagonal of the board and
        # increment the player scores accordingly
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

    @staticmethod
    def check_anti_diagonal(board, magic_square):
        # Checks if pieces aligned on the anti diagonal are a win
        player_one_score = 0
        player_two_score = 0
        # Check the anti-diagonal of the board and
        # increment player scores accordingly
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
