from .base import ChessPiece


class Rook(ChessPiece):
    """Class representing the Rook chess piece.

    The rook is a powerful piece that moves any number of squares vertically or horizontally.
    It plays a key role in castling and endgame strategies.

    Attributes:
        color (str): Piece color ('white' or 'black'), inherited from ChessPiece.
        symbol (str): 'R' for white rook, 'r' for black rook.
        has_moved (bool): Tracks if rook has moved (important for castling).
    """

    def get_symbol(self, color):
        """Returns the symbol representation of the rook.

        Args:
            color (str): Color of the piece ('white' or 'black').

        Returns:
            str: Uppercase 'R' for white rook, lowercase 'r' for black rook.
        """
        return 'R' if color == 'white' else 'r'

    def is_valid_move(self, board, start, end):
        """Validates rook movement according to standard chess rules.

        Args:
            board (list[list[ChessPiece]]): Current board state as 2D array.
            start (tuple[int, int]): (row, column) of starting position.
            end (tuple[int, int]): (row, column) of target position.

        Returns:
            bool: True if the move is valid according to rook movement rules.

        Rules:
            1. Must move in straight line (either horizontal or vertical)
            2. Cannot jump over other pieces
            3. Can capture opponent's piece at destination
            4. Cannot land on square occupied by own piece
            5. Movement range is unlimited (except board edges)
        """
        x1, y1 = start
        x2, y2 = end

        if x1 != x2 and y1 != y2:
            return False

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
