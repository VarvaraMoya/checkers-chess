from .base import ChessPiece

class King(ChessPiece):
    """Class representing the King chess piece.

    The king is the most important piece in chess. It moves one square in any direction.
    This implementation includes basic movement rules but does not handle castling or check validation.

    Attributes:
        color (str): Piece color ('white' or 'black'), inherited from ChessPiece.
        symbol (str): 'K' for white king, 'k' for black king.
        has_moved (bool): Tracks if king has moved (important for castling).
    """

    def get_symbol(self, color):
        """Returns the symbol representation of the king.

        Args:
            color (str): Color of the piece ('white' or 'black').

        Returns:
            str: Uppercase 'K' for white king, lowercase 'k' for black king.
        """
        return 'K' if color == 'white' else 'k'

    def is_valid_move(self, board, start, end):
        """Validates king movement according to standard chess rules.

        The king can move:
        - One square in any direction (orthogonal or diagonal)
        - Cannot move to squares under attack
        - Cannot move to squares occupied by own pieces
        - Special move: castling (not implemented in this basic version)

        Args:
            board (list[list[ChessPiece]]): Current board state as 2D array.
            start (tuple[int, int]): (row, column) of starting position.
            end (tuple[int, int]): (row, column) of target position.

        Returns:
            bool: True if the basic movement pattern is valid (does not check for checks).

        Rules:
            1. Maximum movement distance of one square in any direction
            2. Cannot land on square occupied by own piece
            3. Can capture opponent's piece at destination
            4. Does not validate if destination is under attack
        """
        x1, y1 = start
        x2, y2 = end
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        # Basic movement validation (1 square max)
        if not (dx <= 1 and dy <= 1):
            return False

        # Check destination (can capture opponent but not own piece)
        target = board[x2][y2]
        if target is not None and target.color == self.color:
            return False

        return True
