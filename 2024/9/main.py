from pathlib import Path

from helpers import GetFile
from classes import DiscSpace


def part1(file: GetFile) -> int:
    disc_space = DiscSpace()
    disc_space.load_disc_space(file)
    disc_space.clear_disc_space()
    return disc_space.calculate_checksum()


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='')
    print(part1(file))


if __name__ == "__main__":
    main()
