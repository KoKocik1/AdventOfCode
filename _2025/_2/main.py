from pathlib import Path

from helpers import GetFile
from _2025._2.classes import Range


def part1(array: list[Range]) -> int:
    """Sum all overlapping numbers across all ranges."""
    return sum(
        sum(range_obj.has_overlaps())
        for range_obj in array
        if range_obj.start <= range_obj.end
    )


def part2(array: list[Range]) -> int:
    """Sum all repeating numbers across all ranges."""
    return sum(
        sum(range_obj.has_repeats())
        for range_obj in array
        if range_obj.start <= range_obj.end
    )

def get_ranges(row: list[str]) -> list[Range]:
    """Parse range strings (e.g., '11-22') into Range objects."""
    ranges = []
    for range_str in row:
        parts = range_str.split('-')
        if len(parts) == 2:
            ranges.append(Range(int(parts[0]), int(parts[1])))
    return ranges


def read_data(file: GetFile) -> list[Range]:
    """Read all ranges from file."""
    ranges = []
    for row in file.get_row():
        ranges.extend(get_ranges(row))
    return ranges

def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=',')
    array = read_data(file)
    print(part1(array))
    print(part2(array))


if __name__ == "__main__":
    main()
