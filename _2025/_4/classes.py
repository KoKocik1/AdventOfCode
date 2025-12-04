from helpers import Position, Board

PAPER_ROLL = '@'
REMOVED_PAPER_ROLL = 'x'

class Forklift:
    def __init__(self, board: Board):
        self.board = board
    
    def check_paper_rolls(self) -> int:
        count = 0
        accessible_paper_rolls = []
        for row in range(self.board.get_row_length()):
            for col in range(self.board.get_column_length()):
                if self.board.is_character_at_position(Position(row, col), PAPER_ROLL):
                    if self.check_surrounding_positions(Position(row, col)):
                        count += 1
                        accessible_paper_rolls.append(Position(row, col))
        return count, accessible_paper_rolls
    
    def check_surrounding_positions(self, position: Position) -> bool:
        count = 0
        for row in range(position.row - 1, position.row + 2):
            for col in range(position.col - 1, position.col + 2):
                if self.board.is_character_at_position(Position(row, col), PAPER_ROLL):
                    count += 1
        return count <= 4
    
    def clear_paper_rolls(self) -> int:
        count = 0
        while True:
            act_count, accessible_paper_rolls = self.check_paper_rolls()
            for position in accessible_paper_rolls:
                self.board.set_character_at_position(position, REMOVED_PAPER_ROLL)
                count += 1
            if act_count == 0:
                break
        return count