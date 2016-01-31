from random import randint


class Ai(object):
    def __init__(self):
        pass

    # TODO: Make the AI smarter
    @staticmethod
    def make_move(board, computer, human, board_checked):
        row = -1
        col = -1
        if not board_checked:
            # TODO: Add defensive moves
            for row_taken in range(0, len(board)):
                if human in board[row_taken] and computer not in board[row_taken]:
                    if row_taken == 2:
                        row = 0
                    else:
                        row = row_taken + 1
                    break
                elif computer in board[row_taken]:
                    if row_taken == 2:
                        row = -1
                        break
                else:
                    row = row_taken
                    break
            # Take the transpose of the board to check the columns
            transpose = zip(*board)
            for col_taken in range(0, len(transpose)):
                # Check for human piece and try to block it
                if human in transpose[col_taken] and computer not in transpose[col_taken]:
                    block = Ai.check_num_human_in_row(board, human, computer)
                    if board[row][col_taken] != human and block:
                        col = col_taken
                    # TODO: Fix out of bounds error with col_taken + 1
                    elif board[row][col_taken + 1] != human:
                        if row == 0:
                            row = 2
                        else:
                            row -= 1
                        if col_taken == 2:
                            col = 0
                        else:
                            col = col_taken + 1
                    else:
                        if col_taken == 0:
                            col = 2
                        else:
                            col = col_taken - 1
                    break
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
            Ai.make_move(board, computer, human, True)
        else:
            board[row][col] = computer

    @staticmethod
    def check_num_human_in_row(board, human, computer):
        # Check for the number of humans in a certain row
        for row in range(0, len(board)):
            num_human = 0
            for col in range(0, len(board)):
                if human == board[row][col]:
                    num_human += 1
                    if num_human >= 2:
                        return True
                elif computer == board[row][col]:
                    num_human = 0
        return False
