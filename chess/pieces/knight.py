from .base import ChessPiece

class Knight(ChessPiece):
    """Class representing the Knight chess piece.

    The knight moves in an L-shape pattern (2 squares in one direction and then
    1 square perpendicular). It is the only piece that can jump over other pieces.

    Attributes:
        color (str): Piece color ('white' or 'black'), inherited from ChessPiece.
        symbol (str): 'N' for white knight, 'n' for black knight.
        has_moved (bool): Inherited from ChessPiece (less relevant for knights).
    """

    def get_symbol(self, color):
        """Returns the symbol representation of the knight.

        Args:
            color (str): Color of the piece ('white' or 'black').

        Returns:
            str: Uppercase 'N' for white knight, lowercase 'n' for black knight.

        Note:
            Uses 'N' instead of 'K' to avoid confusion with the King.
        """
        return 'N' if color == 'white' else 'n'

    def is_valid_move(self, board, start, end):
        """Validates knight movement according to standard chess rules.

        Args:
            board (list[list[ChessPiece]]): Current board state (unused for knights).
            start (tuple[int, int]): (row, column) of starting position.
            end (tuple[int, int]): (row, column) of target position.

        Returns:
            bool: True if the move follows the L-shaped pattern and destination is valid.

        Rules:
            1. Must move in L-shape: 2 squares one way + 1 square perpendicular
            2. Can jump over any intervening pieces
            3. Can capture opponent's piece at destination
            4. Cannot land on square occupied by own piece
        """
        x1, y1 = start
        x2, y2 = end
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        # Check L-shaped movement pattern
        if not ((dx == 2 and dy == 1) or (dx == 1 and dy == 2)):
            return False

        # Check destination (can capture opponent but not own piece)
        target = board[x2][y2]
        if target is not None and target.color == self.color:
            return False

        return True
