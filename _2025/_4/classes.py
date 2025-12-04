from helpers import Position, Board

PAPER_ROLL = '@'
REMOVED_PAPER_ROLL = 'x'
MAX_SURROUNDING_ROLLS = 4


class Forklift:
    """Forklift for managing paper rolls on a board."""
    
    def __init__(self, board: Board):
        self.board = board
    
    def check_paper_rolls(self) -> list[Position]:
        """Find all accessible paper rolls (with <= 4 surrounding rolls)."""
        accessible_paper_rolls = []
        
        for row in range(self.board.get_row_length()):
            for col in range(self.board.get_column_length()):
                position = Position(row, col)
                if (self.board.is_character_at_position(position, PAPER_ROLL) and
                    self._is_accessible(position)):
                    accessible_paper_rolls.append(position)
        
        return accessible_paper_rolls
    
    def _is_accessible(self, position: Position) -> bool:
        """Check if a paper roll is accessible (has <= 4 surrounding rolls)."""
        surrounding_count = 0
        
        for row in range(position.row - 1, position.row + 2):
            for col in range(position.col - 1, position.col + 2):
                if self.board.is_character_at_position(Position(row, col), PAPER_ROLL):
                    surrounding_count += 1
        
        return surrounding_count <= MAX_SURROUNDING_ROLLS
    
    def clear_paper_rolls(self) -> int:
        """Remove all accessible paper rolls iteratively until none remain."""
        total_removed = 0
        
        while True:
            accessible_positions = self.check_paper_rolls()
            
            if not accessible_positions:
                break
            
            for position in accessible_positions:
                self.board.set_character_at_position(position, REMOVED_PAPER_ROLL)
                total_removed += 1
        
        return total_removed