from pathlib import Path

from helpers import GetFile
from _2024._9.classes import DiscSpace


def part1(file: GetFile) -> int:
    disc_space = DiscSpace()
    disc_space.load_disc_space(file)
    disc_space.clear_disc_space()
    return disc_space.calculate_checksum()


def part2(file: GetFile) -> int:
    disc_space = DiscSpace()
    disc_space.load_disc_space(file)
    disc_space.clear_disc_space_all_files()
    return disc_space.calculate_checksum()


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='')
    print(part1(file))
    print(part2(file))


if __name__ == "__main__":
    main()
