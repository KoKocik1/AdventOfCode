from pathlib import Path

from helpers import GetFile, time_and_print
from _2025._5.classes import Range, RangeHelper


def part1(ranges: list[Range], ingredients_array: list[int]) -> int:
    """Count ingredients that fall within any of the given ranges."""
    merged_ranges = RangeHelper.optimize_ranges(ranges)
    return RangeHelper.count_ingredients(merged_ranges, ingredients_array)


def part2(ranges: list[Range]) -> int:
    """Merge overlapping ranges and calculate total size of merged ranges."""
    merged_ranges = RangeHelper.optimize_ranges(ranges)
    return sum(range_obj.get_size() for range_obj in merged_ranges)


def read_range(file: GetFile) -> list[Range]:
    """Read range data from file and return list of Range objects."""
    return [Range(int(row[0]), int(row[1])) for row in file.get_row()]


def read_ingredients(file: GetFile) -> list[int]:
    """Read ingredients from file and return list of integers."""
    return [int(row[0]) for row in file.get_row()]


def main():
    # Read range data
    range_file_path = Path(__file__).parent / 'data/data_range.txt'
    range_file = GetFile(str(range_file_path), delimiter='-')
    range_array = read_range(range_file)

    # Read ingredients data
    ingredients_file_path = Path(__file__).parent / 'data/data_ingredients.txt'
    ingredients_file = GetFile(str(ingredients_file_path), delimiter='\n')
    ingredients_array = read_ingredients(ingredients_file)

    # Run parts with timing
    result1 = time_and_print("Part 1", part1, range_array, ingredients_array)
    result2 = time_and_print("Part 2", part2, range_array)


if __name__ == "__main__":
    main()