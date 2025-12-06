from pathlib import Path

from helpers import GetFile, time_and_print
from helpers.array_helper import Board, Position
from _2025._6.classes import ColumnScore


def part1(column_scores: list[ColumnScore]) -> int:
    """Calculate total score from all column scores."""
    return sum(column_score.calculate_score() for column_score in column_scores)


def part2(column_scores: list[ColumnScore]) -> int:
    """Calculate total score from all column scores."""
    return sum(column_score.calculate_score() for column_score in column_scores)

def get_part1_data(file: GetFile) -> list[ColumnScore]:
    """Extract column scores from file data for part 1.
    
    Reads data where the last row contains math operators and previous rows contain numbers.
    """
    array = [[col for col in row if col != ''] for row in file.get_row()]
    board = Board(array)
    column_scores = []
    
    last_row_index = board.get_column_length() - 1
    
    for col in range(board.get_row_length()):
        math_character = board.get_character(Position(last_row_index, col))
        column_numbers = [
            int(board.get_character(Position(row, col)))
            for row in range(last_row_index - 1, -1, -1)
        ]
        column_scores.append(ColumnScore(column_numbers, math_character))
    
    return column_scores


def get_part2_data(array: list[list[str]]) -> list[ColumnScore]:
    """Extract column scores from array data for part 2.
    
    Processes rotated array where numbers are separated by empty rows
    and math operators are in the last row.
    """
    # Remove math character row and rotate the array
    data_rows = array[:-1]
    rotated_array = [list(row) for row in zip(*data_rows)]
    
    # Convert rotated rows to strings
    number_strings = [''.join(row) for row in rotated_array]
    math_characters = [char for char in array[-1] if char.strip()]
    
    column_scores = []
    current_numbers = []
    column_index = 0
    
    # Process numbers, creating a new ColumnScore when encountering empty row
    for number_str in number_strings:
        if number_str.strip():
            current_numbers.append(int(number_str))
        else:
            # Empty row signals end of current column
            if current_numbers:
                math_character = math_characters[column_index]
                column_scores.append(ColumnScore(current_numbers, math_character))
                current_numbers = []
                column_index += 1
    
    # Add the last column
    if current_numbers and column_index < len(math_characters):
        math_character = math_characters[column_index]
        column_scores.append(ColumnScore(current_numbers, math_character))
    
    return column_scores
    
def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    
    # Part 1: Read with space delimiter
    file = GetFile(str(data_file), delimiter=' ')
    column_scores_part1 = get_part1_data(file)
    result1 = time_and_print("Part 1", part1, column_scores_part1)
    
    # Part 2: Read with empty delimiter (character by character)
    file = GetFile(str(data_file), delimiter='')
    array = file.get_2d_array()
    column_scores_part2 = get_part2_data(array)
    result2 = time_and_print("Part 2", part2, column_scores_part2)


if __name__ == "__main__":
    main()
