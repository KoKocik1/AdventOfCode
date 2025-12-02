"""Tests for _2025/_1/main.py functions."""

import pytest
from _2025._1.main import part1, part2
from _2025._1.classes import parse_rotation


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        rotations = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ]
        array = [parse_rotation(rotation) for rotation in rotations]
        
        result = part1(array)
        
        assert result == 3


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        rotations = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ]
        array = [parse_rotation(rotation) for rotation in rotations]
        
        result = part2(array)
        
        assert result == 6

