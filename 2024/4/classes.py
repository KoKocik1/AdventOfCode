

class Position:
    row: int
    col: int

    def __init__(self, row, col):
        self.row = row
        self.col = col


class Grid:
    grid: list[list[str]]

    def __init__(self, grid):
        self.grid = grid

    def get_row_length(self) -> int:
        return len(self.grid[0])

    def get_column_length(self) -> int:
        return len(self.grid)

    def get_character(self, row: int, col: int) -> str:
        return self.grid[row][col]

    def is_character_at_position(self, row, col, character) -> bool:
        return self.get_character(row, col) == character


class Word:
    word: list[str]

    def __init__(self, word):
        self.word = list(word)

    def get_length(self) -> int:
        return len(self.word)

    def get_character(self, index: int) -> str:
        return self.word[index]
