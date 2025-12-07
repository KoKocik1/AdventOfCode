from collections import deque
from helpers import Board, Position, Player, Directions


# Constants for board characters
START_CHAR = 'S'
SPLITTER_CHAR = '^'
EMPTY_CHAR = '.'
VISITED_CHAR = '|'


class SignalSplitter:
    """Handles signal splitting and counting signal lines on a board."""
    
    def __init__(self, board: Board):
        self.board = board
        self.splitters: set[Position] = set()
        self.splitter_values: dict[Position, int] = {}
        self.player = Player(self.board, Directions.DOWN)

    def split_signal(self) -> int:
        """Split signal and count unique splitters encountered.
        
        Uses BFS to traverse the board, marking visited positions
        and tracking splitter positions.
        """
        start_position = self.board.find_first_character_position(START_CHAR)
        if not start_position:
            return 0
        
        queue = deque([start_position])
        
        while queue:
            current_position = queue.popleft()
            self.player.set_direction(Directions.DOWN)
            next_position = self.player.move(current_position)
            
            if not next_position:
                continue
            
            if self.board.is_character_at_position(next_position, SPLITTER_CHAR):
                self._handle_splitter(next_position, queue)
            elif self.board.is_character_at_position(next_position, EMPTY_CHAR):
                self.board.set_character_at_position(next_position, VISITED_CHAR)
                queue.append(next_position)
        
        return len(self.splitters)
    
    def _handle_splitter(self, splitter_position: Position, queue: deque) -> None:
        """Handle a splitter position by adding left and right paths to queue."""
        if splitter_position not in self.splitters:
            self.splitters.add(splitter_position)
            
            # Add left path
            self.player.set_direction(Directions.LEFT)
            left_position = self.player.move(splitter_position)
            if left_position:
                queue.append(left_position)
            
            # Add right path
            self.player.set_direction(Directions.RIGHT)
            right_position = self.player.move(splitter_position)
            if right_position:
                queue.append(right_position)
    
    def count_signal_lines(self) -> int:
        """Count total signal lines using recursive counting with memoization."""
        start_position = self.board.find_first_character_position(START_CHAR)
        if not start_position:
            return 0
        
        return self._count_line(start_position)

    def _count_line(self, position: Position) -> int:
        """Recursively count signal lines from a given position.
        
        Uses memoization to cache results for splitter positions.
        """
        # Check memoization cache
        if position in self.splitter_values:
            return self.splitter_values[position]
        
        start_position = position
        
        # Traverse down until we hit a splitter or boundary
        while True:
            self.player.set_direction(Directions.DOWN)
            next_position = self.player.move(position)
            
            if not next_position:
                # Reached boundary - single line
                return 1
            
            if self.board.is_character_at_position(next_position, SPLITTER_CHAR):
                # Found splitter - recursively count left and right paths
                self.player.set_direction(Directions.LEFT)
                left_position = self.player.move(next_position)
                
                self.player.set_direction(Directions.RIGHT)
                right_position = self.player.move(next_position)
                
                # Calculate and cache the result
                left_count = self._count_line(left_position) if left_position else 0
                right_count = self._count_line(right_position) if right_position else 0
                total_count = left_count + right_count
                
                self.splitter_values[start_position] = total_count
                return total_count
            
            position = next_position

