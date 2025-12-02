from pathlib import Path

from helpers import GetFile
from _2025._2.classes import Range


def part1(array: list[Range]) -> int:
    count = 0
    for range in array:
        if range.start <= range.end:
            overlaps = range.has_overlaps()
            count += sum(overlaps)
    return count


def part2(array: list[Range]) -> int:
    return 0

def read_data(file: GetFile) -> list[Range]:
    ranges = []
    for row in file.get_row():
        for range in row:
            range = range.split('-')
            if len(range) != 2:
                continue
            ranges.append(Range(int(range[0]), int(range[1])))
    return ranges

def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=',')
    array = read_data(file)
    print(part1(array))
    print(part2(array))


if __name__ == "__main__":
    main()
