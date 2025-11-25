from helpers.array_helper import Board, Position
from helpers.array_helper import Player, Directions

MOVE_COST = 1
TURN_COST = 1000

ALLOWED_CHARACTERS = ['S', 'E', '.']
class MazeSolver:
    def __init__(self, board: Board):
        self.board = board
        self.visited = {}  # Dictionary: (position, direction) -> score
        self.end = self.board.find_first_character_position('E')
        self.scores = []

    def solve(self) -> int:
        start = self.board.find_first_character_position('S')
        self.move(start, Directions.RIGHT, 0)

    def is_visited(self, position: Position, direction: str) -> bool:
        """Check if position and direction combination is visited."""
        key = (position, direction)
        return key in self.visited

    def move(self, position: Position, direction: Directions, score: int) -> None:
        moves_to_do = []
        moves_to_do.append((position, direction, score))
        while moves_to_do:
            position, direction, score = moves_to_do.pop(0)
            key = (position, direction)
            if self.end == position:
                self.scores.append(score)
                #print(f"Score: {score}")
                continue
                
            if self.is_visited(position, direction):
                # If we already have a better or equal path, skip
                if self.visited[key] <= score:
                    continue
                # Found a better path (lower score), update it
            self.visited[key] = score
            
            player = Player(self.board, direction)
            new_position = player.move(position)
            if new_position and any(self.board.is_character_at_position(new_position, ch) for ch in ALLOWED_CHARACTERS):
                moves_to_do.append((new_position, direction, score + MOVE_COST))
            player = Player(self.board, direction)
            player.turn_right()
            moves_to_do.append((position, player.get_direction(), score + TURN_COST))
            
            player = Player(self.board, direction)
            player.turn_left()
            moves_to_do.append((position, player.get_direction(), score + TURN_COST))
