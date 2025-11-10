class Position:
    row: int
    col: int

    def __init__(self, row, col):
        self.row = row
        self.col = col

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

    def get_board(self) -> list[list[str]]:
        return self.board

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

    def change_all_characters(self, character: str, new_character: str):
        for row in range(self.get_column_length()):
            for col in range(self.get_row_length()):
                if self.is_character_at_position(row, col, character):
                    self.set_character_at_position(row, col, new_character)

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.board])

    def __repr__(self):
        return self.__str__()

    def deep_copy(self):
        return Board([[char for char in row] for row in self.board])


class Player:
    position: Position

    def __init__(self, position):
        self.position = position
        self.direction = 0
        self.directions = ['up', 'right', 'down', 'left']
        self.moved = False

    def get_position(self) -> Position:
        return self.position

    def get_front_position(self) -> Position:
        new_position = Position(self.position.row, self.position.col)
        if self.directions[self.direction] == 'up':
            new_position.row -= 1
        elif self.directions[self.direction] == 'down':
            new_position.row += 1
        elif self.directions[self.direction] == 'left':
            new_position.col -= 1
        elif self.directions[self.direction] == 'right':
            new_position.col += 1
        return new_position

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

    def add_obstacle_in_front(self, board: Board) -> tuple[bool, Position]:
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
            return (False, None)
        else:
            if board.is_character_at_position(new_position.row, new_position.col, '#'):
                return (False, None)
            elif board.is_character_at_position(new_position.row, new_position.col, '+'):
                return (False, None)
            else:
                board.set_character_at_position(
                    new_position.row, new_position.col, 'O')
                return (True, new_position)

    def copy(self) -> 'Player':
        """Create a deep copy of the Player object."""
        copied_player = Player(Position(self.position.row, self.position.col))
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


class Bot:
    def __init__(self):
        self.obstacles = []
        self.start_point = None

    def set_start_point(self, start_point: Position):
        self.start_point = start_point

    def add_obstacle(self, obstacle: Position):
        self.obstacles.append(obstacle)

    def is_obstacle_at_position(self, position: Position) -> bool:
        return position in self.obstacles

    def test_loop(self, board: Board, player: Player) -> bool:

        visited_states = VisitedStates()  # (row, col, direction_index)
        bot = player.copy()

        while True:
            if not bot.move(board):
                return False
            state = (bot.get_position().row,
                     bot.get_position().col, bot.direction)
            board.set_character_at_position(
                bot.get_position().row, bot.get_position().col, '+')
            # print(f"test_board:\n{test_board}")
            # print(test_board)

            # Loop detected within this simulation
            if visited_states.is_visited_state(state):
                return True
            visited_states.add_visited_state(state)
        return False
