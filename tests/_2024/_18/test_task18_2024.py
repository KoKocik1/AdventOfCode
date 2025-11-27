"""Tests for _2024/_18/main.py functions."""

import pytest
from helpers.array_helper import Position
from _2024._18.main import part1, part2


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        # Points data: x,y format
        points_data = [
            (5, 4), (4, 2), (4, 5), (3, 0), (2, 1), (6, 3),
            (2, 4), (1, 5), (0, 6), (3, 3), (2, 6), (5, 1),
            (1, 2), (5, 5), (2, 5), (6, 5), (1, 4), (0, 4),
            (6, 4), (1, 1), (6, 1), (1, 0), (0, 5), (1, 6), (2, 0)
        ]
        
        # Convert to Position objects (note: load_points swaps x,y -> Position(y, x))
        points = [Position(int(y), int(x)) for x, y in points_data]
        
        size_x = 7
        size_y = 7
        obstacles_size = 12  # Take first 12 elements
        
        result = part1(points, size_x, size_y, obstacles_size)
        assert result == 22


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        # Points data: x,y format
        points_data = [
            (5, 4), (4, 2), (4, 5), (3, 0), (2, 1), (6, 3),
            (2, 4), (1, 5), (0, 6), (3, 3), (2, 6), (5, 1),
            (1, 2), (5, 5), (2, 5), (6, 5), (1, 4), (0, 4),
            (6, 4), (1, 1), (6, 1), (1, 0), (0, 5), (1, 6), (2, 0)
        ]

        # Convert to Position objects (note: load_points swaps x,y -> Position(y, x))
        points = [Position(int(y), int(x)) for x, y in points_data]

        size_x = 7
        size_y = 7
        obstacles_size = 12  # Take first 12 elements

        result_position, result_index = part2(
            points, size_x, size_y, obstacles_size)
        assert result_position == Position(1, 6)
