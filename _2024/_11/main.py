from pathlib import Path
from tqdm import tqdm

from helpers import GetFile
from classes import Stones, RecursiveStones


def part1(rows: list[str], blinks: int) -> int:
    stones = Stones(rows)
    for _ in range(blinks):
        stones.blink()
    return stones.number_of_stones()


def part2(rows: list[str], blinks: int) -> int:
    stones = RecursiveStones(rows)
    return stones.recursive_blink(blinks)


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=' ')

    for row in file.get_row():
        print(part1(row, 25))
        print(part2(row, 75))


if __name__ == "__main__":
    main()
