from checkers.game import CheckersGame
from Chess.game import ChessGame, ModifiedChessGame


def main():
    """Main entry point for the game suite application.

    Provides a menu to select between different game variants:
    - Checkers
    - Standard Chess
    - Modified Chess (with custom pieces)
    """
    print("Добро пожаловать в игровой комплект!")
    print("1. Шашки")
    print("2. Классические шахматы")
    print("3. Модифицированные шахматы (с новыми фигурами)")

    while True:
        choice = input("Выберите игру (1-3): ")
        if choice == '1':
            print("\nНачинаем игру в шашки!")
            game = CheckersGame()
            game.play()
            break
        elif choice == '2':
            print("\nНачинаем классические шахматы!")
            game = ChessGame()
            game.play()
            break
        elif choice == '3':
            print("\nНачинаем модифицированные шахматы!")
            game = ModifiedChessGame()
            game.play()
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    """Entry point when executed as a script."""
    main()
