from .base import ChessPiece


class Dragon(ChessPiece):
    """Custom chess piece class representing a Dragon (fairy chess piece).

    The Dragon combines movement patterns of rook and bishop, but only at triple distance.
    This is a non-standard chess piece typically used in variant chess games.

    Attributes:
        color (str): Piece color ('white' or 'black'), inherited from ChessPiece.
        symbol (str): 'D' for white dragon, 'd' for black dragon.
        has_moved (bool): Movement state flag, inherited from ChessPiece.
    """

    def get_symbol(self, color):
        """Returns the symbol representation of the dragon piece.

        Args:
            color (str): Color of the piece ('white' or 'black').

        Returns:
            str: Uppercase 'D' for white dragon, lowercase 'd' for black dragon.
        """
        return 'D' if color == 'white' else 'd'

    def is_valid_move(self, board, start, end):
        """Validates dragon movement according to its unique movement rules.

        The dragon can move:
        - Exactly 3 squares horizontally or vertically (like a triple-length rook)
        - Exactly 3 squares diagonally (like a triple-length bishop)

        Args:
            board (list[list[ChessPiece]]): Current board state as 2D array.
            start (tuple[int, int]): (row, column) of starting position.
            end (tuple[int, int]): (row, column) of target position.

        Returns:
            bool: True if the move is valid according to dragon movement rules.

        Rules:
            1. Must move exactly 3 squares in any orthogonal direction (rook-like)
            2. Must move exactly 3 squares in any diagonal direction (bishop-like)
            3. Cannot jump over pieces - path must be clear
            4. Can capture opponent's piece at destination
            5. Cannot land on own piece
        """
        x1, y1 = start
        x2, y2 = end
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        # Check basic movement pattern
        if not ((dx == 3 and dy == 0) or (dx == 0 and dy == 3) or (dx == 3 and dy == 3)):
            return False

        # Check path is clear
        step_x = 0 if dx == 0 else (1 if x2 > x1 else -1)
        step_y = 0 if dy == 0 else (1 if y2 > y1 else -1)

        x, y = x1 + step_x, y1 + step_y
        while x != x2 or y != y2:
            if board[x][y] is not None:
                return False
            x += step_x
            y += step_y

        # Check destination
        target = board[x2][y2]
        if target is not None and target.color == self.color:
            return False

        return True
