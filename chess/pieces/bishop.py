from .base import ChessPiece


class Bishop(ChessPiece):
    """Concrete class representing a Bishop chess piece.

    Inherits from ChessPiece and implements bishop-specific movement logic.
    Bishops move diagonally any number of squares but cannot jump over pieces.

    Attributes:
        color (str): Inherited from ChessPiece ('white' or 'black').
        symbol (str): 'B' for white bishop, 'b' for black bishop.
        has_moved (bool): Inherited from ChessPiece, tracks if piece has moved.
    """

    def get_symbol(self, color):
        """Returns the Unicode symbol for the bishop.

        Args:
            color (str): Color of the piece ('white' or 'black').

        Returns:
            str: 'B' for white bishop, 'b' for black bishop.
        """
        return 'B' if color == 'white' else 'b'

    def is_valid_move(self, board, start, end):
        """Validates bishop movement according to chess rules.

        Args:
            board (list[list[ChessPiece]]): 2D array representing the chess board.
            start (tuple[int, int]): (row, col) coordinates of starting position.
            end (tuple[int, int]): (row, col) coordinates of target position.

        Returns:
            bool: True if the move is valid, False otherwise.

        Rules:
            - Must move diagonally (equal change in rows and columns)
            - Cannot jump over intervening pieces
            - Can capture opponent's piece at destination
            - Cannot move to square occupied by own piece
        """
        x1, y1 = start
        x2, y2 = end
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        # Bishop must move diagonally
        if dx != dy:
            return False

        step_x = 1 if x2 > x1 else -1
        step_y = 1 if y2 > y1 else -1

        # Check for blocking pieces along the diagonal
        x, y = x1 + step_x, y1 + step_y
        while x != x2 and y != y2:
            if board[x][y] is not None:
                return False
            x += step_x
            y += step_y

        # Check destination (can capture opponent but not own piece)
        target = board[x2][y2]
        if target is not None and target.color == self.color:
            return False

        return True
