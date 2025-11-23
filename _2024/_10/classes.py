from helpers.array_helper import Board, Position, Player


class Climber(Player):
    def __init__(self, board: Board):
        super().__init__(board)
        self.score_positions: set[Position] = set()
        self.score_ways: dict[Position, int] = {}

    def find_trail(self, current_position: Position, last_value: int = -1):
        current_value = int(self.board.get_character(current_position))
        if current_value != last_value + 1:
            return

        if current_value == 9:
            self.score_positions.add(current_position)
            # count occurrences of paths reaching this position
            self.score_ways[current_position] = self.score_ways.get(
                current_position, 0) + 1
            return

        # Explore all four directions
        # Save current direction to restore after recursion
        saved_direction = self.direction
        for _ in self.directions:
            self.turn_right()
            new_position = self.move(current_position)
            if new_position:
                self.find_trail(new_position, current_value)
        # Restore direction state
        self.direction = saved_direction

    def get_score(self) -> int:
        return len(self.score_positions)

    def get_score_ways(self) -> int:
        return sum(self.score_ways.values())
