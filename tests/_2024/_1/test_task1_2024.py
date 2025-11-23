"""Tests for _2024/_1/main.py functions."""

import pytest
from _2024._1.main import (
    quicksort,
    part1,
    part2,
)


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        list1 = [3, 4, 2, 1, 3, 3]
        list2 = [4, 3, 5, 3, 9, 3]
        
        sorted1 = quicksort(list1)
        sorted2 = quicksort(list2)
        
        result1 = part1(sorted1, sorted2)
        
        assert result1 == 11


class TestPart2:

    def test_given_data(self):
        """Test with the provided test data."""
        list1 = [3, 4, 2, 1, 3, 3]
        list2 = [4, 3, 5, 3, 9, 3]
        
        sorted1 = quicksort(list1)
        sorted2 = quicksort(list2)
        
        result2 = part2(sorted1, sorted2)
        
        assert result2 == 31

