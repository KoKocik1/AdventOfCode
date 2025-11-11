from pathlib import Path
from helpers import GetFile
from helpers.array_helper import Board
from classes import AntennaAnalyzer


def part1(board: Board) -> int:
    analyzer = AntennaAnalyzer(board)
    return analyzer.count_sinlge_antinodes()


def part2(board: Board) -> int:
    analyzer = AntennaAnalyzer(board)
    return analyzer.count_recursive_antinodes()


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='')
    board = Board(file.get_2d_array())
    print(part1(board))
    print(part2(board))


if __name__ == "__main__":
    main()
