"""Tests for _2025/_3/main.py functions."""

import pytest
import tempfile
import os
from _2025._3.main import part1, part2, read_data
from helpers import GetFile


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        input_data = """987654321111111
811111111111119
234234234234278
818181911112111"""
        
        # Create a temporary file with the test data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(input_data)
            temp_path = f.name
        
        try:
            file = GetFile(temp_path, delimiter='')
            array = read_data(file)
            
            result = part1(array)
            
            assert result == 357
        finally:
            # Clean up the temporary file
            os.unlink(temp_path)


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        input_data = """987654321111111
811111111111119
234234234234278
818181911112111"""
        
        # Create a temporary file with the test data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(input_data)
            temp_path = f.name
        
        try:
            file = GetFile(temp_path, delimiter='')
            array = read_data(file)
            
            result = part2(array)
            
            assert result == 3121910778619
        finally:
            # Clean up the temporary file
            os.unlink(temp_path)

