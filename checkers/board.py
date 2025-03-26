import copy
from .piece import CheckersPiece


class CheckersBoard:
    """A class representing a checkers game board with pieces and move history.

    Manages piece positioning, move validation, and game state tracking.

    Attributes:
        board (list[list[CheckersPiece|None]]: 8x8 grid representing the board state.
        move_history (list): Stack of previous board states for undo functionality.
    """

    def __init__(self):
        """Initializes a new checkers board with standard starting position."""
        self.board = self.create_initial_board()
        self.move_history = []

    def create_initial_board(self):
        """Creates the standard checkers starting position.

        Returns:
            list[list[CheckersPiece|None]]:
            - Black pieces in top 3 rows on dark squares
            - White pieces in bottom 3 rows on dark squares
            - Empty squares marked as None
        """
        board = [[None] * 8 for _ in range(8)]

        # Black pieces (top)
        for i in range(3):
            for j in range(8):
                if (i + j) % 2 == 1:
                    board[i][j] = CheckersPiece('black')

        # White pieces (bottom)
        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    board[i][j] = CheckersPiece('white')

        return board

    def display(self):
        """Prints the current board state with coordinate labels."""
        print("  A B C D E F G H")
        for i in range(8):
            row = str(8 - i) + " "
            for j in range(8):
                row += (str(self.board[i][j]) if self.board[i][j] else '.') + ' '
            print(row + str(8 - i))
        print("  A B C D E F G H")

    def move_piece(self, start, end):
        """Attempts to move a piece from start to end position.

        Args:
            start (tuple[int, int]): (row, col) of starting position.
            end (tuple[int, int]): (row, col) of target position.

        Returns:
            bool: True if move was valid and executed, False otherwise.
        """
        x1, y1 = start
        x2, y2 = end
        piece = self.board[x1][y1]
        if piece and self.is_valid_move(piece, start, end):
            self.move_history.append(copy.deepcopy(self.board))
            self.board[x2][y2] = piece
            self.board[x1][y1] = None

            # Check for promotion
            if (piece.color == 'white' and x2 == 0) or (piece.color == 'black' and x2 == 7):
                piece.promote()
            return True
        return False

    def is_valid_move(self, piece, start, end):
        """Validates a potential move according to checkers rules.

        Args:
            piece (CheckersPiece): The piece being moved.
            start (tuple[int, int]): Starting (row, col) position.
            end (tuple[int, int]): Target (row, col) position.

        Returns:
            bool: True if the move complies with game rules.
        """
        x1, y1 = start
        x2, y2 = end
        dx, dy = x2 - x1, y2 - y1

        if self.board[x2][y2] is not None:
            return False

        if piece.is_king:
            if abs(dx) == abs(dy):
                step_x = 1 if x2 > x1 else -1
                step_y = 1 if y2 > y1 else -1
                x, y = x1 + step_x, y1 + step_y
                captured = None
                while x != x2 and y != y2:
                    if self.board[x][y]:
                        if captured or self.board[x][y].color == piece.color:
                            return False
                        captured = (x, y)
                    x += step_x
                    y += step_y
                if captured and abs(dx) == 2:
                    self.board[captured[0]][captured[1]] = None
                    return True
                return abs(dx) == 1
        else:
            direction = -1 if piece.color == 'white' else 1
            if dx == direction and abs(dy) == 1:
                return True
            if dx == 2 * direction and abs(dy) == 2:
                mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
                if self.board[mid_x][mid_y] and self.board[mid_x][mid_y].color != piece.color:
                    self.board[mid_x][mid_y] = None
                    return True
        return False

    def undo_move(self):
        """Reverts the board to the previous state.

        Uses the move_history stack to undo the last move.
        Only works if at least one move has been made.
        """
        if self.move_history:
            self.board = self.move_history.pop()
