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

    def get_character(self, row: int, col: int) -> str:
        return self.board[row][col]

    def is_character_at_position(self, row: int, col: int, character: str) -> bool:
        return self.get_character(row, col) == character

    def find_character_position(self, character: str) -> Position:
        for row in range(self.get_column_length()):
            for col in range(self.get_row_length()):
                if self.is_character_at_position(row, col, character):
                    return Position(row, col)
        return None

    def set_character_at_position(self, row: int, col: int, character: str):
        self.board[row][col] = character

    def is_out_of_board(self, position: Position) -> bool:
        return position.row < 0 or position.row >= self.get_column_length() or position.col < 0 or position.col >= self.get_row_length()

    def count_characters(self, character: str) -> int:
        count = 0
        for row in range(self.get_column_length()):
            for col in range(self.get_row_length()):
                if self.is_character_at_position(row, col, character):
                    count += 1
        return count

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.board])

    def __repr__(self):
        return self.__str__()


class Player:
    position: Position

    def __init__(self, position):
        self.position = position
        self.direction = 0
        self.directions = ['up', 'right', 'down', 'left']
        self.moved = False

    def get_position(self) -> Position:
        return self.position

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def move(self, board: Board):

        new_position = Position(self.position.row, self.position.col)
        if self.directions[self.direction] == 'up':
            new_position.row -= 1
        elif self.directions[self.direction] == 'down':
            new_position.row += 1
        elif self.directions[self.direction] == 'left':
            new_position.col -= 1
        elif self.directions[self.direction] == 'right':
            new_position.col += 1

        if board.is_out_of_board(new_position):
            return False
        else:
            if board.is_character_at_position(new_position.row, new_position.col, '#') or board.is_character_at_position(new_position.row, new_position.col, 'O'):
                self.turn_right()
                return self.move(board)
            else:
                self.position = new_position
                self.moved = True
            board.set_character_at_position(
                self.position.row, self.position.col, 'X')
            return True

    def copy(self) -> 'Player':
        """Create a deep copy of the Player object."""
        copied_player = Player(Position.create_from_position(self.position))
        copied_player.direction = self.direction
        copied_player.directions = self.directions.copy()  # Copy the list
        copied_player.moved = False
        return copied_player


class VisitedState:
    def __init__(self, position: Position, direction: int = 0):
        self.position = position
        self.direction = direction

    def __eq__(self, other):
        if not isinstance(other, VisitedState):
            return NotImplemented
        return (self.position.row == other.position.row and
                self.position.col == other.position.col and
                self.direction == other.direction)

    def __hash__(self):
        return hash((self.position.row, self.position.col, self.direction))


class VisitedStates:
    # class to keep information about visited position and direction on this position
    def __init__(self):
        self.visited_states = set()

    def add_visited_state(self, state: VisitedState):
        self.visited_states.add(state)

    def is_visited_state(self, state: VisitedState) -> bool:
        return state in self.visited_states


class LoopChecker:
    def __init__(self, start_point: Position = None):
        self.obstacles = []
        self.start_point = start_point

    def test_loop(self, board: Board, player: Player) -> bool:

        visited_states = VisitedStates()  # track (position, direction)
        bot = player.copy()

        while True:
            if not bot.move(board):
                return False
            visited_state = VisitedState(
                Position.create_from_position(bot.get_position()), bot.direction)

            # Loop detected within this simulation
            if visited_states.is_visited_state(visited_state):
                return True
            visited_states.add_visited_state(visited_state)
        return False
