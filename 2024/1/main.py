from pathlib import Path

from helpers import get_csv_data


def count_occurrences(value, value_list):
    """Count the number of occurrences of a value in a list."""
    return value_list.count(value)


def quicksort(num_list):
    """Sort a list using quicksort algorithm."""
    if len(num_list) <= 1:
        return num_list
    pivot = num_list[0]
    left = [x for x in num_list[1:] if x < pivot]
    right = [x for x in num_list[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)


def part1(sorted_list1, sorted_list2):
    """Part 1: Calculate sum of absolute differences between sorted lists."""
    return sum(abs(sorted_list1[i] - sorted_list2[i])
               for i in range(len(sorted_list1)))


def part2(sorted_list1, sorted_list2):
    """Part 2: Calculate sum of list1[i] * occurrences in list2."""
    return sum(sorted_list1[i] * count_occurrences(sorted_list1[i], sorted_list2)
               for i in range(len(sorted_list1)))


def main():
    """Main function that runs both parts of the task."""
    data_file = Path(__file__).parent / 'data.csv'
    column_names = ['list1', 'list2']

    # Load data
    df = get_csv_data(str(data_file), names=column_names, add_index=False)

    # Convert to lists and sort
    list1 = quicksort(df['list1'].tolist())
    list2 = quicksort(df['list2'].tolist())

    # Calculate and print results
    result1 = part1(list1, list2)
    result2 = part2(list1, list2)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
