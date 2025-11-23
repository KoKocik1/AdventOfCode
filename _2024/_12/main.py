from pathlib import Path

from helpers import GetFile
from helpers.array_helper import Board
from _2024._12.classes import FiledFinder


def calculate_fields(array: list[list[str]]) -> tuple[int, int]:
    finder = FiledFinder(Board(array))
    finder.find_fields()
    return finder.print_fields(), finder.print_fields_with_walls()


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='')
    array = file.get_2d_array()
    part1, part2 = calculate_fields(array)
    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
