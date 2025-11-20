from pathlib import Path

from helpers import GetFile
from helpers.array_helper import Board
from classes import CleanBoard, TRASH

# Constants
SCORE_MULTIPLIER = 100


def calculate_score(board: Board) -> int:
    """Calculate the score based on trash positions.

    Score formula: sum of (100 * row + col) for each trash position.

    Args:
        board: The game board.

    Returns:
        The calculated score.
    """
    trash_positions = board.find_all_character_positions(TRASH)
    return sum(SCORE_MULTIPLIER * position.row + position.col
               for position in trash_positions)


def load_board(file_path: Path) -> Board:
    """Load board from file.

    Args:
        file_path: Path to the board data file.

    Returns:
        Board object initialized from file.
    """
    file = GetFile(str(file_path), delimiter='')
    return Board(file.get_2d_array())


def load_moves(file_path: Path) -> list[str]:
    """Load moves from file.

    Args:
        file_path: Path to the moves data file.

    Returns:
        List of move symbols as strings.
    """
    file = GetFile(str(file_path), delimiter='')
    moves: list[str] = []
    for line in file.get_row():
        moves.extend(list(line))
    return moves


def part1(board: Board, moves: list[str]) -> int:
    """Execute cleaning moves and calculate the final score.

    Args:
        board: The game board.
        moves: List of move symbols to execute.

    Returns:
        The calculated score based on final trash positions.
    """
    clean_board = CleanBoard(board, moves)
    clean_board.clean_board()
    print(board)
    return calculate_score(board)


def part2(board: Board, moves: list[str]) -> int:
    """Part 2 solution (placeholder).

    Args:
        board: The game board.
        moves: List of move symbols.

    Returns:
        Result for part 2.
    """
    return 0


def main():
    """Main entry point."""
    data_dir = Path(__file__).parent / 'data'
    board_file = data_dir / 'data.txt'
    moves_file = data_dir / 'data_moves.txt'

    board = load_board(board_file)
    moves = load_moves(moves_file)

    print(part1(board, moves))
    # print(part2(board, moves))


if __name__ == "__main__":
    main()
