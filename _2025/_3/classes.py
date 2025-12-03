def bubble_sort(array: list[str]) -> list[str]:
    for i in range(len(array)):
        swapped = False
        for j in range(len(array) - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array

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
