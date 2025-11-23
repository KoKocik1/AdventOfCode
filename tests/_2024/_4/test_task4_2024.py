"""Tests for _2024/_4/main.py functions."""

import pytest
from _2024._4.main import (
    task1,
    task2,
    GridFinder,
    GridFinderX,
)



def create_grid_from_string(grid_str: str) -> list[list[str]]:
    """Helper function to create a 2D grid from a string representation."""
    lines = grid_str.strip().split('\n')
    return [list(line) for line in lines]


class TestPart1:
    """Tests for task1 (part1) function."""

    def test_given_data(self):
        """Test with the provided test data."""
        grid_str = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
        
        two_d_array = create_grid_from_string(grid_str)
        grid = GridFinder(two_d_array)
        result = task1(grid)
        assert result == 18


class TestPart2:
    """Tests for task2 (part2) function."""

    def test_given_data(self):
        """Test with the provided test data."""
        grid_str = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
        
        two_d_array = create_grid_from_string(grid_str)
        grid_x = GridFinderX(two_d_array)
        result = task2(grid_x)
        assert result == 9

