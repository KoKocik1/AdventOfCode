from helpers import Board, Position, Player, Directions


class SignalSplitter:
    def __init__(self, board: Board):
        self.board = board
        self.splitters: set[Position] = set()
        self.splitter_values: dict[Position, int] = {}
        self.player = Player(self.board, Directions.DOWN)

    def split_signal(self) -> int:
        points_to_visit: list[Position] = []
        start_position = self.board.find_first_character_position('S')
        points_to_visit.append(start_position)
        
        while points_to_visit:
            current_position = points_to_visit.pop(0)
            self.player.set_direction(Directions.DOWN)
            new_position = self.player.move(current_position)
            if new_position:
                if self.board.is_character_at_position(new_position, '^'):
                    if new_position not in self.splitters:
                        self.splitters.add(new_position)
                        self.player.set_direction(Directions.LEFT)
                        left_position=self.player.move(new_position)
                        points_to_visit.append(left_position)
                        self.player.set_direction(Directions.RIGHT)
                        right_position = self.player.move(new_position)
                        points_to_visit.append(right_position)
                elif self.board.is_character_at_position(new_position, '.'):
                    self.board.set_character_at_position(new_position, '|')
                    points_to_visit.append(new_position)
        return len(self.splitters)
    
    def count_signal_lines(self) -> int:
        points_to_visit: list[Position] = []
        start_position = self.board.find_first_character_position('S')
        
        return self._count_line(start_position)

    def _count_line(self, position: Position) -> int:
        
        start_position = position
        if position in self.splitter_values:
            return self.splitter_values[position]
        
        while True:
            self.player.set_direction(Directions.DOWN)
            new_position = self.player.move(position)
            if new_position:
                if self.board.is_character_at_position(new_position, '^'):
                    self.player.set_direction(Directions.LEFT)
                    left_position = self.player.move(new_position)
                    self.player.set_direction(Directions.RIGHT)
                    right_position = self.player.move(new_position)
                    self.splitter_values[start_position] = self._count_line(
                        left_position) + self._count_line(right_position)
                    return self.splitter_values[start_position]
                position = new_position
            else:
                return 1

