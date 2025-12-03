from pathlib import Path

from helpers import GetFile
from classes import iterate_array


def part1(array: list[list[int]]) -> int:
    return iterate_array(array, 2)


def part2(array: list[list[int]]) -> int:
    return iterate_array(array, 12)

def read_data(file: GetFile) -> list[list[int]]:
    numbers = []
    for row in file.get_row():
        numbers.append([int(number) for number in row])
    return numbers

def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='')
    array = read_data(file)
    print(part1(array))
    print(part2(array))


if __name__ == "__main__":
    main()
