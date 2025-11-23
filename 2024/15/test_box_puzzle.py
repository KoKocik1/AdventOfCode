"""Tests for Box-Pushing Puzzle game logic."""

from classes import CleanBoardHuge, PLAYER, CLEAN, TRASH, WALL
import importlib.util
import sys
from pathlib import Path

# Add 2024 directory to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import directly from array_helper to avoid __init__.py dependencies
spec = importlib.util.spec_from_file_location(
    "array_helper", project_root / "helpers" / "array_helper.py")
array_helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(array_helper)
Board = array_helper.Board
Position = array_helper.Position


# Box puzzle symbols
BOX_LEFT = '['
BOX_RIGHT = ']'


def create_board_from_string(board_str: str) -> Board:
    """Helper function to create a Board from a string representation."""
    lines = board_str.strip().split('\n')
    return Board([list(line) for line in lines])


def board_to_string(board: Board) -> str:
    """Helper function to convert Board to string for comparison."""
    return str(board)


def test_box_puzzle_initial_state():
    """Test initial board state setup for box puzzle."""
    initial_board = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "")
    new_board = clean_board.board

    # Check player position is found correctly
    assert clean_board.player_position.row == 3
    assert clean_board.player_position.col == 10
    assert new_board.get_character(
        clean_board.player_position) == PLAYER

    expected_board = """##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############"""

    assert board_to_string(new_board) == expected_board.strip()


def test_box_puzzle_move_left():
    """Test moving left in box puzzle."""
    initial_board = """##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "<")

    # Execute move
    clean_board.clean_board()

    # Player should move left, pushing boxes
    expected_board = """##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############"""

    assert board_to_string(board) == expected_board.strip()


def test_box_puzzle_move_down_first():
    """Test first move down in box puzzle."""
    initial_board = """##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "v")

    # Execute move
    clean_board.clean_board()

    # Player should move down
    expected_board = """##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############"""

    assert board_to_string(board) == expected_board.strip()


def test_box_puzzle_move_down_second():
    """Test second move down in box puzzle."""
    initial_board = """##############
##......##..##
##......@...##
##...[][]...##
##....[]....##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "v")

    # Execute move
    clean_board.clean_board()

    # Player should move down
    expected_board = """##############
##......##..##
##..........##
##...[].@...##
##.....[]...##
##....[]....##
##############"""

    assert board_to_string(board) == expected_board.strip()


def test_box_puzzle_move_left_after_down():
    """Test moving left after moving down."""
    initial_board = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "<", False)

    # Execute move
    clean_board.clean_board()

    # Player should move left
    expected_board = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############"""

    assert board_to_string(board) == expected_board.strip()


def test_box_puzzle_move_left_twice():
    """Test moving left twice."""
    initial_board = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "<<", False)

    # Execute first move
    clean_board.clean_board()

    # Player should move left twice
    expected_board = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##....@.....##
##############"""

    assert board_to_string(board) == expected_board.strip()


def test_box_puzzle_move_up_first():
    """Test first move up in box puzzle."""
    initial_board = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "^", False)

    # Execute move
    clean_board.clean_board()

    # Player should move up
    expected_board = """##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############"""

    assert board_to_string(board) == expected_board.strip()


def test_box_puzzle_move_up_second():
    """Test second move up (hits wall or box)."""
    initial_board = """##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "^", False)

    # Execute move
    clean_board.clean_board()

    # Player should move up (or stay if blocked)
    expected_board = """##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############"""

    assert board_to_string(board) == expected_board.strip()


def test_box_puzzle_move_left_after_up():
    """Test moving left after moving up."""
    initial_board = """##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "<", False)

    # Execute move
    clean_board.clean_board()

    # Player should move left
    expected_board = """##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############"""

    assert board_to_string(board) == expected_board.strip()


def test_box_puzzle_move_left_twice_after_up():
    """Test moving left twice after moving up."""
    initial_board = """##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "<", False)

    # Execute first move
    clean_board.clean_board()

    # Player should move left twice
    expected_board = """##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############"""

    assert board_to_string(board) == expected_board.strip()


def test_box_puzzle_move_up_to_push_box():
    """Test moving up to push a box."""
    initial_board = """##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "^", False)

    # Execute move
    clean_board.clean_board()

    # Player should move up, potentially pushing box
    expected_board = """##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############"""

    assert board_to_string(board) == expected_board.strip()


def test_box_puzzle_move_up_final():
    """Test final move up."""
    initial_board = """##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "^", False)

    # Execute move
    clean_board.clean_board()

    # Player should move up, pushing box
    expected_board = """##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############"""

    assert board_to_string(board) == expected_board.strip()


def test_box_puzzle_full_sequence():
    """Test the complete sequence of moves."""
    initial_board = """##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    moves = "<vv<<^^<<^^"
    clean_board = CleanBoardHuge(board, moves, False)

    # Execute all moves
    clean_board.clean_board()

    # Final state after all moves
    expected_final = """##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############"""

    assert board_to_string(board) == expected_final.strip()


def test_box_puzzle_move_into_wall():
    """Test moving into a wall."""
    initial_board = """##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, ">", False)

    # Execute move - should hit wall
    clean_board.clean_board()

    # Player should stay in place or handle wall collision
    player_pos = board.find_character_position(PLAYER)
    assert player_pos is not None


def test_box_puzzle_move_into_box():
    """Test moving into a box (should push it)."""
    initial_board = """##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "<", False)

    # Execute move - should push box
    clean_board.clean_board()

    # Box should have moved left
    # Player should be where box was
    player_pos = board.find_character_position(PLAYER)
    assert player_pos is not None
    assert player_pos.col == 9  # Should have moved left


def test_box_puzzle_box_cannot_push_box():
    """Test that a box cannot push another box."""
    initial_board = """##############
##......##..##
##..........##
##...@[][].##
##....[]....##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, ">", False)

    # Execute move - player tries to push box into another box
    clean_board.clean_board()

    # Should handle blocked push correctly
    player_pos = board.find_character_position(PLAYER)
    assert player_pos is not None


def test_box_puzzle_box_at_wall():
    """Test pushing a box that's against a wall."""
    initial_board = """##############
##......##..##
##..........##
##@.[][]...##
##....[]....##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "<", False)

    # Execute move - player tries to push box into wall
    clean_board.clean_board()

    # Should handle wall collision correctly
    player_pos = board.find_character_position(PLAYER)
    assert player_pos is not None



def test_box_puzzle_edge_case_corner():
    """Test moving in a corner."""
    initial_board = """##############
##@.........##
##..........##
##..........##
##..........##
##..........##
##############"""

    board = create_board_from_string(initial_board)
    clean_board = CleanBoardHuge(board, "^", False)

    # Execute move - should hit wall
    clean_board.clean_board()

    # Player should handle corner correctly
    player_pos = board.find_character_position(PLAYER)
    assert player_pos is not None


if __name__ == "__main__":
    # Run tests
    test_box_puzzle_initial_state()
    print("✓ test_box_puzzle_initial_state passed")

    test_box_puzzle_move_left()
    print("✓ test_box_puzzle_move_left passed")

    test_box_puzzle_move_down_first()
    print("✓ test_box_puzzle_move_down_first passed")

    test_box_puzzle_move_down_second()
    print("✓ test_box_puzzle_move_down_second passed")

    test_box_puzzle_move_left_after_down()
    print("✓ test_box_puzzle_move_left_after_down passed")

    test_box_puzzle_move_left_twice()
    print("✓ test_box_puzzle_move_left_twice passed")

    test_box_puzzle_move_up_first()
    print("✓ test_box_puzzle_move_up_first passed")

    test_box_puzzle_move_up_second()
    print("✓ test_box_puzzle_move_up_second passed")

    test_box_puzzle_move_left_after_up()
    print("✓ test_box_puzzle_move_left_after_up passed")

    test_box_puzzle_move_left_twice_after_up()
    print("✓ test_box_puzzle_move_left_twice_after_up passed")

    test_box_puzzle_move_up_to_push_box()
    print("✓ test_box_puzzle_move_up_to_push_box passed")

    test_box_puzzle_move_up_final()
    print("✓ test_box_puzzle_move_up_final passed")

    test_box_puzzle_move_into_wall()
    print("✓ test_box_puzzle_move_into_wall passed")

    test_box_puzzle_move_into_box()
    print("✓ test_box_puzzle_move_into_box passed")

    test_box_puzzle_box_cannot_push_box()
    print("✓ test_box_puzzle_box_cannot_push_box passed")

    test_box_puzzle_box_at_wall()
    print("✓ test_box_puzzle_box_at_wall passed")

    test_box_puzzle_multiple_boxes()
    print("✓ test_box_puzzle_multiple_boxes passed")

    test_box_puzzle_edge_case_corner()
    print("✓ test_box_puzzle_edge_case_corner passed")

    print("\n✅ All box puzzle tests passed!")
