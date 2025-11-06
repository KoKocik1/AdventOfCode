from get_data import get_data
from quickSort import quickSort


def getOccurrences(value, list):
    # Returns the number of occurrences of a value in a list
    return list.count(value)


def part1(sorted_list1, sorted_list2):
    return sum([abs(sorted_list1[i] - sorted_list2[i])
                for i in range(len(sorted_list1))])


def part2(sorted_list1, sorted_list2):
    return sum([sorted_list1[i] * getOccurrences(sorted_list1[i], sorted_list2)
                for i in range(len(sorted_list1))])


def main():
    names = ['list1', 'list2']
    df = get_data(
        '/Users/krzysztofkokot/Projects/Algorithms/2024/1/data.csv',
        names=names)

    list1 = df['list1'].tolist()
    list2 = df['list2'].tolist()

    print(f"Part 1: {part1(list1, list2)}")
    print(f"Part 2: {part2(list1, list2)}")


if __name__ == "__main__":
    main()
