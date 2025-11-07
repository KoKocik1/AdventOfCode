# horizontal, vertical, diagonal, written backwards, or even overlapping other words
# find all xmas words in the text
# write pytests
from pathlib import Path

from helpers import GetFile
from main import find_words, look_for_character_position
from classes import Word, Grid


def test_read_2d_array():
    """Test loading file to 2D array."""
    data_file = Path(__file__).parent / 'test.txt'
    # Empty delimiter for character-by-character reading
    file_reader = GetFile(data_file, '')
    grid = file_reader.get_2d_array()

    # Check it's a 2D array
    assert isinstance(grid, list)
    assert len(grid) == 10  # 10 rows
    assert all(isinstance(row, list) for row in grid)

    # Check first row matches expected
    assert grid[0] == ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M']

    # Check all rows have same length (10 columns)
    assert all(len(row) == 10 for row in grid)

    # Check a specific cell
    assert grid[4][0] == 'X'  # Row 5 (0-indexed 4), Column 1 (0-indexed 0)
    assert grid[4][1] == 'M'  # Row 5, Column 2
    assert grid[4][2] == 'A'  # Row 5, Column 3
    assert grid[4][3] == 'S'  # Row 5, Column 4 - should be "XMAS" horizontally

    print("✓ 2D array loaded successfully!")
    print(f"  Dimensions: {len(grid)} rows x {len(grid[0])} columns")
    print(f"  First row: {''.join(grid[0])}")
    print(f"  Row 5: {''.join(grid[4])}")


def test_find_xmas_test_words():
    """Test finding XMAS words in the test file."""
    data_file = Path(__file__).parent / 'test.txt'
    file_reader = GetFile(data_file, '')
    grid = Grid(file_reader.get_2d_array())

    word = Word("XMAS")
    positions = look_for_character_position(grid, word.get_character(0))
    found_words = find_words(grid, word, positions)
    # Check vertical occurrences of XMAS
    assert found_words == 18
