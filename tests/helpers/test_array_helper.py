"""Tests for helpers.array_helper module."""

import pytest
from helpers.array_helper import Position, Board, Player, Directions


class TestPosition:
    """Tests for Position class."""

    def test_initialization(self):
        """Test Position initialization."""
        pos = Position(5, 10)
        assert pos.row == 5
        assert pos.col == 10

    def test_create_from_position(self):
        """Test creating Position from another Position."""
        original = Position(3, 7)
        copy = Position.create_from_position(original)
        assert copy.row == 3
        assert copy.col == 7
        assert copy is not original  # Should be a new object

    def test_move_up(self):
        """Test moving position up."""
        pos = Position(5, 5)
        new_pos = pos.move('up')
        assert new_pos.row == 4
        assert new_pos.col == 5

    def test_move_down(self):
        """Test moving position down."""
        pos = Position(5, 5)
        new_pos = pos.move('down')
        assert new_pos.row == 6
        assert new_pos.col == 5

    def test_move_left(self):
        """Test moving position left."""
        pos = Position(5, 5)
        new_pos = pos.move('left')
        assert new_pos.row == 5
        assert new_pos.col == 4

    def test_move_right(self):
        """Test moving position right."""
        pos = Position(5, 5)
        new_pos = pos.move('right')
        assert new_pos.row == 5
        assert new_pos.col == 6

    def test_move_invalid_direction(self):
        """Test moving with invalid direction."""
        pos = Position(5, 5)
        result = pos.move('invalid')
        assert result is None

    def test_equality(self):
        """Test Position equality comparison."""
        pos1 = Position(3, 4)
        pos2 = Position(3, 4)
        pos3 = Position(3, 5)
        
        assert pos1 == pos2
        assert pos1 != pos3
        assert pos1 != "not a position"

    def test_hash(self):
        """Test Position hashing for use in sets and dicts."""
        pos1 = Position(3, 4)
        pos2 = Position(3, 4)
        pos3 = Position(3, 5)
        
        pos_set = {pos1, pos2, pos3}
        assert len(pos_set) == 2  # pos1 and pos2 are equal


class TestBoard:
    """Tests for Board class."""

    def test_initialization(self):
        """Test Board initialization."""
        board_data = [['a', 'b'], ['c', 'd']]
        board = Board(board_data)
        assert board.get_row_length() == 2
        assert board.get_column_length() == 2

    def test_get_character(self):
        """Test getting character at position."""
        board_data = [['a', 'b'], ['c', 'd']]
        board = Board(board_data)
        pos = Position(0, 1)
        assert board.get_character(pos) == 'b'

    def test_set_character_at_position(self):
        """Test setting character at position."""
        board_data = [['a', 'b'], ['c', 'd']]
        board = Board(board_data)
        pos = Position(0, 1)
        board.set_character_at_position(pos, 'x')
        assert board.get_character(pos) == 'x'

    def test_is_character_at_position(self):
        """Test checking if character is at position."""
        board_data = [['a', 'b'], ['c', 'd']]
        board = Board(board_data)
        pos = Position(0, 0)
        assert board.is_character_at_position(pos, 'a') is True
        assert board.is_character_at_position(pos, 'b') is False
        assert board.is_character_at_position(None, 'a') is False

    def test_find_character_position(self):
        """Test finding first character position."""
        board_data = [['a', 'b'], ['c', 'a']]
        board = Board(board_data)
        pos = board.find_character_position('a')
        assert pos is not None
        assert pos.row == 0
        assert pos.col == 0

    def test_find_character_position_not_found(self):
        """Test finding character that doesn't exist."""
        board_data = [['a', 'b'], ['c', 'd']]
        board = Board(board_data)
        pos = board.find_character_position('x')
        assert pos is None

    def test_find_all_character_positions(self):
        """Test finding all positions of a character."""
        board_data = [['a', 'b'], ['c', 'a']]
        board = Board(board_data)
        positions = board.find_all_character_positions('a')
        assert len(positions) == 2
        assert Position(0, 0) in positions
        assert Position(1, 1) in positions

    def test_find_first_character_position(self):
        """Test finding first character position."""
        board_data = [['a', 'b'], ['c', 'a']]
        board = Board(board_data)
        pos = board.find_first_character_position('a')
        assert pos.row == 0
        assert pos.col == 0

    def test_get_all_characters(self):
        """Test getting all unique characters."""
        board_data = [['a', 'b'], ['c', 'a']]
        board = Board(board_data)
        characters = board.get_all_characters()
        assert set(characters) == {'a', 'b', 'c'}

    def test_is_out_of_board(self):
        """Test checking if position is out of board."""
        board_data = [['a', 'b'], ['c', 'd']]
        board = Board(board_data)
        
        assert board.is_out_of_board(Position(-1, 0)) is True
        assert board.is_out_of_board(Position(0, -1)) is True
        assert board.is_out_of_board(Position(2, 0)) is True
        assert board.is_out_of_board(Position(0, 2)) is True
        assert board.is_out_of_board(Position(0, 0)) is False
        assert board.is_out_of_board(Position(1, 1)) is False

    def test_count_characters(self):
        """Test counting characters on board."""
        board_data = [['a', 'b'], ['c', 'a']]
        board = Board(board_data)
        assert board.count_characters('a') == 2
        assert board.count_characters('b') == 1
        assert board.count_characters('x') == 0

    def test_str_representation(self):
        """Test string representation of board."""
        board_data = [['a', 'b'], ['c', 'd']]
        board = Board(board_data)
        board_str = str(board)
        assert board_str == 'ab\ncd'

    def test_repr_representation(self):
        """Test repr representation of board."""
        board_data = [['a', 'b'], ['c', 'd']]
        board = Board(board_data)
        board_repr = repr(board)
        assert board_repr == 'ab\ncd'


class TestPlayer:
    """Tests for Player class."""

    def test_initialization(self):
        """Test Player initialization."""
        board_data = [['.', '.'], ['.', '.']]
        board = Board(board_data)
        player = Player(board)
        assert player.direction == Directions.UP
        assert len(player.directions) == 4

    def test_turn_right(self):
        """Test turning right."""
        board_data = [['.', '.'], ['.', '.']]
        board = Board(board_data)
        player = Player(board)
        
        assert player.direction == Directions.UP
        player.turn_right()
        assert player.direction == Directions.RIGHT
        player.turn_right()
        assert player.direction == Directions.DOWN
        player.turn_right()
        assert player.direction == Directions.LEFT
        player.turn_right()
        assert player.direction == Directions.UP  # Wraps around

    def test_move_up(self):
        """Test moving up."""
        board_data = [['.', '.'], ['.', '.']]
        board = Board(board_data)
        player = Player(board)
        player.direction = Directions.UP  # UP
        
        pos = Position(1, 1)
        new_pos = player.move(pos)
        assert new_pos.row == 0
        assert new_pos.col == 1

    def test_move_right(self):
        """Test moving right."""
        board_data = [['.', '.'], ['.', '.']]
        board = Board(board_data)
        player = Player(board)
        player.direction = Directions.RIGHT  # RIGHT
        
        pos = Position(1, 0)
        new_pos = player.move(pos)
        assert new_pos.row == 1
        assert new_pos.col == 1

    def test_move_down(self):
        """Test moving down."""
        board_data = [['.', '.'], ['.', '.']]
        board = Board(board_data)
        player = Player(board)
        player.direction = Directions.DOWN  # DOWN
        
        pos = Position(0, 1)
        new_pos = player.move(pos)
        assert new_pos.row == 1
        assert new_pos.col == 1

    def test_move_left(self):
        """Test moving left."""
        board_data = [['.', '.'], ['.', '.']]
        board = Board(board_data)
        player = Player(board)
        player.direction = Directions.LEFT  # LEFT
        
        pos = Position(1, 1)
        new_pos = player.move(pos)
        assert new_pos.row == 1
        assert new_pos.col == 0

    def test_move_out_of_bounds(self):
        """Test moving out of board bounds."""
        board_data = [['.', '.'], ['.', '.']]
        board = Board(board_data)
        player = Player(board)
        player.direction = Directions.UP  # UP
        
        pos = Position(0, 0)  # At top edge
        new_pos = player.move(pos)
        assert new_pos is None

    def test_is_valid_position(self):
        """Test checking if position is valid (doesn't contain character)."""
        board_data = [['.', '#'], ['#', '.']]
        board = Board(board_data)
        player = Player(board)
        
        assert player.is_valid_position(Position(0, 0), '#') is True
        assert player.is_valid_position(Position(0, 1), '#') is False

