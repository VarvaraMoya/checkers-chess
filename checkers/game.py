from .board import CheckersBoard


class CheckersGame:
    """A class representing a complete checkers game with turn management.

    This class handles game flow, player turns, and user input processing.
    It uses a CheckersBoard instance to manage the game state.

    Attributes:
        board (CheckersBoard): The game board instance.
        players (list): List of player colors in order ['white', 'black'].
        turn_index (int): Current player index (0 for white, 1 for black).
    """

    def __init__(self):
        """Initializes a new checkers game with fresh board and white player first."""
        self.board = CheckersBoard()
        self.players = ['white', 'black']
        self.turn_index = 0

    def switch_turn(self):
        """Switches the current player turn between white and black."""
        self.turn_index = (self.turn_index + 1) % 2

    def play(self):
        """Main game loop that handles player moves and game flow.

        The loop:
        1. Displays current board state
        2. Prompts current player for move
        3. Processes move or undo command
        4. Validates and executes moves
        5. Switches turns after valid moves

        Supports 'undo' command to revert last move.
        """
        while True:
            self.board.display()
            current_player = self.players[self.turn_index]
            print(f"{current_player.capitalize()} ходит")
            start = input("Выберите шашку (например, E3): ")
            end = input("Введите целевую позицию (например, F4): ")

            if start.lower() == 'undo' or end.lower() == 'undo':
                self.board.undo_move()
                self.switch_turn()
                continue

            try:
                x1, y1 = self.convert_to_coords(start)
                x2, y2 = self.convert_to_coords(end)
                if self.board.move_piece((x1, y1), (x2, y2)):
                    self.switch_turn()
            except Exception:
                print("Неверный ввод! Попробуйте еще раз.")

    def convert_to_coords(self, position):
        """Converts algebraic notation (e.g., 'E3') to board coordinates.

        Args:
            position (str): Position in algebraic notation (letter + number).

        Returns:
            tuple: (row, column) coordinates for internal board representation.

        Raises:
            ValueError: If input format is invalid.
            IndexError: If coordinates are out of board bounds.
        """
        col = ord(position[0].lower()) - ord('a')
        row = 8 - int(position[1])
        return row, col
