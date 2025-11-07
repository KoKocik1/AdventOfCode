from pathlib import Path
from helpers import GetFile
from classes import GridFinder, Word, Position, GridFinderX


def find_words(grid: GridFinder, word: Word, positions: list[Position]) -> int:
    count = 0
    for position in positions:
        if grid.find_horizontal_words_at_position(word, position):
            count += 1
        if grid.find_horizontal_backward_words_at_position(word, position):
            count += 1
        if grid.find_vertical_words_at_position(word, position):
            count += 1
        if grid.find_vertical_backward_words_at_position(word, position):
            count += 1
        if grid.find_diagonal_right_down_words_at_position(word, position):
            count += 1
        if grid.find_diagonal_right_up_words_at_position(word, position):
            count += 1
        if grid.find_diagonal_left_down_words_at_position(word, position):
            count += 1
        if grid.find_diagonal_left_up_words_at_position(word, position):
            count += 1
    return count


def task1(grid: GridFinder):
    word = Word("XMAS")
    positions = grid.look_for_character_position(word.get_character(0))
    count = find_words(grid, word, positions)
    print(count)


def task2(grid: GridFinderX):
    positions = grid.look_for_character_position('A')
    count = 0
    for position in positions:
        if grid.find_words_x('S', 'M', position):
            count += 1
    print(count)


if __name__ == "__main__":
    data_file = Path(__file__).parent / 'data/data.txt'
    file_reader = GetFile(data_file, '')
    two_d_array = file_reader.get_2d_array()
    grid = GridFinder(two_d_array)
    task1(grid)

    grid_x = GridFinderX(two_d_array)
    task2(grid_x)
