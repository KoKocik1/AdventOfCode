from pathlib import Path

from helpers import GetFile


MAX_DIFFERENCE = 3


def parse_row_to_int_list(row):
    """Convert row (list of strings) to list of integers."""
    return [int(x) for x in row]


def is_ascending(num_list):
    """Check if the list is in ascending order."""
    return all(num_list[i] < num_list[i+1] for i in range(len(num_list)-1))


def is_descending(num_list):
    """Check if the list is in descending order."""
    return all(num_list[i] > num_list[i+1] for i in range(len(num_list)-1))


def is_sorted(num_list):
    """Check if the list is sorted (ascending or descending)."""
    return is_ascending(num_list) or is_descending(num_list)


def has_valid_differences(num_list):
    """Check if all adjacent differences are <= MAX_DIFFERENCE."""
    return all(abs(num_list[i] - num_list[i+1]) <= MAX_DIFFERENCE
               for i in range(len(num_list)-1))


def is_safe_level(num_list):
    """Check if a level is safe (sorted and has valid differences)."""
    return is_sorted(num_list) and has_valid_differences(num_list)


def is_safe_level_with_removal(num_list):
    """Check if a level is safe, allowing removal of one element."""
    # First check if the full list is safe
    if is_safe_level(num_list):
        return True

    # Try removing one element at a time
    for i in range(len(num_list)):
        modified_list = num_list[:i] + num_list[i + 1:]
        if is_safe_level(modified_list):
            return True

    return False


def part1(file):
    """Part 1: Count levels that are safe without any modifications."""
    safe_count = 0
    for row in file.get_row():
        num_list = parse_row_to_int_list(row)
        if is_safe_level(num_list):
            safe_count += 1
    return safe_count


def part2(file):
    """Part 2: Count levels that are safe after removing one element."""
    safe_count = 0
    for row in file.get_row():
        num_list = parse_row_to_int_list(row)
        if is_safe_level_with_removal(num_list):
            safe_count += 1
    return safe_count


def main():
    """Main function that runs both parts of the task."""
    data_file = Path(__file__).parent / 'data.txt'
    delimiter = ' '

    # Part 1: Count safe levels without modifications
    file1 = GetFile(str(data_file), delimiter)
    result1 = part1(file1)
    print(f"Part 1: {result1}")

    # Part 2: Count safe levels with one element removal allowed
    file2 = GetFile(str(data_file), delimiter)
    result2 = part2(file2)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
