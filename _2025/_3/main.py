from pathlib import Path

from helpers import GetFile
from classes import find_largest_number


def part1(array: list[str]) -> int:
    count = 0
    for a in array:
        max_position = len(a)-1
        best_value = find_largest_number(a, 0, max_position)
        print(best_value)
        count += best_value
    return count


def part2(array: list[str]) -> int:
    count = 0
    for a in array:
        max_position = len(a)-11
        best_value = find_largest_number(a, 0, max_position)
        print(best_value)
        count += best_value
    return count

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
