

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
    # Direction vectors: (row_delta, col_delta) for each direction
    DIRECTIONS = [
        (0, 1),   # horizontal (right)
        (0, -1),  # horizontal_backward (left)
        (1, 0),   # vertical (down)
        (-1, 0),  # vertical_backward (up)
        (1, 1),   # diagonal_right_down
        (-1, 1),  # diagonal_right_up
        (1, -1),  # diagonal_left_down
        (-1, -1),  # diagonal_left_up
    ]

    def __init__(self, grid):
        super().__init__(grid)

    def _find_word_at_position_in_direction(self, word: Word, position: Position,
                                            row_delta: int, col_delta: int) -> bool:
        """Generic method to find word at position in a given direction (character-by-character checking)."""
        word_len = word.get_length()

        # Calculate final position
        final_row = position.row + (word_len - 1) * row_delta
        final_col = position.col + (word_len - 1) * col_delta

        # Check bounds
        if (final_row < 0 or final_row >= self.get_column_length() or
                final_col < 0 or final_col >= self.get_row_length()):
            return False

        # Check character by character
        for i in range(word_len):
            check_row = position.row + i * row_delta
            check_col = position.col + i * col_delta
            if not self.is_character_at_position(check_row, check_col, word.get_character(i)):
                return False
        return True

    def find_horizontal_words_at_position(self, word: Word, position: Position) -> bool:
        """Find horizontal occurrences (left to right)."""
        return self._find_word_at_position_in_direction(word, position, 0, 1)

    def find_horizontal_backward_words_at_position(self, word: Word, position: Position) -> bool:
        """Find horizontal occurrences (right to left)."""
        return self._find_word_at_position_in_direction(word, position, 0, -1)

    def find_vertical_words_at_position(self, word: Word, position: Position) -> bool:
        """Find vertical occurrences (top to bottom)."""
        return self._find_word_at_position_in_direction(word, position, 1, 0)

    def find_vertical_backward_words_at_position(self, word: Word, position: Position) -> bool:
        """Find vertical occurrences (bottom to top)."""
        return self._find_word_at_position_in_direction(word, position, -1, 0)

    def find_diagonal_right_down_words_at_position(self, word: Word, position: Position) -> bool:
        """Find diagonal occurrences (top-left to bottom-right)."""
        return self._find_word_at_position_in_direction(word, position, 1, 1)

    def find_diagonal_right_up_words_at_position(self, word: Word, position: Position) -> bool:
        """Find diagonal occurrences (bottom-left to top-right)."""
        return self._find_word_at_position_in_direction(word, position, -1, 1)

    def find_diagonal_left_down_words_at_position(self, word: Word, position: Position) -> bool:
        """Find diagonal occurrences (top-right to bottom-left)."""
        return self._find_word_at_position_in_direction(word, position, 1, -1)

    def find_diagonal_left_up_words_at_position(self, word: Word, position: Position) -> bool:
        """Find diagonal occurrences (bottom-right to top-left)."""
        return self._find_word_at_position_in_direction(word, position, -1, -1)


class GridFinderX(GridFinder):
    def __init__(self, grid):
        super().__init__(grid)

    def find_words_x(self, characterA: str, characterB: str, position: Position) -> bool:
        """Find X pattern: center 'A' with diagonal characters matching characterA and characterB."""
        # Check bounds for all diagonal positions
        if (position.col + 1 >= self.get_row_length() or
            position.row + 1 >= self.get_column_length() or
            position.col - 1 < 0 or
                position.row - 1 < 0):
            return False

        # Get diagonal characters
        diagonal_chars = {
            'right_down': self.get_character(position.row + 1, position.col + 1),
            'right_up': self.get_character(position.row - 1, position.col + 1),
            'left_down': self.get_character(position.row + 1, position.col - 1),
            'left_up': self.get_character(position.row - 1, position.col - 1),
        }

        # Check if opposite corners have same character (invalid X pattern)
        if (diagonal_chars['right_down'] == diagonal_chars['left_up'] or
                diagonal_chars['right_up'] == diagonal_chars['left_down']):
            return False

        # Check if diagonal characters match the expected pattern (2x characterA, 2x characterB)
        diagonal_list = list(diagonal_chars.values())
        expected_chars = sorted(
            [characterA, characterA, characterB, characterB])
        return sorted(diagonal_list) == expected_chars
