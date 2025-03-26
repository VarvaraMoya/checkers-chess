import copy
from .pieces import (King, Queen, Rook, Bishop,
                     Knight, Pawn, Wizard, Dragon, Jester)


class ChessBoard:
    """A class representing a standard chess board with game state management.

    Manages piece positions, move validation, and special rules like castling and en passant.

    Attributes:
        board (list[list[ChessPiece|None]]): 8x8 grid representing the chess board.
        move_history (list): Stack of previous board states for undo functionality.
        white_king_pos (tuple): Current (row, col) position of white king.
        black_king_pos (tuple): Current (row, col) position of black king.
        en_passant_target (tuple|None): Square vulnerable to en passant capture.
    """

    def __init__(self):
        """Initializes a new chess board with standard starting position."""
        self.board = self.create_initial_board()
        self.move_history = []
        self.white_king_pos = (7, 4)
        self.black_king_pos = (0, 4)
        self.en_passant_target = None

    def create_initial_board(self):
        """Creates the standard chess starting position.

        Returns:
            list[list[ChessPiece|None]]: 8x8 grid with:
            - Pieces in standard positions
            - White at bottom (row 7-6)
            - Black at top (row 0-1)
        """
        board = [[None] * 8 for _ in range(8)]
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(8):
            board[0][i] = piece_order[i]('black')
            board[7][i] = piece_order[i]('white')
            board[1][i] = Pawn('black')
            board[6][i] = Pawn('white')

        return board

    def display(self):
        """Prints the current board state with coordinate labels.

        Output format:
          A B C D E F G H
          ----------------
        8 r n b q k b n r 8
        7 p p p p p p p p 7
        ...
        1 P P P P P P P P 1
          ----------------
          A B C D E F G H
        """
        print("  A B C D E F G H")
        print("  ----------------")
        for i in range(8):
            row = str(8 - i) + " "
            for j in range(8):
                row += (str(self.board[i][j]) if self.board[i][j] else '.') + ' '
            print(row + str(8 - i))
        print("  ----------------")
        print("  A B C D E F G H")

    def move_piece(self, start, end):
        """Attempts to move a piece following chess rules.

        Args:
            start (tuple[int, int]): (row, col) of starting position.
            end (tuple[int, int]): (row, col) of target position.

        Returns:
            bool: True if move was valid and executed.
        """
        x1, y1 = start
        x2, y2 = end
        piece = self.board[x1][y1]

        if not piece:
            print("Нет фигуры в начальной позиции!")  # No piece at start position
            return False

        if not piece.is_valid_move(self.board, start, end):
            print("Недопустимый ход для этой фигуры!")  # Invalid move for this piece
            return False

        if isinstance(piece, Jester) and self.board[x2][y2] is not None:
            if abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
                self.move_history.append(copy.deepcopy(self.board))
                self.board[x2][y2], self.board[x1][y1] = self.board[x1][y1], self.board[x2][y2]
                return True

        test_board = copy.deepcopy(self)
        test_board.board[x2][y2] = test_board.board[x1][y1]
        test_board.board[x1][y1] = None

        king_pos = self.white_king_pos if piece.color == 'white' else self.black_king_pos
        if test_board.is_square_under_attack(king_pos, 'black' if piece.color == 'white' else 'white'):
            print("Ход оставляет короля под шахом!")  # Move leaves king in check
            return False

        self.move_history.append(copy.deepcopy(self.board))
        self.board[x2][y2] = piece
        self.board[x1][y1] = None
        piece.has_moved = True

        if isinstance(piece, King):
            if piece.color == 'white':
                self.white_king_pos = (x2, y2)
            else:
                self.black_king_pos = (x2, y2)

        return True

    def is_square_under_attack(self, position, by_color):
        """Checks if a square is attacked by any piece of given color.

        Args:
            position (tuple[int, int]): (row, col) to check.
            by_color (str): 'white' or 'black' attacking color.

        Returns:
            bool: True if square is under attack.
        """
        x, y = position
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.color == by_color:
                    if piece.is_valid_move(self.board, (i, j), (x, y)):
                        return True
        return False

    def undo_move(self):
        """Reverts the board to previous state using move history."""
        if self.move_history:
            self.board = self.move_history.pop()


class ModifiedChessBoard(ChessBoard):
    """Variant chess board with custom pieces (Wizard, Dragon, Jester).

    Modifications:
    - Wizards replace queens
    - Dragons replace kings
    - Additional Jesters in pawn positions
    """

    def create_initial_board(self):
        """Creates initial position with custom piece arrangement.

        Returns:
            list[list[ChessPiece|None]]: 8x8 grid with:
            - Standard pieces except:
              - Wizards at d1/d8
              - Dragons at e1/e8
              - Jesters at c2/c7 and f2/f7
        """
        board = [[None] * 8 for _ in range(8)]
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(8):
            board[0][i] = piece_order[i]('black')
            board[7][i] = piece_order[i]('white')
            board[1][i] = Pawn('black')
            board[6][i] = Pawn('white')
          
        board[0][3] = Wizard('black')
        board[7][3] = Wizard('white')
        board[0][4] = Dragon('black')
        board[7][4] = Dragon('white')
        board[1][2] = Jester('black')
        board[6][2] = Jester('white')
        board[1][5] = Jester('black')
        board[6][5] = Jester('white')

        return board
