"""Tests for _2024/_10/main.py functions."""

import pytest
from _2024._10.main import (
    part1,
    part2,
)


def create_array_from_string(grid_str: str) -> list[list[str]]:
    """Helper function to create a 2D array from a string representation."""
    lines = grid_str.strip().split('\n')
    return [list(line) for line in lines]


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        grid_str = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
        
        array = create_array_from_string(grid_str)
        result = part1(array)
        assert result == 36


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        grid_str = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
        
        array = create_array_from_string(grid_str)
        result = part2(array)
        assert result == 81

