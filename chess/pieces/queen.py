from .base import ChessPiece


class Queen(ChessPiece):
    """Class representing the Queen chess piece.

    The queen combines the movement capabilities of both rook and bishop.
    It is the most powerful piece, able to move any number of squares:
    - Vertically
    - Horizontally
    - Diagonally

    Attributes:
        color (str): Piece color ('white' or 'black'), inherited from ChessPiece.
        symbol (str): 'Q' for white queen, 'q' for black queen.
        has_moved (bool): Inherited from ChessPiece (not particularly relevant for queens).
    """

    def get_symbol(self, color):
        """Returns the symbol representation of the queen.

        Args:
            color (str): Color of the piece ('white' or 'black').

        Returns:
            str: Uppercase 'Q' for white queen, lowercase 'q' for black queen.
        """
        return 'Q' if color == 'white' else 'q'

    def is_valid_move(self, board, start, end):
        """Validates queen movement according to standard chess rules.

        Args:
            board (list[list[ChessPiece]]): Current board state as 2D array.
            start (tuple[int, int]): (row, column) of starting position.
            end (tuple[int, int]): (row, column) of target position.

        Returns:
            bool: True if the move is valid according to queen movement rules.

        Rules:
            1. Can move any number of squares vertically, horizontally or diagonally
            2. Cannot jump over other pieces
            3. Can capture opponent's piece at destination
            4. Cannot land on square occupied by own piece
        """
        x1, y1 = start
        x2, y2 = end
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if not ((x1 == x2 or y1 == y2) or (dx == dy)):
            return False

        # Determine direction steps
        step_x = 0 if x1 == x2 else (1 if x2 > x1 else -1)
        step_y = 0 if y1 == y2 else (1 if y2 > y1 else -1)

        x, y = x1 + step_x, y1 + step_y
        while x != x2 or y != y2:
            if board[x][y] is not None:
                return False
            x += step_x
            y += step_y

        target = board[x2][y2]
        if target is not None and target.color == self.color:
            return False

        return True
