from .base import ChessPiece


class Pawn(ChessPiece):
    """Class representing the Pawn chess piece.

    The pawn is the most numerous chess piece with unique movement rules:
    - Moves forward but captures diagonally
    - Special two-square initial move
    - En passant capture (not implemented here)
    - Promotion upon reaching the opposite rank

    Attributes:
        color (str): Piece color ('white' or 'black'), inherited from ChessPiece.
        symbol (str): 'P' for white pawn, 'p' for black pawn.
        has_moved (bool): Tracks if pawn has moved (affects two-square move).
    """

    def get_symbol(self, color):
        """Returns the symbol representation of the pawn.

        Args:
            color (str): Color of the piece ('white' or 'black').

        Returns:
            str: Uppercase 'P' for white pawn, lowercase 'p' for black pawn.
        """
        return 'P' if color == 'white' else 'p'

    def is_valid_move(self, board, start, end):
        """Validates pawn movement according to standard chess rules.

        Args:
            board (list[list[ChessPiece]]): Current board state as 2D array.
            start (tuple[int, int]): (row, column) of starting position.
            end (tuple[int, int]): (row, column) of target position.

        Returns:
            bool: True if the move is valid according to pawn movement rules.

        Rules:
            1. White pawns move up (decreasing row), black pawns move down
            2. Normal move: 1 square forward to empty square
            3. Initial move: Optionally 2 squares forward if path is clear
            4. Capture: 1 square diagonally forward to opponent's piece
            5. Does not implement en passant or promotion logic
        """
        x1, y1 = start
        x2, y2 = end
        dx = x2 - x1
        dy = abs(y2 - y1)
        direction = -1 if self.color == 'white' else 1  # White moves up, black moves down

        if dy == 0:
            if dx == direction and board[x2][y2] is None:
                return True
            start_row = 6 if self.color == 'white' else 1
            if (x1 == start_row and dx == 2 * direction and
                    board[x2][y2] is None and board[x1 + direction][y1] is None):
                return True
            return False

        if dy == 1 and dx == direction:
            if board[x2][y2] is not None and board[x2][y2].color != self.color:
                return True
            return False

        return False
