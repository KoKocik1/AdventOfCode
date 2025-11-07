from helpers import GetFile
from classes import Grid, Word, Position


def look_for_character_position(grid: Grid, character: str) -> list[Position]:
    positions = []
    for row in range(grid.get_column_length()):
        for col in range(grid.get_row_length()):
            if grid.is_character_at_position(row, col, character):
                positions.append(Position(row, col))
    return positions


def find_horizontal_words_at_position(grid: Grid, word: Word, position: Position) -> bool:
    """Find horizontal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
    if position.col + word.get_length() <= grid.get_row_length():
        for i in range(word.get_length()):
            if not grid.is_character_at_position(position.row, position.col + i, word.get_character(i)):
                return False
        return True
    return False


def find_horizontal_backward_words_at_position(grid: Grid, word: Word, position: Position) -> bool:
    """Find horizontal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
    if position.col + 1 - word.get_length() >= 0:
        for i in range(word.get_length()):
            if not grid.is_character_at_position(position.row, position.col - i, word.get_character(i)):
                return False
        return True
    return False


def find_vertical_words_at_position(grid: Grid, word: Word, position: Position) -> bool:
    """Find vertical occurrences of word in the grid at a specific position (using Grid and Word classes)."""
    if position.row + word.get_length() <= grid.get_column_length():
        for i in range(word.get_length()):
            if not grid.is_character_at_position(position.row + i, position.col, word.get_character(i)):
                return False
        return True
    return False


def find_vertical_backward_words_at_position(grid: Grid, word: Word, position: Position) -> bool:
    """Find vertical occurrences of word in the grid at a specific position (using Grid and Word classes)."""
    if position.row + 1 - word.get_length() >= 0:
        for i in range(word.get_length()):
            if not grid.is_character_at_position(position.row - i, position.col, word.get_character(i)):
                return False
        return True
    return False


def find_diagonal_right_down_words_at_position(grid: Grid, word: Word, position: Position) -> bool:
    """Find diagonal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
    if position.row + word.get_length() <= grid.get_column_length() and position.col + word.get_length() <= grid.get_row_length():
        for i in range(word.get_length()):
            if not grid.is_character_at_position(position.row + i, position.col + i, word.get_character(i)):
                return False
        return True
    return False


def find_diagonal_right_up_words_at_position(grid: Grid, word: Word, position: Position) -> bool:
    """Find diagonal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
    if position.row + 1 - word.get_length() >= 0 and position.col + word.get_length() <= grid.get_row_length():
        for i in range(word.get_length()):
            if not grid.is_character_at_position(position.row - i, position.col + i, word.get_character(i)):
                return False
        return True
    return False


def find_diagonal_left_down_words_at_position(grid: Grid, word: Word, position: Position) -> bool:
    """Find diagonal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
    if position.row + word.get_length() <= grid.get_column_length() and position.col + 1 - word.get_length() >= 0:
        for i in range(word.get_length()):
            if not grid.is_character_at_position(position.row + i, position.col - i, word.get_character(i)):
                return False
        return True
    return False


def find_diagonal_left_up_words_at_position(grid: Grid, word: Word, position: Position) -> bool:
    """Find diagonal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
    if position.row + 1 - word.get_length() >= 0 and position.col + 1 - word.get_length() >= 0:
        for i in range(word.get_length()):
            if not grid.is_character_at_position(position.row - i, position.col - i, word.get_character(i)):
                return False
        return True
    return False


def find_words(grid: Grid, word: Word, positions: list[Position]) -> int:
    count = 0
    for position in positions:
        if find_horizontal_words_at_position(grid, word, position):
            count += 1
        if find_horizontal_backward_words_at_position(grid, word, position):
            count += 1
        if find_vertical_words_at_position(grid, word, position):
            count += 1
        if find_vertical_backward_words_at_position(grid, word, position):
            count += 1
        if find_diagonal_right_down_words_at_position(grid, word, position):
            count += 1
        if find_diagonal_right_up_words_at_position(grid, word, position):
            count += 1
        if find_diagonal_left_down_words_at_position(grid, word, position):
            count += 1
        if find_diagonal_left_up_words_at_position(grid, word, position):
            count += 1
    return count


if __name__ == "__main__":
    file_reader = GetFile(
        '/Users/krzysztofkokot/Projects/Algorithms/2024/4/data.txt', '')
    two_d_array = file_reader.get_2d_array()
    grid = Grid(two_d_array)
    word = Word("XMAS")
    positions = look_for_character_position(grid, word.get_character(0))
    count = find_words(grid, word, positions)
    print(count)
