from helpers.array_helper import Board, Position

# Board symbols
PLAYER = '@'
CLEAN = '.'
TRASH = 'O'
WALL = '#'
TRASH1 = '['
TRASH2 = ']'

# Directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Move symbols
MOVE_RIGHT = '>'
MOVE_LEFT = '<'
MOVE_UP = '^'
MOVE_DOWN = 'v'

# Mapping from move symbols to directions
MOVE_TO_DIRECTION = {
    MOVE_RIGHT: RIGHT,
    MOVE_LEFT: LEFT,
    MOVE_UP: UP,
    MOVE_DOWN: DOWN,
}


class Move:
    """Represents a move made by the player with its symbol and position."""

    def __init__(self, symbol: str, position: Position):
        self.symbol = symbol
        self.position = position

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Move(symbol='{self.symbol}', position=({self.position.row}, {self.position.col}))"



class CleanBoard:
    """Manages the cleaning board game logic."""

    def __init__(self, board: Board, moves: str, should_transform_board=False):
        self.board = self._transform_board(
            board) if should_transform_board else board
        self.moves = moves
        self.moves_done: list[list[Move]] = []
        self.was_wall: bool = False
        self.visited_positions: set[Position] = set()

    def _transform_board(self, board: Board) -> Board:
        """Transform the board to a larger board."""
        # Build a new 2x wide board, copying/expanding symbols row by row.
        new_board = []
        for row in range(board.get_column_length()):
            expanded_row = []
            for col in range(board.get_row_length()):
                cell_char = board.get_character(Position(row, col))
                if cell_char == TRASH:
                    expanded_row.extend(['[', ']'])
                elif cell_char == PLAYER:
                    expanded_row.extend([PLAYER, CLEAN])
                else:
                    expanded_row.extend([cell_char, cell_char])
            new_board.append(expanded_row)

        return Board(new_board)

    def _finish_move(self, moves_done: list[Move]) -> None:
        """Finish the move by placing trash and setting the player position."""
        character_to_place = CLEAN
        for move in moves_done:
            if move.symbol == WALL:
                return
            self.board.set_character_at_position(move.position, character_to_place)
            character_to_place = move.symbol

    def move_player(self, direction: str, player_position: Position, after_trash: bool = False) -> None:
        """Move the player in the given direction until hitting a wall or stopping condition."""
        new_moves_done = []
        
        while True:
            if self.was_wall:
                return
            
            character = self.board.get_character(player_position)
            new_moves_done.append(Move(character, player_position))
            self.visited_positions.add(player_position)
            
            if character == WALL:
                self.was_wall = True
                return

            if character == CLEAN:
                self.moves_done.append(new_moves_done)
                return
            
            # Handle vertical movement through trash pairs
            if not after_trash and direction in (UP, DOWN):
                if character in (TRASH1, TRASH2):
                    second_trash_position = self._get_second_trash_position(player_position, character)
                    if second_trash_position and second_trash_position not in self.visited_positions:
                        self.move_player(direction, second_trash_position, after_trash=True)

            after_trash = False
            player_position = player_position.move(direction)
            
    def _get_second_trash_position(self, player_position: Position, first_trash_symbol: str) -> Position | None:
        """Get the second trash position based on the first trash symbol."""
        if first_trash_symbol == TRASH1:
            return Position(player_position.row, player_position.col + 1)
        elif first_trash_symbol == TRASH2:
            return Position(player_position.row, player_position.col - 1)
        return None
        
    def _move_player_direction(self, move_symbol: str) -> None:
        """Convert move symbol to direction and move the player."""
        player_position = self.board.find_character_position(PLAYER)
        if not player_position:
            return
            
        direction = MOVE_TO_DIRECTION.get(move_symbol)
        if not direction:
            return
            
        self.move_player(direction, player_position)
        
        if self.was_wall:
            # Wall collision: discard all moves and reset
            self.moves_done.clear()
            self.was_wall = False
        else:
            # Apply all moves to the board
            for move_list in self.moves_done:
                self._finish_move(move_list)
        
        self.visited_positions.clear()

    def clean_board(self, debug: bool = False) -> Board:
        """Execute all moves to clean the board.

        Args:
            debug: If True, print debug output after each move.

        Returns:
            The board after all moves are executed.
        """
        for move_symbol in self.moves:
            self._move_player_direction(move_symbol)

            if debug:
                print("--------------------------------")
                print(move_symbol)
                print(self.board)
                print("--------------------------------")

        return self.board
    

def create_board_from_string(board_str: str) -> Board:
    """Helper function to create a Board from a string representation."""
    lines = board_str.strip().split('\n')
    return Board([list(line) for line in lines])

if __name__ == "__main__":
    initial_board = """####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##...[].......[]..##
##[]##....[]......##
##[]......[]..[]..##
##..[][]..@[].[][]##
##........[]......##
####################"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoard(board, "^", False)

    # Execute move
    clean_board.clean_board()
    
    print(clean_board.board)