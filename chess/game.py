from .board import ChessBoard, ModifiedChessBoard


class ChessGame:
    """A class representing a complete chess game with turn management.

    Handles the game flow, player turns, and move input for standard chess rules.

    Attributes:
        board (ChessBoard): The game board instance.
        turn (str): Current player's color ('white' or 'black').
        move_count (int): Total number of moves played in the game.
    """

    def __init__(self):
        """Initializes a new chess game with standard setup and white to move first."""
        self.board = ChessBoard()
        self.turn = 'white'
        self.move_count = 0

    def switch_turn(self):
        """Alternates the current player's turn between white and black."""
        self.turn = 'black' if self.turn == 'white' else 'white'

    def play(self):
        """Main game loop that handles player input and move execution.

        Features:
        - Displays current board state
        - Accepts algebraic notation input (e.g., E2-E4)
        - Supports 'undo' command
        - Validates moves according to chess rules
        - Tracks move count and player turns

        The loop continues until manual interruption.
        """
        while True:
            self.board.display()
            print(f"Ход {self.move_count + 1}, {self.turn} ходит")  
            start = input("Выберите фигуру (например, E2): ")  
            end = input("Введите целевую позицию (например, E4): ")  

            if start.lower() == 'undo' or end.lower() == 'undo':
                self.board.undo_move()
                self.switch_turn()
                continue

            try:
                # Convert algebraic notation to board coordinates
                x1, y1 = 8 - int(start[1]), ord(start[0].lower()) - ord('a')
                x2, y2 = 8 - int(end[1]), ord(end[0].lower()) - ord('a')

                if self.board.move_piece((x1, y1), (x2, y2)):
                    self.switch_turn()
                    self.move_count += 1
            except Exception as e:
                print(f"Неверный ввод! Ошибка: {e}")  # Invalid input! Error: [error]


class ModifiedChessGame(ChessGame):
    """A variant chess game featuring custom pieces (Wizard, Dragon, Jester).

    Inherits core gameplay from ChessGame but uses ModifiedChessBoard with special pieces.

    New Pieces:
    - Wizard (W/w): Combines knight and bishop movements
    - Dragon (D/d): Moves exactly 3 squares in any direction (jumping)
    - Jester (J/j): Moves like king and can swap with adjacent pieces
    """

    def __init__(self):
        """Initializes a modified chess game with custom piece setup."""
        self.board = ModifiedChessBoard()
        self.turn = 'white'
        self.move_count = 0

    def play(self):
        """Starts the modified chess game with custom piece explanations.

        Before starting the main game loop:
        - Displays special piece information
        - Shows movement rules for new pieces
        - Then proceeds with standard gameplay
        """
        print("\n=== МОДИФИЦИРОВАННЫЕ ШАХМАТЫ ===")
        print("Новые фигуры:")  # New pieces:
        print("W - Волшебник (ходы как конь+слон)")
        print("D - Дракон (ход на 3 клетки, прыгает)")
        print("J - Шут (ход как король + обмен местами)\n")
        super().play()
