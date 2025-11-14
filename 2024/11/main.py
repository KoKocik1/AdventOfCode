from pathlib import Path

from helpers import GetFile
from classes import Stones


def part1(rows: list[str], blinks: int) -> int:
    stones = Stones.create_from_string(rows)
    for _ in range(blinks):
        stones.blink()
        # print(stones)
    return stones.number_of_stones()


def part2(rows: list[list[int]]) -> int:
    return 0


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=' ')
    for row in file.get_row():
        print(part1(row, 25))


if __name__ == "__main__":
    main()
