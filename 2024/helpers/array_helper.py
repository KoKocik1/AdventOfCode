class Position:
    row: int
    col: int

    def __init__(self, row, col):
        self.row = row
        self.col = col

    @staticmethod
    def create_from_position(position: 'Position'):
        return Position(position.row, position.col)

    def __eq__(self, other):
        """Compare two Position objects by their row and col values."""
        if not isinstance(other, Position):
            return False
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        """Make Position hashable so it can be used in sets and as dictionary keys."""
        return hash((self.row, self.col))


class Board:
    board: list[list[str]]

    def __init__(self, board):
        self.board = board

    def get_row_length(self) -> int:
        return len(self.board[0])

    def get_column_length(self) -> int:
        return len(self.board)

    def get_character(self, position: Position) -> str:
        return self.board[position.row][position.col]

    def is_character_at_position(self, position: Position, character: str) -> bool:
        return self.get_character(position) == character

    def find_character_position(self, character: str) -> Position:
        for row in range(self.get_column_length()):
            for col in range(self.get_row_length()):
                if self.is_character_at_position(Position(row, col), character):
                    return Position(row, col)
        return None

    def find_all_character_positions(self, character: str) -> list[Position]:
        positions = []
        for row in range(self.get_column_length()):
            for col in range(self.get_row_length()):
                if self.is_character_at_position(Position(row, col), character):
                    positions.append(Position(row, col))
        return positions

    def get_all_characters(self) -> list[str]:
        characters = set()
        for row in range(self.get_column_length()):
            for col in range(self.get_row_length()):
                characters.add(self.get_character(Position(row, col)))
        return list(characters)

    def set_character_at_position(self, position: Position, character: str):
        self.board[position.row][position.col] = character

    def is_out_of_board(self, position: Position) -> bool:
        return position.row < 0 or position.row >= self.get_column_length() or position.col < 0 or position.col >= self.get_row_length()

    def count_characters(self, character: str) -> int:
        count = 0
        for row in range(self.get_column_length()):
            for col in range(self.get_row_length()):
                if self.is_character_at_position(Position(row, col), character):
                    count += 1
        return count

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.board])

    def __repr__(self):
        return self.__str__()
