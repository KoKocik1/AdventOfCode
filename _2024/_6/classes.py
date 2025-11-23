from helpers.array_helper import Position, Board


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
            if board.is_character_at_position(new_position, '#') or board.is_character_at_position(new_position, 'O'):
                self.turn_right()
                return self.move(board)
            else:
                self.position = new_position
                self.moved = True
            board.set_character_at_position(
                self.position, 'X')
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
