from pathlib import Path

from helpers import GetFile, Board
from _2025._4.classes import Forklift


def part1(board: Board) -> int:
    """Count accessible paper rolls (with <= 4 surrounding rolls)."""
    forklift = Forklift(board)
    accessible_count = forklift.check_paper_rolls()
    return len(accessible_count)


def part2(board: Board) -> int:
    """Remove all accessible paper rolls iteratively and return total count."""
    forklift = Forklift(board)
    return forklift.clear_paper_rolls()


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='')
    array = file.get_2d_array()
    board = Board(array)
    print(part1(board))
    print(part2(board))


if __name__ == "__main__":
    main()
