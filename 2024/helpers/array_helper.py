
class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    @staticmethod
    def create_from_position(position: 'Position') -> 'Position':
        return Position(position.row, position.col)

    def __eq__(self, other: object) -> bool:
        """Compare two Position objects by their row and col values."""
        if not isinstance(other, Position):
            return False
        return self.row == other.row and self.col == other.col

    def __hash__(self) -> int:
        """Make Position hashable so it can be used in sets and as dictionary keys."""
        return hash((self.row, self.col))


class Board:
    def __init__(self, board: list[list[str]]):
        self.board = board

    def get_row_length(self) -> int:
        return len(self.board[0])

    def get_column_length(self) -> int:
        return len(self.board)

    def get_character(self, position: Position) -> str:
        return self.board[position.row][position.col]

    def is_character_at_position(self, position: Position, character: str) -> bool:
        return self.get_character(position) == character

    def find_character_position(self, character: str) -> Position | None:
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
        """Return a list of all unique characters on the board."""
        characters: set[str] = set()
        for row in range(self.get_column_length()):
            for col in range(self.get_row_length()):
                characters.add(self.get_character(Position(row, col)))
        return list(characters)

    def set_character_at_position(self, position: Position, character: str):
        self.board[position.row][position.col] = character

    def is_out_of_board(self, position: Position) -> bool:
        """Check if a position is outside the board boundaries."""
        return (position.row < 0 or position.row >= self.get_column_length() or
                position.col < 0 or position.col >= self.get_row_length())

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


class Directions:
    UP = 'up'
    RIGHT = 'right'
    DOWN = 'down'
    LEFT = 'left'


class Player:
    def __init__(self, board: Board):
        self.board = board
        self.directions = [Directions.UP, Directions.RIGHT,
                           Directions.DOWN, Directions.LEFT]
        self.direction = 0

    def turn_right(self) -> None:
        self.direction = (self.direction + 1) % 4

    def move(self, current_position: Position) -> Position | None:
        """Move one step in the current direction from the given position."""
        direction_name = self.directions[self.direction]

        if direction_name == Directions.UP:
            new_position = Position(
                current_position.row - 1, current_position.col)
        elif direction_name == Directions.RIGHT:
            new_position = Position(
                current_position.row, current_position.col + 1)
        elif direction_name == Directions.DOWN:
            new_position = Position(
                current_position.row + 1, current_position.col)
        elif direction_name == Directions.LEFT:
            new_position = Position(
                current_position.row, current_position.col - 1)
        else:
            return None

        if self.board.is_out_of_board(new_position):
            return None
        return new_position

    def is_valid_position(self, position: Position, character: str) -> bool:
        """Check if position does NOT contain the specified character."""
        return not self.board.is_character_at_position(position, character)
