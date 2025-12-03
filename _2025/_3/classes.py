def find_largest_number(array: list[int], start_position: int = 0, max_position: int = 0) -> int:
    last_best = 0
    best_position = 0
    position = start_position
    
    if max_position > len(array):
        return 0
    
    for number in array[start_position:max_position]:
        position += 1
        if number > last_best:
            last_best = number
            best_position = position
            
    return last_best* 10**(len(array) - (max_position)) + find_largest_number(array, best_position, max_position+1)


def iterate_array(array: list[list[int]], number_of_digits: int) -> int:
    count = 0
    for a in array:
        max_position = len(a)-number_of_digits + 1
        best_value = find_largest_number(a, 0, max_position)
        count += best_value
    return count
