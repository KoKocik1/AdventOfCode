from helpers.array_helper import Board, Position

# Board symbols
PLAYER = '@'
CLEAN = '.'
TRASH = 'O'
WALL = '#'

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

    def __init__(self, board: Board, moves: str):
        self.board = board
        self.moves = moves
        self.player_position = self.board.find_character_position(PLAYER)

    def _get_position_without_trash(self, moves_done: list[Move]) -> Position | None:
        """Get the position without trash when hitting a wall with < 2 moves.

        Args:
            moves_done: List of moves made during this turn.

        Returns:
            Position to use (second move if available, otherwise first), or None if empty.
        """
        if not moves_done:
            return None
        # Return the second move if available, otherwise the first
        return moves_done[1].position if len(moves_done) > 1 else moves_done[0].position

    def _finish_move(self, moves_done: list[Move], was_wall: bool) -> None:
        """Finish the move by placing trash and setting the player position."""
        trash_count = sum(1 for move in moves_done if move.symbol == TRASH)

        # When hitting a wall with few moves, use a special position
        position_without_trash = None
        if was_wall and len(moves_done) < 2:
            position_without_trash = self._get_position_without_trash(
                moves_done)

        # Process moves in reverse, placing trash until trash_count reaches 0
        for move in reversed(moves_done):
            if trash_count == 0:
                # Place player at appropriate position
                final_position = position_without_trash if position_without_trash else move.position
                self.board.set_character_at_position(final_position, PLAYER)
                self.player_position = final_position
                break
            trash_count -= 1
            self.board.set_character_at_position(move.position, TRASH)

    def move_player(self, direction: str, moves_done: list[Move]) -> None:
        """Move the player in the given direction until hitting a wall or stopping condition."""
        clean_count = 0
        trash_count = 0

        while True:
            new_position = self.player_position.move(direction)

            # Check for wall collision
            if self.board.is_character_at_position(new_position, WALL):
                self._finish_move(moves_done, was_wall=True)
                return

            # Track trash and clean cells encountered
            if self.board.is_character_at_position(new_position, TRASH):
                trash_count = 1
                moves_done.append(Move(TRASH, new_position))

            if self.board.is_character_at_position(new_position, CLEAN):
                clean_count += 1
                moves_done.append(Move(CLEAN, new_position))
                # Stop when clean count equals or exceeds trash count
                if clean_count >= trash_count:
                    self._finish_move(moves_done, was_wall=False)
                    return

            # Mark current position as clean and update player position
            self.board.set_character_at_position(new_position, CLEAN)
            self.player_position = new_position

    def _move_player_direction(self, move_symbol: str, moves_done: list[Move]) -> None:
        """Convert move symbol to direction and move the player."""
        direction = MOVE_TO_DIRECTION.get(move_symbol)
        if direction:
            self.move_player(direction, moves_done)

    def _initialize_move(self, moves_done: list[Move]) -> None:
        """Initialize a move by resetting player position and marking starting position."""
        self.player_position = self.board.find_character_position(PLAYER)
        moves_done.append(Move(PLAYER, self.player_position))
        self.board.set_character_at_position(self.player_position, CLEAN)

    def clean_board(self, debug: bool = False) -> Board:
        """Execute all moves to clean the board.

        Args:
            debug: If True, print debug output after each move.

        Returns:
            The board after all moves are executed.
        """
        for move_symbol in self.moves:
            moves_done: list[Move] = []
            self._initialize_move(moves_done)
            self._move_player_direction(move_symbol, moves_done)

            if debug:
                print(move_symbol)
                print(self.board)
                print("--------------------------------")

        return self.board
