from get_file import GetFile


def get_list_from_row(row):
    return [int(x) for x in row]


def check_if_ascending(num_list):
    return all(num_list[i] < num_list[i+1] for i in range(len(num_list)-1))


def check_if_descending(num_list):
    return all(num_list[i] > num_list[i+1] for i in range(len(num_list)-1))


def check_difference(num_list):
    max_difference = 3
    return all(abs(num_list[i] - num_list[i+1]) <= max_difference for i in range(len(num_list)-1))


def check_if_save_level(num_list):
    is_sorted = check_if_ascending(num_list) or check_if_descending(
        num_list)
    return is_sorted and check_difference(num_list)


def check_if_save_level_again(num_list):
    if check_if_save_level(num_list):
        return True

    for i in range(len(num_list)):
        updated_num_list = num_list[:i] + num_list[i + 1:]
        is_sorted = check_if_ascending(updated_num_list) or check_if_descending(
            updated_num_list)
        if is_sorted and check_difference(updated_num_list):
            return True
    return False


def part1(file):
    save_levels = 0
    for row in file.get_row():
        num_list = get_list_from_row(row)
        if check_if_save_level(num_list):
            save_levels += 1
    return save_levels


def part2(file):
    save_levels = 0
    for row in file.get_row():
        num_list = get_list_from_row(row)
        if check_if_save_level_again(num_list):
            save_levels += 1
    return save_levels


def main():
    file = GetFile(
        '/Users/krzysztofkokot/Projects/Algorithms/2024/2/data_part1.txt', ' ')
    print(part1(file))
    print(part2(file))


if __name__ == "__main__":
    main()
