from pathlib import Path

from helpers import GetFile, time_and_print
from helpers.array_helper import Board
from helpers.array_helper import Position
from _2025._6.classes import ColumnScore


def part1(column_scores: list[ColumnScore]) -> int:
    row_scores = []
    for column_score in column_scores:
        row_scores.append(column_score.calculate_score())
    return sum(row_scores)


def part2(column_scores: list[ColumnScore]) -> int:
    row_scores = []
    for column_score in column_scores:
        row_scores.append(column_score.calculate_score())
    return sum(row_scores)

def get_part1_data(file: GetFile) -> list[ColumnScore]:
    array = [[col for col in row if col != ''] for row in file.get_row(strip=False)]
    board = Board(array)
    column_scores = []
    
    last_row = board.get_column_length() - 1
    for col in range(board.get_row_length()):
        math_character = board.get_character(Position(last_row, col))
        column = []
        for row in range(last_row-1, -1, -1):
            column.append(int(board.get_character(Position(row, col))))
        column_score = ColumnScore(column, math_character)
        column_scores.append(column_score)
    return column_scores

def check_column_empty(row: list[str]) -> bool:
    for col in row:
        if col != '':
            return False
    return True


def get_part2_data(array: list[list[str]]) -> list[ColumnScore]:
    array_without_math_characters = array[:-1]  
    rotated_array = [list(row)
                     for row in zip(*array_without_math_characters)]
    column_scores = []
    math_character = ''
    
    numbers = [''.join(row) for row in rotated_array]
    math_characters = [row for row in array[-1] if row[-1] != ' ']
    act_numbers = []
    act_column=0
    for row in numbers[:-1]:
        if row.strip():
            act_numbers.append(int(row))
        else:
            math_character = math_characters[act_column]
            column_score = ColumnScore(act_numbers, math_character)
            act_numbers = []
            act_column += 1
            column_scores.append(column_score)
            
    math_character = math_characters[act_column]
    column_score = ColumnScore(act_numbers, math_character)
    act_numbers = []
    act_column += 1
    column_scores.append(column_score)
    
    return column_scores
    
def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=' ')
    column_scores = get_part1_data(file)
    result1 = time_and_print("Part 1", part1, column_scores)
    
    file = GetFile(str(data_file), delimiter='')
    array = file.get_2d_array()
    column_scores2 = get_part2_data(array)
    result2 = time_and_print("Part 2", part2, column_scores2)


if __name__ == "__main__":
    main()
