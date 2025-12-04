def find_largest_number(array: list[int], start_position: int = 0, max_position: int = 0) -> int:
    """Recursively find the largest number by selecting digits from array.
    
    Selects digits from the array within the given range, finds the maximum,
    and recursively processes the remaining positions.
    """
    if max_position > len(array):
        return 0
    
    best_digit = 0
    best_index = start_position
    
    # Find the maximum digit in the current range
    for i, digit in enumerate(array[start_position:max_position], start=start_position):
        if digit > best_digit:
            best_digit = digit
            best_index = i + 1
    
    # Calculate multiplier for current digit position
    remaining_digits = len(array) - max_position
    multiplier = 10 ** remaining_digits if remaining_digits > 0 else 1
    
    # Recursively process remaining positions
    next_value = find_largest_number(array, best_index, max_position + 1)
    
    return best_digit * multiplier + next_value


def iterate_array(array: list[list[int]], number_of_digits: int) -> int:
    """Sum the largest numbers found in each row using specified number of digits."""
    total = 0
    
    for row in array:
        max_position = len(row) - number_of_digits + 1
        best_value = find_largest_number(row, 0, max_position)
        total += best_value
    
    return total
