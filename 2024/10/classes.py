from helpers import Board, Position, Player


class Climber(Player):
    def __init__(self, board: Board):
        super().__init__(board)
        self.score_positions: set[Position] = set()
        self.score_ways: dict[Position, int] = {}

    def find_trail(self, current_position: Position, last_value: int = -1):
        act_value = int(self.board.get_character(current_position))
        if act_value != last_value + 1:
            return
        if act_value == 9:
            self.score_positions.add(current_position)
            # count occurrences of paths reaching this position
            self.score_ways[current_position] = self.score_ways.get(
                current_position, 0) + 1
            return
        player = Player(self.board)
        for _ in self.directions:
            player.turn_right()
            new_position = player.move(current_position)
            if new_position:
                self.find_trail(new_position, act_value)

    def get_score(self) -> int:
        return len(self.score_positions)

    def get_score_ways(self) -> int:
        return sum(self.score_ways.values())
