from pathlib import Path

from helpers import GetFile
from helpers.array_helper import Board
from _2024._15.classes import CleanBoard, TRASH

# Constants
SCORE_MULTIPLIER = 100


def calculate_score(board: Board, character: str) -> int:
    """Calculate the score based on trash positions.

    Score formula: sum of (100 * row + col) for each trash position.

    Args:
        board: The game board.

    Returns:
        The calculated score.
    """
    trash_positions = board.find_all_character_positions(character)
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


def load_moves(file_path: Path) -> str:
    """Load moves from file.

    Args:
        file_path: Path to the moves data file.

    Returns:
        String containing all move symbols concatenated.
    """
    file = GetFile(str(file_path), delimiter='')
    moves: list[str] = []
    for line in file.get_row():
        moves.extend(list(line))
    return ''.join(moves)


def part1(board: Board, moves: str) -> int:
    """Execute cleaning moves and calculate the final score.

    Args:
        board: The game board.
        moves: String of move symbols to execute.

    Returns:
        The calculated score based on final trash positions.
    """
    clean_board = CleanBoard(board, moves)
    clean_board.clean_board()
    return calculate_score(board, TRASH)


def part2(board: Board, moves: str) -> int:
    """Part 2 solution with transformed board.

    Args:
        board: The game board.
        moves: String of move symbols.

    Returns:
        Result for part 2.
    """
    clean_board_huge = CleanBoard(board, moves, should_transform_board=True)
    clean_board_huge.clean_board()
    return calculate_score(clean_board_huge.board, '[')


def main():
    """Main entry point."""
    data_dir = Path(__file__).parent / 'data'
    board_file = data_dir / 'data.txt'
    moves_file = data_dir / 'data_moves.txt'

    board = load_board(board_file)
    moves = load_moves(moves_file)

    print(part1(board, moves))
    
    board = load_board(board_file)
    print(part2(board, moves))


if __name__ == "__main__":
    main()
