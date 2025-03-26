class CheckersPiece:
    """A class representing a checkers piece (pawn or king).

    This class encapsulates the state and behavior of a single checkers piece,
    including its color, rank (pawn/king), and string representation.

    Attributes:
        color (str): The color of the piece ('black' or 'white').
        is_king (bool): Whether the piece is a king (False for regular pawn).
    """

    def __init__(self, color, is_king=False):
        """Initializes a new checkers piece.

        Args:
            color (str): The color of the piece ('black' or 'white').
            is_king (bool, optional): Whether the piece starts as a king.
                                     Defaults to False (regular pawn).

        Raises:
            ValueError: If color is not 'black' or 'white'.
        """
        self.color = color
        self.is_king = is_king

    def promote(self):
        """Promotes the piece from pawn to king.

        This method changes the piece's status to king, which affects its
        movement capabilities on the board.
        """
        self.is_king = True

    def __str__(self):
        """Provides string representation of the piece for board display.

        Returns:
            str:
                - 'b' for black pawn
                - 'B' for black king
                - 'w' for white pawn
                - 'W' for white king
        """
        if self.is_king:
            return 'B' if self.color == 'black' else 'W'
        return 'b' if self.color == 'black' else 'w'
