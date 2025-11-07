

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

    def look_for_character_position(self, character: str) -> list[Position]:
        positions = []
        for row in range(self.get_column_length()):
            for col in range(self.get_row_length()):
                if self.is_character_at_position(row, col, character):
                    positions.append(Position(row, col))
        return positions


class Word:
    word: list[str]

    def __init__(self, word):
        self.word = list(word)

    def get_length(self) -> int:
        return len(self.word)

    def get_character(self, index: int) -> str:
        return self.word[index]


class GridFinder(Grid):
    def __init__(self, grid):
        super().__init__(grid)

    def find_horizontal_words_at_position(self, word: Word, position: Position) -> bool:
        """Find horizontal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
        if position.col + word.get_length() <= self.get_row_length():
            for i in range(word.get_length()):
                if not self.is_character_at_position(position.row, position.col + i, word.get_character(i)):
                    return False
            return True
        return False

    def find_horizontal_backward_words_at_position(self, word: Word, position: Position) -> bool:
        """Find horizontal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
        if position.col + 1 - word.get_length() >= 0:
            for i in range(word.get_length()):
                if not self.is_character_at_position(position.row, position.col - i, word.get_character(i)):
                    return False
            return True
        return False

    def find_vertical_words_at_position(self, word: Word, position: Position) -> bool:
        """Find vertical occurrences of word in the grid at a specific position (using Grid and Word classes)."""
        if position.row + word.get_length() <= self.get_column_length():
            for i in range(word.get_length()):
                if not self.is_character_at_position(position.row + i, position.col, word.get_character(i)):
                    return False
            return True
        return False

    def find_vertical_backward_words_at_position(self, word: Word, position: Position) -> bool:
        """Find vertical occurrences of word in the grid at a specific position (using Grid and Word classes)."""
        if position.row + 1 - word.get_length() >= 0:
            for i in range(word.get_length()):
                if not self.is_character_at_position(position.row - i, position.col, word.get_character(i)):
                    return False
            return True
        return False

    def find_diagonal_right_down_words_at_position(self, word: Word, position: Position) -> bool:
        """Find diagonal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
        if position.row + word.get_length() <= self.get_column_length() and position.col + word.get_length() <= self.get_row_length():
            for i in range(word.get_length()):
                if not self.is_character_at_position(position.row + i, position.col + i, word.get_character(i)):
                    return False
            return True
        return False

    def find_diagonal_right_up_words_at_position(self, word: Word, position: Position) -> bool:
        """Find diagonal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
        if position.row + 1 - word.get_length() >= 0 and position.col + word.get_length() <= self.get_row_length():
            for i in range(word.get_length()):
                if not self.is_character_at_position(position.row - i, position.col + i, word.get_character(i)):
                    return False
            return True
        return False

    def find_diagonal_left_down_words_at_position(self, word: Word, position: Position) -> bool:
        """Find diagonal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
        if position.row + word.get_length() <= self.get_column_length() and position.col + 1 - word.get_length() >= 0:
            for i in range(word.get_length()):
                if not self.is_character_at_position(position.row + i, position.col - i, word.get_character(i)):
                    return False
            return True
        return False

    def find_diagonal_left_up_words_at_position(self, word: Word, position: Position) -> bool:
        """Find diagonal occurrences of word in the grid at a specific position (using Grid and Word classes)."""
        if position.row + 1 - word.get_length() >= 0 and position.col + 1 - word.get_length() >= 0:
            for i in range(word.get_length()):
                if not self.is_character_at_position(position.row - i, position.col - i, word.get_character(i)):
                    return False
            return True
        return False


class GridFinderX(GridFinder):
    def __init__(self, grid):
        super().__init__(grid)

    def find_words_x(self, characterA: str, characterB: str, position: Position) -> bool:
        if position.col + 1 >= self.get_row_length() or position.row + 1 >= self.get_column_length() or position.col - 1 < 0 or position.row - 1 < 0:
            return False

        right_down_character = self.get_character(
            position.row + 1, position.col + 1)
        right_up_character = self.get_character(
            position.row - 1, position.col + 1)
        left_down_character = self.get_character(
            position.row + 1, position.col - 1)
        left_up_character = self.get_character(
            position.row - 1, position.col - 1)

        if right_down_character == left_up_character or right_up_character == left_down_character:
            return False

        compare_characters = sorted(
            [right_down_character, right_up_character, left_down_character, left_up_character])
        sorted_characters = sorted(
            [characterA, characterA, characterB, characterB])
        if compare_characters == sorted_characters:
            return True
        return False
