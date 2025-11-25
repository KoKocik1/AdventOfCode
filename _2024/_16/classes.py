from helpers.array_helper import Board, Position
from helpers.array_helper import Player, Directions

MOVE_COST = 1
TURN_COST = 1000

ALLOWED_CHARACTERS = ['S', 'E', '.']
class MazeSolver:
    def __init__(self, board: Board):
        self.board = board
        self.visited = {}  # Dictionary: (position, direction) -> score
        self.connections = {}  # Dictionary: (position, direction) -> (position, direction), score
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
        moves_to_do.append((position, direction, score, position))
        last_position = position        
        while moves_to_do:
            position, direction, score, last_position = moves_to_do.pop(0)
            key = (position, direction)
            if position not in self.connections:
                self.connections[position] = []
            self.connections[position].append((last_position, score))
            
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
                moves_to_do.append((new_position, direction, score + MOVE_COST, position))
            player = Player(self.board, direction)
            player.turn_right()
            moves_to_do.append((position, player.get_direction(), score + TURN_COST, position))
            
            player = Player(self.board, direction)
            player.turn_left()
            moves_to_do.append((position, player.get_direction(), score + TURN_COST, position))

    def mark_path(self, act_score: int) -> None:
        """Mark all positions on optimal paths by backtracking from the end."""
        end = self.board.find_first_character_position('E')
        visited = set()
        processed = set()  # Track (position, score) pairs to avoid duplicates
        queue = [(end, act_score)]
        
        self.board.set_character_at_position(end, 'O')
        visited.add(end)
        processed.add((end, act_score))
        
        while queue:
            position, current_score = queue.pop(0)
            if position not in self.connections:
                continue

            for prev_position, stored_score in self.connections[position]:
                # If stored_score matches current_score, this is part of an optimal path
                if stored_score == current_score and prev_position not in visited:
                    self.board.set_character_at_position(prev_position, 'O')
                    visited.add(prev_position)
                    
                    # Continue backtracking if not at start
                    if not self.board.is_character_at_position(prev_position, 'S'):
                        for cost in [MOVE_COST, TURN_COST + MOVE_COST, TURN_COST]:
                            prev_score = current_score - cost
                            if prev_score >= 0:
                                path_key = (prev_position, prev_score)
                                if path_key not in processed:
                                    processed.add(path_key)
                                    queue.append((prev_position, prev_score))