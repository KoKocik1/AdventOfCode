from pathlib import Path

from helpers import GetFile
from helpers import Board
from _2025._4.classes import Forklift


def part1(board: Board) -> int:
    forklift = Forklift(board)
    return forklift.check_paper_rolls()[0]


def part2(board: Board) -> int:
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
