from pathlib import Path

from helpers import GetFile
from _2025._3.classes import iterate_array


def part1(array: list[list[int]]) -> int:
    """Find largest numbers using 2 digits from each row."""
    return iterate_array(array, 2)


def part2(array: list[list[int]]) -> int:
    """Find largest numbers using 12 digits from each row."""
    return iterate_array(array, 12)


def read_data(file: GetFile) -> list[list[int]]:
    """Read and parse file data into a 2D array of integers."""
    return [[int(digit) for digit in row] for row in file.get_row()]


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='')
    array = read_data(file)
    print(part1(array))
    print(part2(array))


if __name__ == "__main__":
    main()
