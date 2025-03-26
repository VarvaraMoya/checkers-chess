from .base import ChessPiece


class Jester(ChessPiece):
    """Custom chess piece class representing a Jester (non-standard chess piece).

    The Jester moves similarly to a king but without castling or check restrictions.
    This whimsical piece is typically used in fairy chess variants and custom games.

    Attributes:
        color (str): Piece color ('white' or 'black'), inherited from ChessPiece.
        symbol (str): 'J' for white jester, 'j' for black jester.
        has_moved (bool): Tracks if piece has moved (unused for jester).
    """

    def get_symbol(self, color):
        """Returns the symbol representation of the jester piece.

        Args:
            color (str): Color of the piece ('white' or 'black').

        Returns:
            str: Uppercase 'J' for white jester, lowercase 'j' for black jester.
        """
        return 'J' if color == 'white' else 'j'

    def is_valid_move(self, board, start, end):
        """Validates jester movement according to its unique movement rules.

        The jester can move:
        - One square in any direction (orthogonal or diagonal)
        - Cannot move more than one square at a time
        - Follows standard capture rules (can take opponent's pieces)

        Args:
            board (list[list[ChessPiece]]): Current board state as 2D array.
            start (tuple[int, int]): (row, column) of starting position.
            end (tuple[int, int]): (row, column) of target position.

        Returns:
            bool: True if the move is valid according to jester movement rules.

        Rules:
            1. Maximum one square movement in any direction
            2. Can capture opponent's piece at destination
            3. Cannot land on own piece
            4. No special moves (castling/en passant)
        """
        x1, y1 = start
        x2, y2 = end
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if not (dx <= 1 and dy <= 1):
            return False

        target = board[x2][y2]
        if target is not None and target.color == self.color:
            return False

        return True
