"""Tests for _2024/_12/main.py functions."""

import pytest
from _2024._12.main import (
    calculate_fields,
)


def create_array_from_string(grid_str: str) -> list[list[str]]:
    """Helper function to create a 2D array from a string representation."""
    lines = grid_str.strip().split('\n')
    return [list(line) for line in lines]


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        grid_str = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
        
        array = create_array_from_string(grid_str)
        part1_result, _ = calculate_fields(array)
        assert part1_result == 1930


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        grid_str = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
        
        array = create_array_from_string(grid_str)
        _, part2_result = calculate_fields(array)
        assert part2_result == 1206

