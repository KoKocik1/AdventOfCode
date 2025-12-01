from pathlib import Path

from helpers import GetFile
from _2025._1.classes import parse_rotation


def part1(array: list[int]) -> int:
    password = 0
    act_value = 50
    for rotation in array:
        act_value += rotation
        act_value %= 100
        if act_value == 0:
            password += 1
    return password

def check_zero(act_value: int, rotation: int, password: int) -> bool:
    left = rotation < 0
    for _ in range(abs(rotation)):
        act_value += -1 if left else 1
        if act_value == -1:
            act_value = 99
        elif act_value == 100:
            act_value = 0
        if act_value == 0:
            password += 1
    return act_value, password

def part2(array: list[int]) -> int:
    password = 0
    act_value = 50
    for rotation in array:
        act_value, password = check_zero(act_value, rotation, password)
    return password

def read_file(file: GetFile) -> list[int]:
    array = []
    for row in file.get_row():
        array.append(parse_rotation(row))
    return array

def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='\n')
    array = read_file(file)
    print(part1(array))
    print(part2(array))


if __name__ == "__main__":
    main()
