from .base import ChessPiece


class Wizard(ChessPiece):
    """Class representing a Wizard, a custom fairy chess piece.

    The Wizard combines the movement patterns of both knight and bishop:
    - Can move like a knight (L-shape)
    - Can move like a bishop (diagonally any distance)
    - Cannot jump over pieces when moving diagonally

    This is a non-standard piece used in some chess variants.

    Attributes:
        color (str): Piece color ('white' or 'black'), inherited from ChessPiece.
        symbol (str): 'W' for white wizard, 'w' for black wizard.
        has_moved (bool): Inherited from ChessPiece (not particularly relevant).
    """

    def get_symbol(self, color):
        """Returns the symbol representation of the wizard.

        Args:
            color (str): Color of the piece ('white' or 'black').

        Returns:
            str: Uppercase 'W' for white wizard, lowercase 'w' for black wizard.

        Note:
            Uses 'W' to distinguish from standard pieces while maintaining clarity.
        """
        return 'W' if color == 'white' else 'w'

    def is_valid_move(self, board, start, end):
        """Validates wizard movement according to its hybrid rules.

        Args:
            board (list[list[ChessPiece]]): Current board state as 2D array.
            start (tuple[int, int]): (row, column) of starting position.
            end (tuple[int, int]): (row, column) of target position.

        Returns:
            bool: True if the move is valid according to wizard movement rules.

        Rules:
            1. Knight movement: 2 squares in one direction + 1 square perpendicular
            2. Bishop movement: Any number of squares diagonally (path must be clear)
            3. Can capture opponent's piece at destination
            4. Cannot land on square occupied by own piece
        """
        x1, y1 = start
        x2, y2 = end
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
      
        knight_move = (dx == 2 and dy == 1) or (dx == 1 and dy == 2)
        if knight_move:
            target = board[x2][y2]
            return target is None or target.color != self.color

        bishop_move = (dx == dy)
        if bishop_move:
            step_x = 1 if x2 > x1 else -1
            step_y = 1 if y2 > y1 else -1
            x, y = x1 + step_x, y1 + step_y
            while x != x2 and y != y2:
                if board[x][y] is not None:
                    return False
                x += step_x
                y += step_y
            target = board[x2][y2]
            return target is None or target.color != self.color

        return False
