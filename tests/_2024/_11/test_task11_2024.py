"""Tests for _2024/_11/main.py functions."""

import pytest
from _2024._11.main import (
    part1,
    part2,
)


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        # Input: "125 17" split by space delimiter
        rows = ['125', '17']
        blinks = 25
        
        result = part1(rows, blinks)
        assert result == 55312
