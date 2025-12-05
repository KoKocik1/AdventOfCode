from pathlib import Path

from helpers import GetFile, time_and_print
from _2025._5.classes import Range
from tqdm import tqdm


def part1(range_array: list[Range], ingredients_array: list[int]) -> int:
    count = 0
    for ingredient in ingredients_array:
        for range in range_array:
            if range.is_in_range(ingredient):
                count += 1
                break
    return count


def part2(ranges : list[Range]) -> int:
    count = 0
    all_ranges: list[Range] = []
    for range in ranges:
        range.extend(all_ranges)
    
    all_ranges1: list[Range] = []
    for range in all_ranges:
        range.extend(all_ranges1)
    all_ranges = all_ranges1
    
    for range in all_ranges:
        count += range.get_size()
    
    return count

def read_range(file: GetFile) -> list[list[int]]:
    ranges = []
    for row in file.get_row():
        ranges.append(Range(int(row[0]), int(row[1])))
    return ranges

def read_ingredients(file: GetFile) -> list[int]:
    ingredients = []
    for row in file.get_row():
        ingredients.append(int(row[0]))
    return ingredients

def main():
    data_file = Path(__file__).parent / 'data/data_range.txt'
    range_file = GetFile(str(data_file), delimiter='-')
    range_array = read_range(range_file)

    data_file = Path(__file__).parent / 'data/data_ingredients.txt'
    ingredients_file = GetFile(str(data_file), delimiter='\n')
    ingredients_array = read_ingredients(ingredients_file)

    result1 = time_and_print("Part 1", part1, range_array, ingredients_array)
    result2 = time_and_print("Part 2", part2, range_array)


if __name__ == "__main__":
    main()



#  1, 10 -> 1,10
#  2, 5 -> 1,10

# 3,11 -> 1,10 | 10,11
# 14,16 -> 1,10 | 10,11 | 14,16
# 12, 13 -> 1,10 | 10,11 | 14,16 | 12,15

#  1, 10 -> 1,10
#  2, 5 -> 1,10

# 3,11 -> 1,11
# 14,16 -> 1,11 | 14,16
# 9, 15 -> 1,15 | 14,16 


#  1,3  7,9  12,14
# 1,14 - > 4, 11



# 4,6   5,8  -> 4,8
# 4,6   3,5 -> 3,6
# 4,6   3,8 -> 