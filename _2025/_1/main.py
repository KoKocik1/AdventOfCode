from pathlib import Path

from helpers import GetFile
from _2025._1.classes import parse_rotation, check_zero, check_zero_end


def part1(array: list[int]) -> int:
    password = 0
    act_value = 50
    for rotation in array:
        act_value, password = check_zero_end(act_value, rotation, password)
    return password


def part2(array: list[int]) -> int:
    password = 0
    act_value = 50
    for rotation in array:
        act_value, password = check_zero(act_value, rotation, password)
    return password

def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='\n')
    array = file.get_string_list()
    array = [parse_rotation(rotation) for rotation in array]
    print(part1(array))
    print(part2(array))


if __name__ == "__main__":
    main()
