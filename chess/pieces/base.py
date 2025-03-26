class ChessPiece:
    """Abstract base class representing a chess piece.

    Provides the common interface and core functionality for all chess pieces.
    Concrete piece classes should inherit from this class and implement the abstract methods.

    Attributes:
        color (str): The color of the piece ('white' or 'black').
        symbol (str): The character symbol representing the piece.
        has_moved (bool): Flag indicating if the piece has moved from its initial position.
                         Relevant for special moves like castling and pawn promotion.
    """

    def __init__(self, color):
        """Initializes a new chess piece with basic properties.

        Args:
            color (str): The color of the piece, either 'white' or 'black'.

        Raises:
            ValueError: If an invalid color is provided.
        """
        self.color = color
        self.symbol = self.get_symbol(color)
        self.has_moved = False

    def get_symbol(self, color):
        """Gets the symbol representation of the piece.

        Args:
            color (str): The color of the piece ('white' or 'black').

        Returns:
            str: The character symbol representing the piece.

        Raises:
            NotImplementedError: Must be implemented by concrete subclasses.
        """
        raise NotImplementedError("Subclasses must implement get_symbol()")

    def is_valid_move(self, board, start, end):
        """Validates whether a move is legal for this piece.

        Args:
            board (list[list[ChessPiece]]): The current board state as a 2D array.
            start (tuple[int, int]): The (row, column) of the starting position.
            end (tuple[int, int]): The (row, column) of the target position.

        Returns:
            bool: True if the move is valid according to the piece's movement rules.

        Raises:
            NotImplementedError: Must be implemented by concrete subclasses.
        """
        raise NotImplementedError("Subclasses must implement is_valid_move()")

    def __str__(self):
        """Returns the string representation of the piece.

        Returns:
            str: The symbol of the piece, used for board display.
        """
        return self.symbol
