"""Tests for _2025/_5/main.py functions."""

import pytest
import tempfile
import os
from _2025._5.main import part1, part2, read_range
from _2025._5.classes import Range
from helpers import GetFile


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        # Ranges: 3-5, 10-14, 16-20, 12-18
        # Ingredients: 1, 5, 8, 11, 17, 32
        # Expected: 3 (ingredients 5, 11, 17 are in ranges)
        ranges = [
            Range(3, 5),
            Range(10, 14),
            Range(16, 20),
            Range(12, 18),
        ]
        ingredients = [1, 5, 8, 11, 17, 32]
        
        result = part1(ranges, ingredients)
        
        assert result == 3


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        input_data = """3-5
7-9
12-14
2-4
1-8
6-9
11-12
16-19
8-18
21-22"""
        
        # Create a temporary file with the test data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(input_data)
            temp_path = f.name
        
        try:
            file = GetFile(temp_path, delimiter='-')
            ranges = read_range(file)
            
            result = part2(ranges)
            
            assert result == 21
        finally:
            # Clean up the temporary file
            os.unlink(temp_path)

